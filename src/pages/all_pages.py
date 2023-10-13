from pages.page1 import search_page_one
from pages.page2 import search_page_two
from pages.page5 import search_page_five
from pages.page6 import search_page_six

def serch_all_pages(pages, dataset):
  for page in pages:
    if (page['id'] == 'p1'):
        search_page_one(page, dataset)
    if (page['id'] == 'p2'):
        search_page_two(page, dataset)
    if (page['id'] == 'p5'):
        search_page_five(page, dataset)
    if (page['id'] == 'p6'):
        search_page_six(page, dataset)