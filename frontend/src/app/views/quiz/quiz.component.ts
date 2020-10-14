import { Component, OnInit } from '@angular/core';
import { QuestionProviderService } from 'src/app/core/question-provider.service';
import { IQuestion } from 'src/app/interfaces/iquestion';

@Component({
  selector: 'app-quiz',
  templateUrl: './quiz.component.html',
  styleUrls: ['./quiz.component.css']
})
export class QuizComponent implements OnInit {

  questions: IQuestion[];
  constructor(public provider: QuestionProviderService) {
    provider.getQuiz(10, 'easy', 'biology')
    provider.questions$.subscribe(response => this.questions = response);
  }

  getQuiz() {
    this.provider.questions$.subscribe(response => this.questions = response);
    console.log(this.questions)
  }

  ngOnInit(): void {
  }

}
