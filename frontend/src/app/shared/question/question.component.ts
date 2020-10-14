import { Component, Input, OnInit } from '@angular/core';
import { IQuestion } from 'src/app/interfaces/iquestion';

@Component({
  selector: 'app-question',
  templateUrl: './question.component.html',
  styleUrls: ['./question.component.css']
})
export class QuestionComponent implements OnInit {

  @Input('question') question: IQuestion;
  constructor() { }

  ngOnInit(): void {
  }

}
