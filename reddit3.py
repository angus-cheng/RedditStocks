import requests
import pandas as pd

base_url = 'https://api.pushshift.io/reddit/search/submission'

size = 500
duration = '1d'


def get_today_submissions(query, subreddit):
    params = {'title': query,
              'subreddit': subreddit, 
              'size': size, 
              'after': duration}
    resp = requests.get(base_url, params=params)
    print(resp.url)
    return resp.json()['data']


def main():
    submissions = get_today_submissions('gme', 'wallstreetbets')
    df = pd.DataFrame(submissions)
    df.apply(pd.Series)
    print(df.head())
    print(df.columns)
    print(df['full_link'])


if __name__ == "__main__":
    main()