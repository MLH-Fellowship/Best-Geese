import { debugOutputAstAsTypeScript } from '@angular/compiler';
import { Component, OnInit, Inject } from '@angular/core';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
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
    public fb: FormBuilder,
    public dialogRef: MatDialogRef<QuizCreatorComponent>,
    @Inject(MAT_DIALOG_DATA) {questions, difficulty, subject}
  ) {
    this.form = fb.group({
      questions: [questions, [Validators.min(10), Validators.max(50), Validators.required]],
      difficulty: [difficulty, Validators.required],
      subject: [subject.name.toLowerCase()]
    });
  }

  ngOnInit(): void {
    //this.form = this.fb.group({
      //description: [this.description, []]
    //});
  }

  close() {
    this.dialogRef.close();
  }

  save() {
    if (this.form.valid){
      this.dialogRef.close(this.form.value);
    }
  }

  levels: Level[] = [
    {value: 'easy', viewValue: 'Easy'},
    {value: 'medium', viewValue: 'Medium'},
    {value: 'hard', viewValue: 'Hard'},
    {value: 'mixed', viewValue: 'Mixed'}
  ];

}