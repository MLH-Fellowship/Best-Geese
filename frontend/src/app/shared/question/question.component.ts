import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { IQuestion } from 'src/app/interfaces/iquestion';

@Component({
  selector: 'app-question',
  templateUrl: './question.component.html',
  styleUrls: ['./question.component.css']
})
export class QuestionComponent implements OnInit {

  options: string[];
  @Input('question') question: IQuestion;
  @Output('answer') answer: EventEmitter<any> = new EventEmitter();
  constructor() {}

  answerQuestion(option: string) {
      this.answer.emit([this.question.id, this.question[this.question.correct_answer] == option]);
  }

  ngOnInit(): void {
    let q = this.question;
    this.options = [q.option_1, q.option_2, q.option_3, q.option_4]
    // Shuffle the options
    {
      for (var i = this.options.length - 1; i > 0; i--) {
        var j = Math.floor(Math.random() * (i + 1));
        var temp = this.options[i];
        this.options[i] = this.options[j];
        this.options[j] = temp;
      }
    }
    console.log(this.question); console.log(this.options)
  }

}
