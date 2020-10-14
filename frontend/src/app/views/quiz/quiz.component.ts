import { Component, OnInit } from '@angular/core';
import { ActivatedRoute} from '@angular/router';
import { QuestionProviderService } from 'src/app/core/question-provider.service';
import { IQuestion } from 'src/app/interfaces/iquestion';

@Component({
  selector: 'app-quiz',
  templateUrl: './quiz.component.html',
  styleUrls: ['./quiz.component.css']
})
export class QuizComponent implements OnInit {

  questions: IQuestion[];
  answers = new Map();
  result = "";
  constructor(public provider: QuestionProviderService, route: ActivatedRoute) {
    let num_of_questions: number;
    let subject: string;
    let difficulty: string;
    route.paramMap.subscribe(res => num_of_questions = parseInt(res.get('number')));
    route.paramMap.subscribe(res => subject = res.get("subject"));
    route.paramMap.subscribe(res => difficulty = res.get("diff"));
    provider.getQuiz(num_of_questions, difficulty, subject);
    provider.questions$.subscribe(response => {this.questions = response});
  }

  onAnswer(questionState) {
    this.answers.set(questionState[0], questionState[1]);
  }

  finish() {
    console.log("Answers size: ", this.answers.size)
    console.log("Questions length: ", this.questions.length)
    if (this.answers.size < this.questions.length) {
      this.result = "Please answer all questions!"
      return;
    } else {
      let an = [];
      this.answers.forEach(el => an.push(el));
      let correct = an.filter(el => el == true);
      this.result = `You got ${correct.length} out of ${this.questions.length} correct!`
    }
  }
  ngOnInit(): void {
  }

}
