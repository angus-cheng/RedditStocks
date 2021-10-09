import requests
import time
import pandas as pd

base_url = 'https://api.pushshift.io/reddit/search/submission'


def get_posts(subreddit):
    params = {'subreddit': subreddit}
    submissions = requests.get(base_url, params=params)

    return submissions.json()


def get_last_post(subreddit):
    submissions = get_posts(subreddit)
    last_submission_time = submissions['data'][-1]['created_utc']
    params = {'subreddit': subreddit, 'before': last_submission_time}

    return requests.get(base_url, params=params)


def crawl_page(subreddit: str, last_page=None):
    params = {'subreddit': subreddit, 'size': 50, 'sort': 'desc',
              'sort_type': 'created_utc'}
    if last_page is not None:
        if len(last_page) > 0:
            params['before'] = last_page[-1]['created_utc']
        else:
            return []
    results = requests.get(base_url, params)
    if not results.ok:
        raise Exception(f'Server returned status code {results.status_code}')
    return results.json()['data']


def crawl_subreddit(subreddit, max_submissions=2000):
    submissions = []
    last_page = None
    while last_page != [] and len(submissions) < max_submissions:
        last_page = crawl_page(subreddit, last_page)
        submissions += last_page
        time.sleep(3)    

    return submissions[:max_submissions]


def main():
    # posts = get_posts('science')
    page = crawl_subreddit('wallstreetbets')
    print(page)


if __name__ == "__main__":
    main()