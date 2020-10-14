import { Component, OnInit, Inject } from '@angular/core';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
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
    { value: 'easy-0', viewValue: 'Easy' },
    { value: 'medium-1', viewValue: 'Medium' },
    { value: 'hard-2', viewValue: 'Hard' },
    { value: 'mixed-2', viewValue: 'Mixed' }
  ];

}
