import requests
import pprint
def web():
  from bs4 import BeautifulSoup

  r = requests.get('https://en.wikipedia.org/wiki/HTTP_301')
  soup = BeautifulSoup(r.content, 'lxml')
  sections = soup.find_all('span', class_='mw-headline')

  pprint.pprint(sections)