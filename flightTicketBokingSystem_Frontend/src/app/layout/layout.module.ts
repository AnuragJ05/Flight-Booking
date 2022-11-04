import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { LayoutRoutingModule } from './layout-routing.module';
import { LayoutComponent } from './layout.component';
import { BookComponent } from './book/book.component';
import { RegisterComponent } from './register/register.component';
import { PaymentComponent } from './payment/payment.component';

@NgModule({
  declarations: [
    LayoutComponent
  ],
  imports: [
    CommonModule,
    LayoutRoutingModule
  ],
})
export class LayoutModule { }
