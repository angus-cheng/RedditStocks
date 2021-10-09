import requests
import pandas as pd

base_url = 'https://api.pushshift.io/reddit/search'

# Search parameters
data_type='comment'
query="python"
duration='30d' # Epoch or Integer + s/m/h/d
size=100
sort_type='score' # Sort by 'score', 'num_comments', 'created_utc'
sort='desc'
# aggs='subreddit' # Contains 'author', 'link_id', 'created_utc', 'subreddit'
# aggs = grouping


def search(data_type, **kwargs):
    endpoint = f'{base_url}/{data_type}/'
    payload = kwargs
    resp = requests.get(endpoint, params=payload)
    resp.raise_for_status()
    print(resp.url)

    return resp.json()['data']


def main():

    resp = search(data_type=data_type,
        q=query,
        after=duration,
        size=size)

    # Get each subreddit that appears in the search
#     data = resp.get('aggs').get(aggs)


if __name__ == "__main__":
    main()