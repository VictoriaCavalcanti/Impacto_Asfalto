import requests
from bs4 import BeautifulSoup

def get_html(url):
  response = requests.get(url)
  if response.status_code == 200:
      soup = BeautifulSoup(response.text, 'html.parser')
      return soup
  else:
    raise ValueError('BAD URL', url)
