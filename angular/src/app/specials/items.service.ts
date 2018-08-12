import {Injectable} from '@angular/core';
import {HttpClient, HttpErrorResponse} from '@angular/common/http';
import { Observable } from 'rxjs';
import { Item } from './item.model';
import {API_URL} from '../env';


@Injectable()
export class ItemsService {
    constructor(private http: HttpClient) {

    }
    private static _handleError(err: HttpErrorResponse | any) {
        return Observable.throw(err.message || 'Error: Unable to complete request.');
      }

    getItems(): Observable<Item[]> {
        return this.http.get<Item[]>(`${API_URL}`)
    }

}