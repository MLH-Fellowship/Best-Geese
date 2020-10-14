import { QuizCreatorComponent } from './../quiz-creator/quiz-creator.component';
import { subjects } from './../../subjects';
import { Component, OnInit } from '@angular/core';
import { MatDialog, MatDialogConfig } from '@angular/material/dialog';
import { Router } from '@angular/router';

@Component({
  selector: 'app-subject',
  templateUrl: './subject.component.html',
  styleUrls: ['./subject.component.css']
})
export class SubjectComponent implements OnInit {
  subjects = subjects;
  constructor(
    public dialog: MatDialog,
    private router: Router
  ) { }

  ngOnInit(): void {
  }

  openDialog(subject) {
    const dialogConfig = new MatDialogConfig();

    dialogConfig.disableClose = true;
    dialogConfig.autoFocus = true;
    // how do we pass the button that we clicked on?
    dialogConfig.data = {
      id: 1,
      subject: subject
    };

    const dialogRef = this.dialog.open(QuizCreatorComponent, dialogConfig);

    dialogRef.afterClosed().subscribe(
      data => {
        if (data) {
          this.router.navigateByUrl(`/quiz/${data.subject}/${data.questions}/${data.difficulty}`, {skipLocationChange: true});
        }
      }
    );
  }
}
