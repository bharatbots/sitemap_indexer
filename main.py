import requests
import httplib2

from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from bs4 import BeautifulSoup


SCOPES = ["https://www.googleapis.com/auth/indexing"]
ENDPOINT = 'https://indexing.googleapis.com/batch'

JSON_KEY_FILE = "worker_oath.json"

creds = Credentials.from_service_account_file(JSON_KEY_FILE, scopes=SCOPES)
service = build('indexing', 'v3', credentials=creds)

with open('indexed_urls.txt', 'r') as f:
    indexed_urls = f.read().splitlines()


new_published = []


def callback(request_id, response, exception):
    if exception:
        print(exception)
    else:
        url = response['urlNotificationMetadata']['url']

        if url not in indexed_urls:

            with open("indexed_urls.txt", "a") as myfile:

                myfile.write(url + "\n")
                new_published.append(url)


def get_urls_from_sitemap(url: str):
    sitemap = requests.get(url, timeout=10)
    soup = BeautifulSoup(sitemap.content, features='xml')

    urls = [loc.text.strip() for loc in soup.find_all('loc')]

    return list(set(urls))


sitemap_urls = get_urls_from_sitemap(config.sitemap_url)

batch = service.new_batch_http_request(callback=callback)

for sitemap_url in sitemap_urls:
    if sitemap_url not in indexed_urls:
        batch.add(service.urlNotifications().publish(
            body={
                "url": sitemap_url.strip(),
                "type": "URL_UPDATED",
            }
        ))
        
        
batch.execute(http=httplib2.Http())
print(f"Published {len(new_published)} new urls")
