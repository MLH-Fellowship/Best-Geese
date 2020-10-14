import { AuthService } from 'src/app/core/auth.service';
import { MaterialModule } from './material.module';
import { RouterModule } from '@angular/router';
import { BrowserModule } from '@angular/platform-browser';
import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { LayoutModule } from '@angular/cdk/layout';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { FlexLayoutModule } from '@angular/flex-layout';
import { HttpClientModule } from '@angular/common/http'

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './views/login/login.component';
import { SignupComponent } from './views/signup/signup.component';
import { HomepageComponent } from './views/homepage/homepage.component';
import { ProgressComponent } from './views/progress/progress.component';
import { SubjectComponent } from './views/subject/subject.component';
import { MainNavComponent } from './shared/main-nav/main-nav.component';
import { QuestionListComponent } from './shared/question-list/question-list.component';
import { QuizComponent } from './views/quiz/quiz.component';
import { QuestionComponent } from './shared/question/question.component';
import { AuthGuard } from './core/auth.guard';
import { QuizCreatorComponent } from './views/quiz-creator/quiz-creator.component';


@NgModule({
  declarations: [
    AppComponent,
    HomepageComponent,
    ProgressComponent,
    SubjectComponent,
    MainNavComponent,
    QuestionListComponent,
    QuizComponent,
    LoginComponent,
    SignupComponent,
    QuestionComponent,
    QuizCreatorComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    RouterModule,
    BrowserAnimationsModule,
    LayoutModule,
    MaterialModule,
    HttpClientModule,
    FlexLayoutModule,
    FormsModule
  ],
  schemas: [
    CUSTOM_ELEMENTS_SCHEMA
  ],
  providers: [AuthService, AuthGuard],
  bootstrap: [AppComponent]
})
export class AppModule { }
