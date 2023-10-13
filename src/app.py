from links.states_urls import states_urls
from links.test_urls import test_urls
from dataset.data import create_data_set

from utils.filters import state_abbreviation_filter
from utils.maps import dataset_map
from utils.writer import write_csv
from utils.writer import write_sheets_map
from utils.writer import load_sheets_map
from utils.writer import sheets_exists
from utils.writer import get_sheets_file_name
from utils.requester import get_html
from utils.validator import dataset_validator

from pages.state_page import search_state_page
from pages.all_pages import serch_all_pages

class Scrappy:
  total_links = 0
  total_lines = 0
  successes = 0
  errors = 0
  test = False
  urls = []
  datasets = []

  def __init__(self, urls = None, test = False) -> None:
    if (urls):
      self.urls = urls
    else:
      if (test): self.urls = test_urls
      else: self.urls = states_urls
    self.test = test

  def run(self):
    if (self.test):
      pass
    else:
      sheets_map = load_sheets_map()
      for state_url in self.urls:
        # Tabela já foi escrita e está correta
        if (state_url in sheets_map and sheets_map[state_url] and sheets_exists(get_sheets_file_name(state_url))):
          continue
        try:
          dataset = create_data_set()
          state_page = get_html(state_url)
          search_state_page(state_page, dataset)
          abbreviation = state_abbreviation_filter(state_url)
          urls = dataset[dataset_map['urls']]
          urls = urls[1:]

          for url in urls:
            edp_html = get_html(url)
            edp_pages = edp_html.find_all('div', class_='page')
            serch_all_pages(edp_pages, dataset)
          
          result = dataset_validator(dataset)
          if (not result[0]):
            print(f'Dataset do inválido - Estado {abbreviation} de link {state_url}')
            print('Falharam as seguintes colunas: \n')
            for i in range(len(result[1])):
              print(f'Coluna: {result[1][i]} - Tamanho: {result[2][i]} - Esperado: {result[3]}')
            print('\nEscrita cancelada\n')
            continue

          result = write_csv(dataset, 'dados_' + abbreviation + '.csv')
          expected = len(dataset[dataset_map['urls']])
          sheets_map.update({state_url : result[0] == expected})
          write_sheets_map(sheets_map)
          if (result[0] != expected):
            print(f'Planilha inválida - Ao todo escreveu-se {result[0]} linhas')
            print(f"O esperado era {expected} linhas")
          print(f'Local de salvamento: {result[1]}')
          print()
          

          self.successes += 1
          self.total_lines += result[0]
        except ValueError as error:
          print(error.args)
          print('Erro ao acessar ')
          self.errors += 1
    print('Fim do programa')

  def summary():
    pass