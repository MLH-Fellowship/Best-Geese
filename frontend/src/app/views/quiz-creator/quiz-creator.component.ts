import { debugOutputAstAsTypeScript } from '@angular/compiler';
import { Component, OnInit, Inject } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { MatDialogRef, MAT_DIALOG_DATA } from "@angular/material/dialog";
interface Level {
  value: string;
  viewValue: string;
}

@Component({
  selector: 'app-quiz-creator',
  templateUrl: './quiz-creator.component.html',
  styleUrls: ['./quiz-creator.component.css']
})
export class QuizCreatorComponent implements OnInit {
  form: FormGroup;
  description: string;

  constructor(
    private fb: FormBuilder,
    public dialogRef: MatDialogRef<QuizCreatorComponent>,
    @Inject(MAT_DIALOG_DATA) {questions, difficulty, subject}
  ) {
    this.form = fb.group({
      questions: [questions],
      difficulty: [difficulty],
      subject: [subject]
    });
  }

  ngOnInit(): void {
    this.form = this.fb.group({
      description: [this.description, []]
    });
  }

  close() {
    this.dialogRef.close();
  }

  save() {
    this.dialogRef.close(this.form.value);
  }

  levels: Level[] = [
    {value: 'easy-0', viewValue: 'Easy'},
    {value: 'medium-1', viewValue: 'Medium'},
    {value: 'hard-2', viewValue: 'Hard'},
    {value: 'mixed-2', viewValue: 'Mixed'}
  ];

}
