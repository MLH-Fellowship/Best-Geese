import { QuestionProviderService } from 'src/app/core/question-provider.service';
import { Component, OnInit, Inject } from '@angular/core';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators, FormControl } from '@angular/forms';
interface Level {
  value: string;
  viewValue: string;
}

@Component({
  selector: 'app-quiz-add',
  templateUrl: './quiz-add.component.html',
  styleUrls: ['./quiz-add.component.css']
})
export class QuizAddComponent implements OnInit {
  form: FormGroup;
  constructor(
    public fb: FormBuilder,
    private _question: QuestionProviderService,
  ) {
    this.form = fb.group({
      tag: [''],
      difficulty: [''],
      question: [''],
      option_1: [''],
      option_2: [''],
      option_3: [''],
      option_4: [''],
      correct_answer: ['']
    });
  }

  ngOnInit(): void {
  }

  levels: Level[] = [
    { value: 'easy', viewValue: 'Easy' },
    { value: 'medium', viewValue: 'Medium' },
    { value: 'hard', viewValue: 'Hard' },
    { value: 'mixed', viewValue: 'Mixed' }
  ];

  addQuestion() {
    console.log(this.form)
    this._question.addQuestion({
      tag: this.form.value.tag,
      difficulty: this.form.value.difficulty,
      question: this.form.value.question,
      option_1: this.form.value.option_1,
      option_2: this.form.value.option_2,
      option_3: this.form.value.option_3,
      option_4: this.form.value.option_4,
      correct_answer: this.form.value.correct_answer
    })
  }

}
