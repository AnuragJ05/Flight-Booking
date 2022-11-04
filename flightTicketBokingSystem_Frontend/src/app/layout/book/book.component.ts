import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-book',
  templateUrl: './book.component.html',
  styleUrls: ['./book.component.css']
})
export class BookComponent implements OnInit {

  constructor(public router:Router) { }

  ngOnInit(): void {
  }
  add(){
    alert('Added Passenger list!!!')
  }
  back(){
    this.router.navigate(['details'])
  }
  pay(){
    this.router.navigate(['payment'])
  }
}
