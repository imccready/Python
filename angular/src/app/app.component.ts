import { Component } from '@angular/core';
import { ItemsService } from './specials/items.service';
import { Item } from './specials/item.model';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'angular';
  items: Item[]
  constructor(private itemService: ItemsService) {

  }

  ngOnInit() {
    this.itemService.getItems()
    .subscribe((items: Item[]) => {
      this.items = items
    }) 
  }

}
