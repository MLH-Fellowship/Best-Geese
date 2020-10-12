import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http'
import { IQuestion } from '../interfaces/iquestion';
import { AuthService } from './auth.service';

@Injectable({
  providedIn: 'root'
})
export class QuestionProviderService {
  // Question list for current session.
  private _questions: BehaviorSubject<IQuestion[]> = new BehaviorSubject([]);
  private authHeader: any;
  public readonly questions$: Observable<IQuestion[]> = this._questions.asObservable();

  // Backend question provider address.
  private backendUrl: string = "http://localhost:5000/api";

  constructor(private http: HttpClient, private auth: AuthService) { 
    // When this service is initialized, there should be no questions,
    // but we do need the http client to be available within this service.
    // The authHeader property needs to be set after auth is initialized, as seen below.
    this.authHeader = {
      headers: this.auth.authToken || localStorage.getItem('auth_token' || "")
    };
   }

   /// This gets all questions from the database. DO NOT USE THIS UNLESS YOU ARE WILLING TO WAIT.
   public getAllQuestions(): void {
     this.http.get(`${this.backendUrl}/questions`)
     .subscribe(response => this._questions.next(response as IQuestion[]));
   }

   /**
    * This adds a single question to the database.
    * @param question 
    */
   public addQuestion(question: IQuestion): void {
     this.http.post(`${this.backendUrl}/questions`, question, {headers: this.authHeader});
   }

   /**
    * This updates a question in the database. The optional id property in IQuestion must be filled out for this to function.
    * @param question 
    */
   public updateQuestion(question: IQuestion) : void {
     if (question.id == undefined) {return}
     this.http.put(`${this.backendUrl}/questions`, question, {headers: this.authHeader});
   }

   /**
    *This takes a question object with the id property or just an id, and deletes that from the database.
    * @param questionID 
    */
   public deleteQuestion(questionID: string | IQuestion) {
     let URIend = typeof questionID == "string" ? questionID : questionID.id || undefined;
     this.http.delete(`${this.backendUrl}/questions/${URIend}`);
   }

   /**
    * Sets the questions of the service to a quiz generated based on params.
    * @param questions 
    * @param difficulty 
    * @param subject 
    */
   public getQuiz(questions: number, difficulty: string, subject: string): void {
    this.http.get(`${this.backendUrl}/play/`, {
      headers: this.authHeader,
      params: {'tag': subject, 'num_of_questions': questions.toString(), 'difficulty': difficulty}
    }).subscribe(response => this._questions.next(response as IQuestion[]));
   }

}
