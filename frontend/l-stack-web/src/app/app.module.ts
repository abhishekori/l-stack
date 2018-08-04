import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { MaterialModule } from './material/material.module';
import { FormsModule, ReactiveFormsModule } from '../../node_modules/@angular/forms';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { CommonModule } from '../../node_modules/@angular/common';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    MaterialModule,
    FormsModule,
    ReactiveFormsModule,
    BrowserAnimationsModule,
    CommonModule,
    
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
