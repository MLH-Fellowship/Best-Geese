import { ConditionalExpr } from '@angular/compiler';
import { Component, OnInit } from '@angular/core';
import { AuthService } from 'src/app/core/auth.service';
import { QuestionProviderService } from 'src/app/core/question-provider.service';
import { IQuestion } from 'src/app/interfaces/iquestion';

@Component({
  selector: 'app-question-list',
  templateUrl: './question-list.component.html',
  styleUrls: ['./question-list.component.css']
})
export class QuestionListComponent implements OnInit {
  public questions: IQuestion[] = [];
  constructor(private questionProvider: QuestionProviderService) {
  }
  
  getQuestions(): void {
    this.questionProvider.getAllQuestions();
    this.questionProvider.questions$.subscribe(res => this.questions = res);
  }

  ngOnInit(): void {
  }

}
