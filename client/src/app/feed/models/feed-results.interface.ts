import { DrfApi } from './drf-api.interface';
import { FeedItem } from './feed.interface';

export interface FeedApiResult extends DrfApi {
  results: FeedItem[];
}
