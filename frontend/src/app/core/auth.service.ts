import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  constructor(private http: HttpClient) {
    // Retrieve the auth token if it exists already.
    this.authToken = localStorage.getItem("auth_token") || "";
  }

  public authToken: string = ""

  private backendUrl: string = "http://localhost:5000/api";

  /**
   * Logs a user into the application.
   * 
   * This function logs the user in, saving the JWT token to
   * the service property authToken and the localStorage item auth_token. 
   * @param email 
   * @param pass 
   */
  public logIn(email:string, pass:string) : void {
    this.http.post(`${this.backendUrl}/auth/login`, {"email": email, "password": pass})
    .subscribe((response: any) => {
      this.saveToken(response.token)
    })
  }

  /**
   * Signs a user up with an account.
   * @param email 
   * @param pass 
   */
  public signUp(email: string, pass:string) : void {
    this.http.post(`${this.backendUrl}/auth/signup`, {"email": email, "password": pass})
    .subscribe(() => {}, error => console.log(error));
  }
  
  /**
   * Logs out the currently authenticated user.
   */
  public signOut() : void {
    localStorage.removeItem('auth_token');

    this.authToken = "";
  }

  /**
   * Saves a token to local storage and to a service property.
   * 
   * @param token 
   */
  private saveToken(token: any): void {
    this.authToken = token;
    localStorage.setItem('auth_token', token);
    return token;
  }

  /**
   * Checks if the user is authenticated and returns a boolean.
   */
  public isAuthenticated(): boolean {
    if (this.authToken != "") {
      this.authToken = localStorage.getItem("auth_token") || "";
    }
    return this.authToken != "";
  }

}
