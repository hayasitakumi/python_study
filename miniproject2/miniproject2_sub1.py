import time
import requests
from bs4 import BeautifulSoup
import pprint

def get_keywords(url):
  time.sleep(0.1)
  r = requests.get(url)
  soup = BeautifulSoup(r.content, 'lxml')
  keywords_csv = soup.find('meta', attrs={'name': 'keywords'}).get('content')
#  print(keywords_csv.split(','))
  return keywords_csv.split(',')

def get_dept():
  url = 'https://kitnet.jp/laboratories/'
  r = requests.get(url)
  soup = BeautifulSoup(r.content, 'lxml')
  sections = soup.find_all('p',class_='title')
  
  # for section in sections:
  #   print(section.text)

  table = soup.find_all('div',class_='homeLaboSection')
#  pprint.pprint(table)
  subjects = table[0].find_all('div',class_='laboList')
  
  link_list = []
  for subject in subjects:
    link_list.append(subject.find_all('a'))

  lab_list = []
  url_list = []
  #pprint.pprint(links)
  for links in link_list:
    labs = []
    url_labs = []
    for link in links:
      if link.has_attr('href') and link['href']:
        url_labs.append(url + link['href'])
        labs.append(link.text)

    url_list.append(url_labs)  
    lab_list.append(labs)

  # for section in sections:
  #   print(section.text)
#  pprint.pprint(url_list)
#  pprint.pprint(lab_list)

  # for url_lab in url_labs:
  #   print(url_lab)

  return sections,lab_list,url_list

def scrape_labs():
  sections,lab_list,url_list = get_dept()
  # for section in sections:
  #   print(section.text)
  #pprint.pprint(url_list)
  #pprint.pprint(lab_list)
  
  lab_in_depts = []
  for i,urls in enumerate(url_list):
    lab_in_dept = []
    labs = lab_list[i]
    for j,url in enumerate(urls):
      dict_keyword = {}
      dict_keyword['keywords'] = get_keywords(url)
      dict_keyword['lab'] = labs[j]
      lab_in_dept.append(dict_keyword)

    lab_in_depts.append(lab_in_dept)
  print(lab_in_depts)
  lists = []
  for i,section in enumerate(sections):
    dict_dept = {}
    dict_dept['dept'] = section.text
    dict_dept['labs'] = lab_in_depts[i]
    lists.append(dict_dept)

  for list in lists:
    print(list)

  #pprint.pprint(list)
#   lists = []

#   keywords = []
  
#   for url in urls:
#     keywords.append(get_keywords(url))
  
#   dict_labs = {}
#   dict['keywords'] = 

#   for section in sections:
#     dict = {}
#     dict = {'dept': section.text,'labs'}
#     lists.append(dict)
    
  # for list in lists:
  #   print(list)
  
  # for keyword in keywords:
  #   print(keyword)

# def serch_labs():

  
if __name__ == "__main__":
#  get_keywords('https://kitnet.jp/laboratories/labo0001/index.html')
#  get_dept()
   scrape_labs()