import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DashboardComponent } from '../layout/dashboard/dashboard.component';
import { RegisterComponent } from '../layout/register/register.component';
import { LoginComponent } from './login.component';

const routes: Routes = [
    {
        path: '',
        component: LoginComponent
    },
    {
        path:'dashboard',
        component:DashboardComponent
    },
    {
        path:'register',
        component:RegisterComponent
    }

];

@NgModule({
    imports: [RouterModule.forChild(routes)],
    exports: [RouterModule]
})
export class LoginRoutingModule {}
