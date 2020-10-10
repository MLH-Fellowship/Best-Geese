import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http'
import { IQuestion } from '../interfaces/iquestion';

@Injectable({
  providedIn: 'root'
})
export class QuestionProviderService {
  // Question list for current session.
  private _questions: BehaviorSubject<IQuestion[]> = new BehaviorSubject([]);
  public readonly questions$: Observable<IQuestion[]> = this._questions.asObservable();

  // Backend question provider address.
  private backendUrl: string = "http://localhost:5000/api";

  constructor(private http: HttpClient) { 
    // When this service is initialized, there should be no questions,
    // but we do need the http client to be available within this service.
   }

   public getAllQuestions(): void {
     this.http.get(`${this.backendUrl}/questions`)
     .subscribe(response => this._questions.next(response as IQuestion[]));
   }

}
