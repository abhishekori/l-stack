import { Component, OnInit } from '@angular/core';
import { Breadcrumb } from '../models/breadcrumb';
import { HttpClient } from '../../../node_modules/@angular/common/http';
import { tap, map } from 'rxjs/operators';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  allBreadCrumbs: Breadcrumb[] = [];
  searchQuery: String;
  info: String;
  tags = [];
  macSetup ;
  winSetup;
  linuxSetup;


  constructor(private http: HttpClient) { }

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

  submitQuery() {
    console.log(this.searchQuery);
    return this.http.get(`http://localhost:5000/summary?q=${this.searchQuery}`).subscribe(res => {
      console.log(res);
      this.info = res['info'];
      this.tags = res['tags'];
      const setup = res['setup'];
      this.macSetup = setup[1]['mac'][0];
      this.winSetup = setup[0]['windows'][0];
      this.linuxSetup = setup[2]['linux'][0];
    })

  }

}
