import os
import csv
import json
from utils.filters import state_abbreviation_filter

## Função que escreve os csv
def write_csv(data_set, file_name):
  # Calcula a transposta da matriz
  dados_transpostos = list(map(list, zip(*data_set)))
  current_path = os.path.abspath(os.path.dirname(__file__))
  save_path = os.path.abspath(os.path.join(current_path, '../../sheets', file_name))

  # Escrever os dados transpostos no arquivo CSV
  with open(save_path, 'w', newline='') as arquivo_csv:
      escritor = csv.writer(arquivo_csv)
      escritor.writerows(dados_transpostos)

  print(f'Dados transpostos foram escritos no arquivo {file_name}')
  print(f'Ao todo escreveu-se {len(dados_transpostos)} linhas')
  return (len(dados_transpostos), save_path)

def write_sheets_map(sheets_map):
  current_path = os.path.abspath(os.path.dirname(__file__))
  save_path = os.path.abspath(os.path.join(current_path, '../../saves', 'sheets_map.json'))
  with open(save_path, "w") as arquivo_json:
    json.dump(sheets_map, arquivo_json)

  print(f'Dicionário foi escrito em {save_path}')

def load_sheets_map():
  # Nome do arquivo JSON a ser lido
  current_path = os.path.abspath(os.path.dirname(__file__))
  save_path = os.path.abspath(os.path.join(current_path, '../../saves', 'sheets_map.json'))

  try:
    # Ler o arquivo JSON e criar um dicionário
    with open(save_path, "r") as arquivo_json:
        sheets_map = json.load(arquivo_json)
        print("Dicionário lido do arquivo JSON:")
        print(sheets_map)
        print()
        return sheets_map
  except FileNotFoundError:
     print('Não há dicionário salvo')
     write_sheets_map({})
     return {}

def sheets_exists(sheets_filename):
   current_path = os.path.abspath(os.path.dirname(__file__))
   sheets_path = os.path.abspath(os.path.join(current_path, '../../sheets', sheets_filename))
   return os.path.exists(sheets_path)

def get_sheets_file_name(state_url):
   abbreviation = state_abbreviation_filter(state_url)
   return 'dados_' + abbreviation + '.csv'