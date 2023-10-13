from links.test_urls import test_urls
from dataset.data import create_data_set
from utils.filters import state_abbreviation_filter
from utils.maps import dataset_map
from utils.writer import write_csv
from utils.writer import write_sheets_map
from utils.writer import load_sheets_map
from utils.writer import sheets_exists
from utils.writer import get_sheets_file_name
from utils.requester import get_all_states_urls
from utils.requester import get_html
from utils.validator import dataset_validator
from utils.printer import print_sheet_status
from utils.printer import print_dataset_error
from pages.state_page import search_state_page
from pages.all_pages import serch_all_pages

class Scrappy:
  test = False
  force_write_sheets = False

  sheets_sizes = []
  urls = []
  invalid_dataset_urls = []
  invalid_urls = []
  valid_urls = []

  sheets_writed_success = 0
  sheets_writed_count = 0
  links_sucess = 0
  lines_sucess = 0
  total_links = 0
  total_lines = 0
  run_times = 0
  successes = 0
  errors = 0

  def __init__(self, urls = [], test = False, force_write_sheets = False) -> None:
    self.urls = urls
    self.test = test
    self.force_write_sheets = force_write_sheets

  def run_all_links(self):
    sheets_map = load_sheets_map()
    states_urls = get_all_states_urls()
    for state_url in states_urls:
      sheets_condition = state_url in sheets_map and sheets_map[state_url] and sheets_exists(get_sheets_file_name(state_url))
      if (not self.force_write_sheets and sheets_condition):
        continue
      
      self.run_times += 1
      try:
        dataset = create_data_set()
        state_page = get_html(state_url)
        search_state_page(state_page, dataset)
        abbreviation = state_abbreviation_filter(state_url)
        urls = dataset[dataset_map['urls']]

        for url in urls[1:]:
          edp_html = get_html(url)
          edp_pages = edp_html.find_all('div', class_='page')
          serch_all_pages(edp_pages, dataset)
        
        result = dataset_validator(dataset)
        if (not result[0]):
          print_dataset_error(abbreviation, state_url, result)
          self.invalid_dataset_urls.append(state_url)
          self.errors += 1
          continue

        result = write_csv(dataset, 'dados_' + abbreviation + '.csv')
        expected = len(dataset[dataset_map['urls']])
        status = result[0] == expected
        sheets_map.update({state_url : status})
        write_sheets_map(sheets_map)

        if (status): self.sheets_writed_success += 1
        print_sheet_status(expected, result)

        self.successes += 1
        self.sheets_sizes.append(result[0])
        self.sheets_writed_count += 1
        self.lines_sucess += result[0]
        self.total_lines += expected
        self.total_links += expected - 1
        self.valid_urls.append(state_url)

      except ValueError as error:
        print(f'Erro ao executar scrappy em {state_url}')
        self.errors += 1
        self.invalid_urls.append(state_url)

  def run(self):
    if (self.test):
      pass
    elif (self.urls):
      pass
    else:
      self.run_all_links()

    self.summary()
    print('Fim do programa')

  def summary(self):
    print('\n========================== Resumo do Programa =============================\n')
    print(f'Quantidade total de tentativas: {self.run_times}')
    print(f'Tentativas sucedidas: {self.successes}')
    print(f'Tentativas com erro: {self.errors}')
    print(f'Taxa de acerto da execução: {round((self.successes / self.run_times) * 100, 2)} %\n')

    print(f'Quantidade total de links: {self.total_links}')
    print(f'Quantidade de links com erros: {len(self.invalid_urls)}')
    print(f'Taxa de acerto dos links: {round(((self.total_links - len(self.invalid_urls) ) / self.total_links) * 100, 2)} %')
    if (len(self.invalid_urls)):
      print('Lista de urls inválidas: ')
      for invalid in self.invalid_urls:
        print(invalid)
    print()

    print(f'Quantidade total de linhas escritas: {self.total_lines}')
    print(f'Quantidade de planilhas escritas: {self.sheets_writed_count}')
    print(f'Quantidade de planilhas escritas corretamente: {self.sheets_writed_success}')
    print(f'Taxa de acerto das planilhas: {round((self.sheets_writed_success / self.sheets_writed_count) * 100, 2)} %')
    print(f'Tamanho das planilhas: ')
    for i in range(len(self.sheets_sizes)):
      print(f'Planilha de {self.valid_urls[i]} - Tamanho {self.sheets_sizes[i]}')
    print()
    