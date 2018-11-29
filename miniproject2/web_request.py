import requests
from bs4 import BeautifulSoup
import pprint

def web_request():
  r = requests.get('https://mars15.mars.kanazawa-it.ac.jp/waiting_room/public')
  
  # parser に 'lxml' を指定してもうまくいかなかったので、'html5lib' を使用した。
  # 文字コードは UTF-8 ではなくシフトJISで、ヘッダーの charset でも記述されていなかったので、
  # 明示的に指定する必要があった。
  soup = BeautifulSoup(r.content, 'html5lib', from_encoding='shift_jis')
  
  tables = soup.find_all('table', class_='default')
  records = tables[1].find_all('tr')
  teachers = []
  for record in records:
      cells = record.find_all('td')
      if cells:
          name = cells[0].text
          start, end = cells[3].text.split('〜')
          teachers.append((name, start, end))
  
  for name, start, end in teachers:
      print('{}:\t{} - {}'.format(name, start, end))

def web_le():
  from bs4 import BeautifulSoup

  r = requests.get('https://en.wikipedia.org/wiki/HTTP_301')
  soup = BeautifulSoup(r.content, 'lxml')
  sections = soup.find_all('span', class_='mw-headline')

  links = soup.find_all('a')
  for link in links:
      if link.has_attr('href') and link['href'].startswith('http'):
          print(link['href'])
if __name__ == "__main__":
  web_le()