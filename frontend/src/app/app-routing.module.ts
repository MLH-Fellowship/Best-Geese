import { SignupComponent } from './views/signup/signup.component';
import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomepageComponent } from './views/homepage/homepage.component';
import { ProgressComponent } from './views/progress/progress.component';
import { SubjectComponent } from './views/subject/subject.component';
import { LoginComponent } from './views/login/login.component';
// import { MainNavComponent } from './shared/main-nav';

const routes: Routes = [
  {
    component: HomepageComponent,
    path: 'index',
    pathMatch: 'full'
  },
  {
    redirectTo: 'index',
    path: '',
    pathMatch: 'full'
  },
  {
    component: SubjectComponent,
    path: 'subjects'
  },
  {
    component: ProgressComponent,
    path: 'progress'
  },
  {
    component: LoginComponent,
    path: 'login'
  },
  {
    component: SignupComponent,
    path: 'signup'
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
