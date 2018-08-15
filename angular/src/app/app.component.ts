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
  items: any = undefined
  groups: Item[][] = undefined
  //items: any = undefined
  constructor(private itemService: ItemsService) {

  }

  ngOnInit() {
    this.itemService.getItems()
    .subscribe((itemz: Item[]) => {
      this.groups = _.chunk(itemz, 4)
      this.items = itemz
      console.log(this.items.length)
      console.log(this.items[0].length)
    })
  }

}
