import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-detail',
  templateUrl: './detail.component.html',
  styleUrls: ['./detail.component.css']
})
export class DetailComponent implements OnInit {

  constructor(
    public router:Router
  ) { }

  ngOnInit(): void {
  }
  book(){
    this.router.navigate(['book'])
  }
  back(){
    this.router.navigate(['dashboard'])
  }
}
