import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Item } from '../item/item.model';
import {API_URL} from '../env';


@Injectable({
  providedIn: 'root'
})
export class SpecialsService {

	constructor(private http: HttpClient) { }

	getSpecials(): Observable<Item[]> {
		return this.http.get<Item[]>(`${API_URL}`)
  }
}
