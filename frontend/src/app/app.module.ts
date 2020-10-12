import { MaterialModule } from './material.module';
import { RouterModule } from '@angular/router';
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomepageComponent } from './views/homepage/homepage.component';
import { ProgressComponent } from './views/progress/progress.component';
import { SubjectComponent } from './views/subject/subject.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MainNavComponent } from './shared/main-nav/main-nav.component';
import { LayoutModule } from '@angular/cdk/layout';
import { QuestionListComponent } from './shared/question-list/question-list.component';
import { HttpClientModule } from '@angular/common/http'

@NgModule({
  declarations: [
    AppComponent,
    HomepageComponent,
    ProgressComponent,
    SubjectComponent,
    MainNavComponent,
    QuestionListComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    RouterModule,
    BrowserAnimationsModule,
    LayoutModule,
    MaterialModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
