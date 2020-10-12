import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  constructor(private http: HttpClient) {
    this.authToken = localStorage.getItem("auth_token") || "";
  }

  public authToken: string = ""

  private backendUrl: string = "http://localhost:5000/api";

  public logIn(email:string, pass:string) : void {
    this.http.post(`${this.backendUrl}/auth/login`, {"email": email, "password": pass})
    .subscribe((response: any) => {
      this.saveToken(response.token)
    })
  }

  public signUp(email: string, pass:string) : void {
    this.http.post(`${this.backendUrl}/auth/signup`, {"email": email, "password": pass})
    .subscribe(() => {}, error => console.log(error));
  }
  
  public signOut() : void {
    localStorage.removeItem('auth_token');

    this.authToken = "";
  }

  private saveToken(token: any): void {
    this.authToken = token;
    localStorage.setItem('auth_token', token);
    return token;
  }

  public isAuthenticated(): boolean {
    return this.authToken != "";
  }

}
