import { AfterViewInit, Component, OnInit, ViewChild } from '@angular/core';
import { MatPaginator } from '@angular/material/paginator';
import { MatSort } from '@angular/material/sort';
import { merge, Observable, of } from 'rxjs';
import { catchError, map, startWith, switchMap } from 'rxjs/operators';
import { environment } from 'src/environments/environment';
import { FeedItem } from '../models';
import { FeedService } from '../services/feed.service';

@Component({
  selector: 'app-feed-page',
  templateUrl: './feed-page.component.html',
  styleUrls: ['./feed-page.component.scss'],
})
export class FeedPageComponent implements AfterViewInit, OnInit {
  displayedColumns: string[] = ['image', 'title', 'address', 'city'];

  resultsLength = 0;
  isLoadingResults = true;
  pageSize = environment.pageSize;

  feedItems!: Observable<FeedItem[]>;

  @ViewChild(MatPaginator) paginator!: MatPaginator;
  @ViewChild(MatSort) sort!: MatSort;

  constructor(private feedService: FeedService) {}

  ngOnInit(): void {}

  ngAfterViewInit(): void {
    this.feedItems = merge(this.sort.sortChange, this.paginator.page).pipe(
      startWith({}),
      switchMap(() => {
        this.isLoadingResults = true;
        return this.feedService.fetchFeedItems(
          this.sort.active,
          this.sort.direction,
          this.paginator.pageIndex
        );
      }),
      map((data) => {
        this.isLoadingResults = false;
        this.resultsLength = data.count;

        return data.results;
      }),
      catchError(() => {
        this.isLoadingResults = false;
        return of([]);
      })
    );
  }

  resetPaging(): void {
    this.paginator.pageIndex = 0;
  }
}
