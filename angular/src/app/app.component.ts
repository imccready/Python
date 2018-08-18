import { Component } from '@angular/core';
import { ItemsService } from './specials/items.service';
import { Item } from './item/item.model';
import { Observable } from 'rxjs';
import * as _ from "lodash";


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Specials';

  constructor(private itemService: ItemsService) {

  }

  ngOnInit() {
   
  }

}
