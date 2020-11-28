from requests import get

from bs4 import BeautifulSoup
import pandas as pd

def get_top_subreddits():
    """ pulls top 10 subreddits by recent activity by scraping redditlist.com """
    url = "http://redditlist.com/sfw"
    response = get(url)
    html_soup = BeautifulSoup(response.text, "html.parser")
    rank_containers = html_soup.find("div", class_="span4 listing").findChildren(
        "span", class_="subreddit-url", limit=125
    )
    top_subreddits = [tag.get_text().strip() for tag in rank_containers]
    pd.DataFrame(top_subreddits).to_csv('/task_data/top_subreddits/top_subreddits.csv', index=False)
    return top_subreddits

if __name__ == "__main__":
    print(get_top_subreddits())