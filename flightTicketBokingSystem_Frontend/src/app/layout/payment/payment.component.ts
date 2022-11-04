import { devOnlyGuardedExpression } from '@angular/compiler';
import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-payment',
  templateUrl: './payment.component.html',
  styleUrls: ['./payment.component.css']
})
export class PaymentComponent implements OnInit {

  constructor(public router:Router) { }

  ngOnInit(): void {
  }

  success(){
    alert('Booking Complete!!! ')  
    window.open('../../../assets/171515_TicketBked.pdf');
  }
  back(){
    this.router.navigate(['book'])
  }
}
