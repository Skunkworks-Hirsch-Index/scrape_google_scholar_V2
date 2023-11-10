from google_scholar_py import CustomGoogleScholarProfiles, CustomGoogleScholarOrganic, CustomGoogleScholarAuthor
from google_scholar_py.serpapi_backend.author_results import SerpApiGoogleScholarAuthor
from google_scholar_py.custom_backend.author_info_all_articles import h_index_without_coauthor,h_index_without_time_period
import json 

def scrape_publications():
    parser = CustomGoogleScholarOrganic()
    data = parser.scrape_google_scholar_organic_results(
        query='Dane Morgan',
        pagination=False,
        save_to_csv=False,
        save_to_json=False
    )
    print(json.dumps(data, indent=2))

def scrape_author(user_id):
    parser = CustomGoogleScholarAuthor()
    data = parser.scrape_google_scholar_author_data(
        user_id=user_id,
        parse_articles=True,
        article_pagination=True
    )
    return data

def scrape_article(link, name, citations_count):
    parser = CustomGoogleScholarAuthor()
    data = parser.scrape_google_scholar_article_data(
        link=link,
        name=name, 
        citations_count=citations_count
    )
    return data
def scrape_author_articles(user_id):
    data = {
        'info': {},
        'articles': []
    }

    parser = CustomGoogleScholarAuthor()
    author_data = parser.scrape_google_scholar_author_data(
        user_id=user_id,
        parse_articles=True,
        article_pagination=True
    )
    name = author_data['info']['name']
    data['info']['name'] = name
    data['info']['h_index'] = author_data['info']['h_index']
    for article in author_data['articles']:
        if article['link'] != None:
            article_data = scrape_article(article['link'], name=name, citations_count=article['cited_by_count'])
            data['articles'].append(article_data)
    return data

if __name__ == '__main__':
    parser = CustomGoogleScholarAuthor()
    # data = parser.scrape_google_scholar_author_data(user_id='Q6m4TzIAAAAJ', parse_articles=True, article_pagination=True)
    data = scrape_author_articles('Q6m4TzIAAAAJ')
    # Using the helper functions
    co_author_name = "Robert Kudrawiec"
    start_year, end_year = 2010, 2020
    print(f"H-Index without {co_author_name}: {h_index_without_coauthor(data['articles'], co_author_name)}")
    print(f"H-Index without papers from {start_year} to {end_year}: {h_index_without_time_period(data['articles'], start_year, end_year)}")

    with open("data/MaciejPolakArticles.json", "w") as f:
        json.dump(data, f, indent=2)