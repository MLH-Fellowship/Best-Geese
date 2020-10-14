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

  ngOnInit(): void {
  }

}
