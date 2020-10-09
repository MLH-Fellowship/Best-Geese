import { subjects } from './../../subjects';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-subject',
  templateUrl: './subject.component.html',
  styleUrls: ['./subject.component.css']
})
export class SubjectComponent implements OnInit {
  subjects = subjects;
  constructor() { }

  ngOnInit(): void {
  }

}
