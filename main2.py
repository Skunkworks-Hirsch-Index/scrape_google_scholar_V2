from google_scholar_py import CustomGoogleScholarProfiles, CustomGoogleScholarOrganic, CustomGoogleScholarAuthor
from google_scholar_py.serpapi_backend.author_results import SerpApiGoogleScholarAuthor

parser = CustomGoogleScholarAuthor()
data = parser.scrape_google_scholar_author_data(user_id='nHhtvqkAAAAJ', parse_articles=True,article_pagination=True)

print(json.dumps(data, indent=2))
        
print(data['info']) # author info
print(data['co-authors'])

for article in data['articles']:
    print(article['title'])
            print(article['cited_by_count'])