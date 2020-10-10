import { SubjectComponent } from './views/subject/subject.component';
import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomepageComponent } from './views/homepage/homepage.component';
import { ProgressComponent } from './views/progress/progress.component';

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
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
