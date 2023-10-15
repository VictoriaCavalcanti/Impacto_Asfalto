from time import time
from datetime import datetime

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
  start_time = time()
  end_time = 0

  invalid_dataset_urls = [] # Urls com datasets inválidos
  valid_dataset_urls = [] # Urls com datasets válidos
  sheets_sizes = [] # Tamanhos das tabelas escritas
  sheets_writed_success = 0 # Quantidade de tabelas corretamente escritas
  sheets_writed_count = 0 # Quantidade de tabelas escritas

  urls = [] # Lista de todas urls
  invalid_urls = [] # Lista com urls inválidas -> Nem chega a montar o dataset
  valid_urls = [] # Lista com urls válidas
  links_sucesses_writed = 0 # Quantidade de links escritos corretamente
  links_errors_writed = 0 # Quantidade de links não escritos ou incorretos
  total_links = 0 # Quantidade total de links percorridos

  lines_writed = 0 # Linhas escritas (total)
  lines_sucess = 0 # Linhas escritas corretamente
  lines_erros = 0 # Linhas escritas incorretamente

  run_times = 0
  successes = 0 # Sucesso -> Apenas conseguiu rodar
  errors = 0 # Error -> Não conseguiu rodar

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
        self.urls = urls[1:]

        for url in self.urls:
          edp_html = get_html(url)
          edp_pages = edp_html.find_all('div', class_='page')
          serch_all_pages(edp_pages, dataset)
        
        result = dataset_validator(dataset)
        if (not result[0]):
          print_dataset_error(abbreviation, state_url, result)
          self.lines_errors += result[3] # Linhas que deixaram de serem escritas
          self.invalid_dataset_urls.append(state_url)
          self.links_errors_writed += len(urls) - 1
          self.errors += 1
          continue

        result = write_csv(dataset, 'dados_' + abbreviation + '.csv')
        expected = len(dataset[dataset_map['urls']])
        status = result[0] == expected
        sheets_map.update({state_url : status})
        write_sheets_map(sheets_map)

        if (status):
          self.sheets_writed_success += 1
          self.valid_dataset_urls.append(state_url)
          self.lines_sucess += result[0]
          self.links_sucesses_writed += result[0] - 1
        else:
          self.links_errors_writed += result[0] - 1

        print_sheet_status(expected, result)

        self.lines_writed += result[0] - 1
        self.sheets_writed_count += 1
        self.sheets_sizes.append(result[0])
        self.valid_urls.append(state_url)

        self.total_links += len(urls) - 1
        self.successes += 1

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

    self.end_time = time()
    self.summary()
    print('Fim do programa')

  def summary(self):
    print('\n========================== Resumo do Programa =============================\n')
    print(f'Data de execução: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
    print(f'Tempo de execução do programa: {round(self.end_time - self.start_time, 2)} s\n')

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

    print(f'Quantidade total de linhas escritas: {self.lines_writed}')
    print(f'Quantidade de planilhas escritas: {self.sheets_writed_count}')
    print(f'Quantidade de planilhas escritas corretamente: {self.sheets_writed_success}')
    print(f'Taxa de acerto das planilhas: {round((self.sheets_writed_success / self.sheets_writed_count) * 100, 2)} %')
    # print(f'Tamanho das planilhas: ')
    # for i in range(len(self.sheets_sizes)):
    #   print(f'Planilha de {self.valid_urls[i]} - Tamanho {self.sheets_sizes[i]}')
    print()

    total_data_amount = self.total_links * len(dataset_map)
    total_data_writed = self.lines_writed * len(dataset_map)
    total_success_data_amount = self.lines_sucess * len(dataset_map)
    total_error_data_amount = self.lines_erros * len(dataset_map)
    print(f'Quantidade total de dados procurados: {total_data_amount}')
    print(f'Quantidade total de dados escritos: {total_data_writed}')
    print(f'Quantidade total de dados não escritos: {total_data_amount - total_data_writed}')
    print(f'Quantidade total de dados escritos corretamente: {total_success_data_amount}')
    print(f'Quantidade total de dados escritos incorretamente: {total_error_data_amount}')
    print(f'Taxa de acerto dos dados: {round((total_success_data_amount - total_error_data_amount) / total_data_writed, 2) * 100} %')
    print('\n===================================================================================\n')
    