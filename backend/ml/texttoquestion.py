# Common imports
import pandas as pd
import _pickle as cPickle

from pathlib import Path

import spacy
from spacy import displacy

import gensim
from gensim.test.utils import datapath, get_tmpfile
from gensim.models import KeyedVectors
from gensim.scripts.glove2word2vec import glove2word2vec

import sklearn

import json
import os

class TextToQuestion(object):

    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')
        tmp_file = 'ml/data/embeddings/word2vec-glove.6B.300d.txt'

        self.model = KeyedVectors.load_word2vec_format(tmp_file)

    def dumpPickle(self,fileName, content):
        pickleFile = open(fileName, 'wb')
        cPickle.dump(content, pickleFile, -1)
        pickleFile.close()

    def loadPickle(self,fileName):    
        file = open(fileName, 'rb')
        content = cPickle.load(file)
        file.close()
    
        return content
        
    def pickleExists(self,fileName):
        file = Path(fileName)
        
        if file.is_file():
            return True
        
        return False

    #Extract answers and the sentence they are in
    def extractAnswers(self,qas, doc):
        answers = []

        senStart = 0
        senId = 0

        for sentence in doc.sents:
            senLen = len(sentence.text)

            for answer in qas:
                answerStart = answer['answers'][0]['answer_start']

                if (answerStart >= senStart and answerStart < (senStart + senLen)):
                    answers.append({'sentenceId': senId, 'text': answer['answers'][0]['text']})

            senStart += senLen
            senId += 1
        
        return answers

    #TODO - Clean answers from stopwords?
    def tokenIsAnswer(self,token, sentenceId, answers):
        for i in range(len(answers)):
            if (answers[i]['sentenceId'] == sentenceId):
                if (answers[i]['text'] == token):
                    return True
        return False

    #Save named entities start points

    def getNEStartIndexs(self,doc):
        neStarts = {}
        for ne in doc.ents:
            neStarts[ne.start] = ne
            
        return neStarts 

    def getSentenceStartIndexes(self,doc):
        senStarts = []
        
        for sentence in doc.sents:
            senStarts.append(sentence[0].i)
        
        return senStarts
        
    def getSentenceForWordPosition(self,wordPos, senStarts):
        for i in range(1, len(senStarts)):
            if (wordPos < senStarts[i]):
                return i - 1
            
    def addWordsForParagrapgh(self,newWords, text):
        doc = self.nlp(text)

        neStarts = self.getNEStartIndexs(doc)
        senStarts = self.getSentenceStartIndexes(doc)
        
        #index of word in spacy doc text
        i = 0
        
        while (i < len(doc)):
            #If the token is a start of a Named Entity, add it and push to index to end of the NE
            if (i in neStarts):
                word = neStarts[i]
                #add word
                currentSentence = self.getSentenceForWordPosition(word.start, senStarts)
                wordLen = word.end - word.start
                shape = ''
                for wordIndex in range(word.start, word.end):
                    shape += (' ' + doc[wordIndex].shape_)

                newWords.append([word.text,
                                0,
                                0,
                                currentSentence,
                                wordLen,
                                word.label_,
                                None,
                                None,
                                None,
                                shape])
                i = neStarts[i].end - 1
            #If not a NE, add the word if it's not a stopword or a non-alpha (not regular letters)
            else:
                if (doc[i].is_stop == False and doc[i].is_alpha == True):
                    word = doc[i]

                    currentSentence = self.getSentenceForWordPosition(i, senStarts)
                    wordLen = 1

                    newWords.append([word.text,
                                    0,
                                    0,
                                    currentSentence,
                                    wordLen,
                                    None,
                                    word.pos_,
                                    word.tag_,
                                    word.dep_,
                                    word.shape_])
            i += 1

    def oneHotEncodeColumns(self,df):
        columnsToEncode = ['NER', 'POS', "TAG", 'DEP']

        for column in columnsToEncode:
            one_hot = pd.get_dummies(df[column])
            one_hot = one_hot.add_prefix(column + '_')

            df = df.drop(column, axis = 1)
            df = df.join(one_hot)
        
        return df


    def generateDf(self,text):
        words = []
        self.addWordsForParagrapgh(words, text)

        wordColums = ['text', 'titleId', 'paragrapghId', 'sentenceId','wordCount', 'NER', 'POS', 'TAG', 'DEP','shape']
        df = pd.DataFrame(words, columns=wordColums)
        
        return df


    def prepareDf(self,df):
        #One-hot encoding
        wordsDf = self.oneHotEncodeColumns(df)

        #Drop unused columns
        columnsToDrop = ['text', 'titleId', 'paragrapghId', 'sentenceId', 'shape']
        wordsDf = wordsDf.drop(columnsToDrop, axis = 1)

        #Add missing colums 
        predictorColumns = ['wordCount','NER_CARDINAL','NER_DATE','NER_EVENT','NER_FAC','NER_GPE','NER_LANGUAGE','NER_LAW','NER_LOC','NER_MONEY','NER_NORP','NER_ORDINAL','NER_ORG','NER_PERCENT','NER_PERSON','NER_PRODUCT','NER_QUANTITY','NER_TIME','NER_WORK_OF_ART','POS_ADJ','POS_ADP','POS_ADV','POS_CCONJ','POS_DET','POS_INTJ','POS_NOUN','POS_NUM','POS_PART','POS_PRON','POS_PROPN','POS_PUNCT','POS_SYM','POS_VERB','POS_X','TAG_''','TAG_-LRB-','TAG_.','TAG_ADD','TAG_AFX','TAG_CC','TAG_CD','TAG_DT','TAG_EX','TAG_FW','TAG_IN','TAG_JJ','TAG_JJR','TAG_JJS','TAG_LS','TAG_MD','TAG_NFP','TAG_NN','TAG_NNP','TAG_NNPS','TAG_NNS','TAG_PDT','TAG_POS','TAG_PRP','TAG_PRP$','TAG_RB','TAG_RBR','TAG_RBS','TAG_RP','TAG_SYM','TAG_TO','TAG_UH','TAG_VB','TAG_VBD','TAG_VBG','TAG_VBN','TAG_VBP','TAG_VBZ','TAG_WDT','TAG_WP','TAG_WRB','TAG_XX','DEP_ROOT','DEP_acl','DEP_acomp','DEP_advcl','DEP_advmod','DEP_agent','DEP_amod','DEP_appos','DEP_attr','DEP_aux','DEP_auxpass','DEP_case','DEP_cc','DEP_ccomp','DEP_compound','DEP_conj','DEP_csubj','DEP_csubjpass','DEP_dative','DEP_dep','DEP_det','DEP_dobj','DEP_expl','DEP_intj','DEP_mark','DEP_meta','DEP_neg','DEP_nmod','DEP_npadvmod','DEP_nsubj','DEP_nsubjpass','DEP_nummod','DEP_oprd','DEP_parataxis','DEP_pcomp','DEP_pobj','DEP_poss','DEP_preconj','DEP_predet','DEP_prep','DEP_prt','DEP_punct','DEP_quantmod','DEP_relcl','DEP_xcomp']

        for feature in predictorColumns:
            if feature not in wordsDf.columns:
                wordsDf[feature] = 0
        
        return wordsDf


    def predictWords(self,wordsDf, df):
        
        predictorPickleName = 'ml/data/pickles/nb-predictor.pkl'
        predictor = self.loadPickle(predictorPickleName)
        
        y_pred = predictor.predict_proba(wordsDf)

        labeledAnswers = []
        for i in range(len(y_pred)):
            labeledAnswers.append({'word': df.iloc[i]['text'], 'prob': y_pred[i][0]})
        
        return labeledAnswers


    def addQuestions(self,answers, text):
        doc = self.nlp(text)
        currAnswerIndex = 0
        qaPair = []

        #Check wheter each token is the next answer
        for sent in doc.sents:
            for token in sent:
                
                #If all the answers have been found, stop looking
                if currAnswerIndex >= len(answers):
                    break
                
                #In the case where the answer is consisted of more than one token, check the following tokens as well.
                answerDoc = self.nlp(answers[currAnswerIndex]['word'])
                answerIsFound = True
                
                for j in range(len(answerDoc)):
                    if token.i + j >= len(doc) or doc[token.i + j].text != answerDoc[j].text:
                        answerIsFound = False
            
                #If the current token is corresponding with the answer, add it 
                if answerIsFound:
                    question = self.blankAnswer(token.i, token.i + len(answerDoc) - 1, sent.start, sent.end, doc)
                    
                    qaPair.append({'question' : question, 'option_1': answers[currAnswerIndex]['word'],'correct_answer' : 'option_1','prob': answers[currAnswerIndex]['prob']})
                    
                    currAnswerIndex += 1
                    
        return qaPair

    def sortAnswers(self,qaPairs):
        orderedQaPairs = sorted(qaPairs, key=lambda qaPair: qaPair['prob'])
        
        return orderedQaPairs


    ## Extract questions
    def blankAnswer(self,firstTokenIndex, lastTokenIndex, sentStart, sentEnd, doc):
        leftPartStart = doc[sentStart].idx
        leftPartEnd = doc[firstTokenIndex].idx
        rightPartStart = doc[lastTokenIndex].idx + len(doc[lastTokenIndex])
        rightPartEnd = doc[sentEnd - 1].idx + len(doc[sentEnd - 1])
        
        question = doc.text[leftPartStart:leftPartEnd] + '_____' + doc.text[rightPartStart:rightPartEnd]
        
        return question

    ## Distractors
    def generate_distractors(self,answer, count):
        answer = str.lower(answer)
        
        ##Extracting closest words for the answer. 
        try:
            closestWords = self.model.most_similar(positive=[answer], topn=count)
        except:
            #In case the word is not in the vocabulary, or other problem not loading embeddings
            return []

        #Return count many distractors
        distractors = list(map(lambda x: x[0], closestWords))[0:count]
        
        return distractors

    def addDistractors(self,qaPairs, count=3):
        for qaPair in qaPairs:
            distractors = self.generate_distractors(qaPair['option_1'], count)
            for i in range(0,len(distractors)):
                    qaPair[f'option_{i+1}'] = distractors[i]
            #qaPair['distractors'] = distractors
        
        return qaPairs


    def generateQuestions(self,text:str, count:int):
        
        # Extract words 
        df = self.generateDf(text)
        wordsDf = self.prepareDf(df)
        
        # Predict 
        labeledAnswers = self.predictWords(wordsDf, df)
        
        # Transform questions
        qaPairs = self.addQuestions(labeledAnswers, text)
        
        # Pick the best questions
        orderedQaPairs = self.sortAnswers(qaPairs)
        
        # Generate distractors
        questions = self.addDistractors(orderedQaPairs[:count], 4)
        with open('questions.json', 'w') as fp:
            json.dump(questions, fp)

        
        return questions

    def remove_prob_and_send_to_db(self,questions:str):
            with open(questions, 'r') as fp:
                res = json.loads(fp.read())
                # print(res)
                ques = []
                for question in res:
                    # print(question)
                    if 'prob' in question: del question['prob']

            os.remove(questions) 
            return res





