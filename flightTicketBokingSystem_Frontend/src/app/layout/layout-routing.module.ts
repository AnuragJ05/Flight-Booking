import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LayoutComponent } from './layout.component';

const routes: Routes = [
    {
        path: '',
        component: LayoutComponent,
        children: [
            { path: '', redirectTo: 'dashboard', pathMatch: 'prefix' },
            {
                path: '',
                loadChildren: () => import('./dashboard/dashboard.module').then((m) => m.DashboardModule)
            },
            {
                path: 'details',
                loadChildren: () => import('./detail/detail.module').then((m) => m.DetailModule)
            },
            {
                path: 'book',
                loadChildren: () => import('./book/book.module').then((m) => m.BookModule)
            },
            {
                path: 'register',
                loadChildren: () => import('./register/register.module').then((m) => m.RegisterModule)
            },
            {
                path: 'payment',
                loadChildren: () => import('./payment/payment.module').then((m) => m.PaymentModule)
            }
        ]
    }
];

@NgModule({
    imports: [RouterModule.forChild(routes)],
    exports: [RouterModule]
})
export class LayoutRoutingModule {}