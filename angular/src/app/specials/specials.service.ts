import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, Subject } from 'rxjs';
import { map, switchMap } from 'rxjs/operators';
import { Item, Items } from '../item/item.model';
import {API_URL} from '../env';


@Injectable({
  providedIn: 'root'
})
export class SpecialsService {

  lastCursor = undefined
  private getNext: Subject<string> = new Subject<string>()
	constructor(private http: HttpClient) { }



  public callApi() {
    this.getNext.next(this.lastCursor)
  }
  
	getSpecials(): Observable<Item[]> {
    return this.getNext.asObservable()
    .pipe( switchMap((value: any) => {

        return this.http.post<Items>(`${API_URL}`, value)
        .pipe(  map((value: Items): Item[] => {
          this.setCursor(value.cursor)
          return value.items
        }))

    }))
  }

  setCursor(cursor: string) {
    this.lastCursor ={ 
      'cursor' : cursor
    }
  }
}
