from bs4 import BeautifulSoup
import requests

def fetch_linkedin_posts(profile_url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(profile_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    posts = []
    for tag in soup.find_all('span'):
        if tag.text.strip():
            posts.append(tag.text.strip())
    return posts[:3]
