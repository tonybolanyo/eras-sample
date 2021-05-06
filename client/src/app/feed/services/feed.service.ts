import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';
import { FeedApiResult } from '../models/feed-results.interface';

@Injectable({
  providedIn: 'root',
})
export class FeedService {
  constructor(private http: HttpClient) {}

  fetchFeedItems(
    sort: string = '',
    order: string = '',
    page: number = 0,
    search: string = ''
  ): Observable<FeedApiResult> {
    const url = `${environment.apiUrl}/feed/`;
    let params = new HttpParams();
    params = params.append('page', `${page + 1}`);
    params = params.append('page_size', `${environment.pageSize}`);
    params = params.append(
      'ordering',
      order === 'desc' ? `-${sort}` : `${sort}`
    );
    return this.http.get<FeedApiResult>(url, { params });
  }
}
