import { Component, OnInit } from '@angular/core';
import { SpecialsService } from './specials.service';
import { Item } from '../item/item.model';

@Component({
  selector: 'app-specials',
  templateUrl: './specials.component.html',
  styleUrls: ['./specials.component.css']
})
export class SpecialsComponent implements OnInit {
  private items: any = undefined
  constructor(private specialsService: SpecialsService) { }

	ngOnInit() {
		this.specialsService.getSpecials()
		.subscribe((items: Item[]) => {
			this.items = items
		})
	}

}
