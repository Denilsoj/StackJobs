import requests 
from bs4 import BeautifulSoup as BS
from helpers import headers, url


response = requests.get(url, headers=headers)

page = BS(response.text, 'html.parser')
jobs_container = page.find('div', {'class': 'col-md-9'})
links_jobs = jobs_container.find_all('a', href=True)
urls_jobs = []
limit_urls = 15

for link in links_jobs:
    
    urls_jobs.append(link['href'])
    if len(urls_jobs) >= limit_urls:
        print('Urls coletadas')
        break
   

