import {Injectable} from '@angular/core';
import {HttpClient, HttpErrorResponse} from '@angular/common/http';
import { Observable } from 'rxjs';
import { Item } from '../item/item.model';
import {API_URL} from '../env';


@Injectable()
export class ItemsService {
    constructor(private http: HttpClient) {

    }
    private static _handleError(err: HttpErrorResponse | any) {
        return Observable.throw(err.message || 'Error: Unable to complete request.');
      }

    getItems(): Observable<Item[]> {
        /* let data = {"categoryId":"specialsgroup.1354","pageNumber":1,"pageSize":36,
        "sortType":"TraderRelevance",
        "url":"/shop/browse/specials/half-price",
        "location":"/shop/browse/specials/half-price",
        "formatObject":"{\"name\":\"Half Price\"}",
        "isSpecial":true,"isBundle":false,"isMobile":false,"filters":null}

        let results = this.http.post("https://www.woolworths.com.au/apis/ui/browse/category", data )

        console.log(results) */

        

        return this.http.get<Item[]>(`${API_URL}`)
    }

}