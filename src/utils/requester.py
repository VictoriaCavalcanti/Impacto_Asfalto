import requests
from bs4 import BeautifulSoup

def get_html(url):
  response = requests.get(url)
  if response.status_code == 200:
      soup = BeautifulSoup(response.text, 'html.parser')
      return soup
  else:
    raise ValueError('BAD URL', url)

def get_all_states_urls():
  urls = []
  prefix = 'https://asphaltepd.org'
  page = get_html('https://asphaltepd.org/published/')
  data_table = page.find('table', id='data-table')
  links = data_table.find_all('a')

  for link in links:
      urls.append(prefix + link.get('href'))
      
  return urls