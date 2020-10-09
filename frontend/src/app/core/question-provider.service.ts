import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http'
import { IQuestion } from '../interfaces/iquestion';

@Injectable({
  providedIn: 'root'
})
export class QuestionProviderService {
  private _questions: BehaviorSubject<IQuestion[]> = new BehaviorSubject([]);
  public readonly questions$: Observable<IQuestion[]> = this._questions.asObservable();
  private backendUrl: string = "localhost:9000";

  constructor(private http: HttpClient) { 
    this.getQuestions();
   }

   public getQuestions(questions: number = 15): void {
     this.http.post(`${this.backendUrl}/getQuestions`, {'questions': questions})
     .subscribe(response => this._questions.next(response as IQuestion[]));
   }

}
