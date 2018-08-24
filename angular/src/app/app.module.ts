import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http'; 

import { AppComponent } from './app.component';
import { ItemsService } from './specials/items.service';
import { ItemComponent } from './item/item.component';
import { SpecialsComponent } from './specials/specials.component';
import { InfiniteScrollModule } from 'ngx-infinite-scroll';
import { NavbarComponent } from './navbar/navbar.component';
import { LayoutComponent } from './ui/layout/layout.component';
import { HeaderComponent } from './ui/header/header.component';
import { FooterComponent } from './ui/footer/footer.component';


@NgModule({
  declarations: [
    AppComponent,
    ItemComponent,
    SpecialsComponent,
    NavbarComponent,
    LayoutComponent,
    HeaderComponent,
    FooterComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    InfiniteScrollModule
  ],
  providers: [ItemsService],
  bootstrap: [AppComponent]
})
export class AppModule { }
