import newsapi
from newsapi import NewsApiClient
from newsapi.newsapi_exception import NewsAPIException


def create_newsapi_client(api_key: str):
    """
    Create a newsapi client
    """
    return NewsApiClient(api_key=api_key)


def query_articles(
        client: NewsApiClient,
        keywords: str,
        start_date: str,
        end_date: str) -> list():
    """
    Query NewsAPI for articles

    Args:
        - client: NewsAPI Client
        - keywords: string of keywords as specified by the API.
            Example: "corona OR covid OR coronavirus"
        - start_date: query start date. Example: "2017-01-01"
        - end_date: query end date. Example: "2017-01-05"

    Return:
        - articles: list of dictionaries containing article metadata.
        See newsapi docs for details
    """
    # initialize
    articles = []
    page = 1
    while True:
        try:
            page_results = client.get_everything(
                q=keywords,
                from_param=start_date,
                to=end_date,
                language='en',
                page=page)

        except NewsAPIException as e:
            print(e)
            break

        articles += page_results['articles']
        page += 1

    return articles
