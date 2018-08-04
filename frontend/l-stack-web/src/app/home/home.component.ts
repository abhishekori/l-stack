import { Component, OnInit } from '@angular/core';
import { Breadcrumb } from '../models/breadcrumb';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  allBreadCrumbs: Breadcrumb[] = [];

  constructor() { }

  ngOnInit() {

    const temp: Breadcrumb = {
      path: '/detail',
      value: 'Details'
    }
    this.allBreadCrumbs.push(temp);
    this.allBreadCrumbs.push(temp);
    this.allBreadCrumbs.push(temp);
    this.allBreadCrumbs.push(temp);
    this.allBreadCrumbs.push(temp);

  }

}
