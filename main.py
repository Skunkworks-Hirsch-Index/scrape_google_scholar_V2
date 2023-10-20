from google_scholar_py import CustomGoogleScholarProfiles, CustomGoogleScholarOrganic, CustomGoogleScholarAuthor
from google_scholar_py.serpapi_backend.author_results import SerpApiGoogleScholarAuthor

import json

# def scrape_profiles():
#     parser = CustomGoogleScholarProfiles()
#     data = parser.scrape_google_scholar_profiles(
#         query='University of Wisconsin',
#         pagination=False,
#         save_to_csv=False,
#         save_to_json=False
#     )
#     print(json.dumps(data, indent=2))

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



# def serp_scrape_author():

#     parser = SerpApiGoogleScholarAuthor()
#     data = parser.scrape_google_scholar_author_results(
#         author_id='Q6m4TzIAAAAJ',
#         api_key='2b0f2e80c02509a0028e51b98f584f280236e564a61888acb21e8068df98129f',
#         parse_articles=False,
#         article_pagination=False,
#     )
    
#     #print(data.keys()) # show available keys
#     with open("data/SerpMaciejPolak.json", "w") as f:
#         json.dump(data, f, indent=2)

if __name__ == '__main__':
    #serp_scrape_author()
    #data = scrape_article('https://scholar.google.com/citations?view_op=view_citation&hl=en&user=DYmXzOYAAAAJ&citation_for_view=DYmXzOYAAAAJ:d1gkVwhDpl0C')
    #print(data)
    data = scrape_author_articles('Q6m4TzIAAAAJ')
    with open("data/MaciejPolakArticles.json", "w") as f:
        json.dump(data, f, indent=2)

    # data = scrape_author_articles('DYmXzOYAAAAJ')
    # with open("data/McCartyArticles.json", "w") as f:
    #     json.dump(data, f, indent=2)
