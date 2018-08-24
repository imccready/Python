import { Component, OnInit } from '@angular/core';
import { SpecialsService } from './specials.service';
import { Item, Items } from '../item/item.model';

@Component({
  selector: 'app-specials',
  templateUrl: './specials.component.html',
  styleUrls: ['./specials.component.css']
})
export class SpecialsComponent implements OnInit {
	private items = []
	sum = 20;
  throttle = 100;
  scrollDistance = 1;
  scrollUpDistance = 2;
  direction = '';

  constructor(private specialsService: SpecialsService) { 
	}

	ngOnInit() {
		this.specialsService.getSpecials()
		.subscribe( (value: Item[]) => {
			this.items = this.items.concat(value)
		})

		this.specialsService.callApi()
	}


	onScrollDown (ev) {
		console.log('scrolled down!!', ev)
		this.specialsService.callApi()
  }

}
