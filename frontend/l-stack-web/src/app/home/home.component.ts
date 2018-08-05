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

  allBreadCrumbs = [];
  searchQuery: String;
  info: String;
  tags = [];
  macSetup;
  winSetup;
  linuxSetup;
  helloWorld;
  suggestions = [];

  isLoading = true;


  constructor(private http: HttpClient) { }

  ngOnInit() {

    // const temp: Breadcrumb = {
    //   path: '/detail',
    //   value: 'Details'
    // }
    // this.allBreadCrumbs.push(temp);
    // this.allBreadCrumbs.push(temp);
    // this.allBreadCrumbs.push(temp);
    // this.allBreadCrumbs.push(temp);
    // this.allBreadCrumbs.push(temp);

  }

  submitQuery() {
    this.isLoading = true;
    console.log(this.searchQuery);
    return this.http.get(`http://192.168.43.191:5000/summary?q=${this.searchQuery}`).subscribe(res => {
      console.log(res);
      this.info = res['info'];
      // clear the array once
      this.tags = [];
      const tempArray = res['tags'];
      // check if we already visited the tag 
      tempArray.forEach(element => {
        if (!this.allBreadCrumbs.includes(element)) {
          this.tags.push(element);
        }
      });
      const setup = res['setup'];
      this.macSetup = setup[1]['mac'][0];
      this.winSetup = setup[0]['windows'][0];
      this.linuxSetup = setup[2]['linux'][0];
      this.helloWorld = res['helloworlds'][0];
      this.suggestions = res['suggestions'];
      this.isLoading = false;
      this.allBreadCrumbs.push(this.searchQuery);
    });

  }

  reloadFor(tag) {
    console.log('searching for ', tag);
    this.isLoading = true;
    this.searchQuery = tag;
    return this.http.get(`http://192.168.43.191:5000/summary?q=${tag}`).subscribe(res => {
      console.log(res);
      this.info = res['info'];
      this.tags = [];
      const tempArray = res['tags'];
      // check if we already visited the tag 
      tempArray.forEach(element => {
        if (!this.allBreadCrumbs.includes(element)) {
          this.tags.push(element);
        }
      });
      const setup = res['setup'];
      this.macSetup = setup[1]['mac'][0];
      this.winSetup = setup[0]['windows'][0];
      this.linuxSetup = setup[2]['linux'][0];
      this.helloWorld = res['helloworlds'][0];
      this.suggestions = res['suggestions'];
      this.isLoading = false;
      this.allBreadCrumbs.push(tag);
    });
  }

}
