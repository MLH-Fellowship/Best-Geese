import { Component, OnInit } from '@angular/core';
import { MatDialogRef } from "@angular/material/dialog";
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
 
  constructor(
    public dialogRef: MatDialogRef<QuizCreatorComponent>
  ) { }

  ngOnInit(): void {
  }

  close() {
    this.dialogRef.close("Thanks for using me!");
  }
  levels: Level[] = [
    {value: 'easy-0', viewValue: 'Easy'},
    {value: 'medium-1', viewValue: 'Medium'},
    {value: 'hard-2', viewValue: 'Hard'},
    {value: 'mixed-2', viewValue: 'Mixed'}
  ];

}
