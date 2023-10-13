def print_dataset_error(abbreviation: bool, state_url: str, result: tuple[int, list, list, int]):
  print(f'Dataset inválido - Estado {abbreviation} - Link {state_url}')
  print('\nFalharam as seguintes colunas:')
  for i in range(len(result[1])):
    print(f'Coluna: {result[1][i]} - Tamanho: {result[2][i]} - Esperado: {result[3]}')
  print('\nEscrita cancelada\n')


def print_sheet_status(expected: bool, result: tuple[int, list, list, int]):
  if (result[0] != expected):
    print(f'Planilha inválida - Ao todo escreveu-se {result[0]} linhas')
    print(f"O esperado era {expected} linhas")
  print(f'Local de salvamento: {result[1]}\n')


def print_summary():
  pass