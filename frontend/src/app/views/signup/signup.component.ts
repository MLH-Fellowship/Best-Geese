import { AuthService } from 'src/app/core/auth.service';
import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router'

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.css']
})
export class SignupComponent implements OnInit {
  registerUserData = {
    email: '',
    pass: ''
  }
  constructor(
    private _auth: AuthService,
    private _router: Router
    ) { }

  ngOnInit(): void{
  }

  signUp() {
    console.log(this.registerUserData)
    this._auth.signUp(this.registerUserData.email, this.registerUserData.pass)
    this._router.navigate([''])
  }

}
