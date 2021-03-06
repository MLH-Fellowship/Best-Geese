import { AuthService } from 'src/app/core/auth.service';
import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router'

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  loginUserData = {
    email: '',
    pass: ''
  }
  constructor(
    private _auth: AuthService,
    private _router: Router
  ) { }

  ngOnInit(): void {
  }

  loginUser() {
    console.log(this.loginUserData)
    this._auth.logIn(this.loginUserData.email, this.loginUserData.pass)
    this._router.navigate([''])
  }

}
