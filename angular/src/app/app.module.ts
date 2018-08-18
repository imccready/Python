import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http'; 

import { AppComponent } from './app.component';
import { ItemsService } from './specials/items.service';
import { ItemComponent } from './item/item.component';
import { SpecialsComponent } from './specials/specials.component';

@NgModule({
  declarations: [
    AppComponent,
    ItemComponent,
    SpecialsComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule
  ],
  providers: [ItemsService],
  bootstrap: [AppComponent]
})
export class AppModule { }
