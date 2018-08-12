import { Component } from '@angular/core';
import { ItemsService } from './specials/items.service';
import { Items, Item } from './specials/item.model';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Specials';
  items: Item[] = []
  constructor(private itemService: ItemsService) {

  }

  ngOnInit() {
    this.itemService.getItems()
    .subscribe((items: Item[]) => {
      this.items = items
    })
  }

}
