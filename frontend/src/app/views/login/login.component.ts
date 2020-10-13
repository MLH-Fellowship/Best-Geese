import { AuthService } from 'src/app/core/auth.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  constructor(
    private Auth: AuthService
  ) { }

  ngOnInit(): void {
  }

  loginUser(event) {
    event.preventDefault()
    const target = event.target
    const username = target.querySelector('#email').value
    const password = target.querySelector('#password').value

    console.log(username, password)
  }

}
