def dataset_validator(dataset):
  correct_size = len(dataset[0])
  incorrect_lines = []
  incorrect_lines_size = []
  for i in range(len(dataset)):
    if (len(dataset[i]) != correct_size):
      incorrect_lines.append(dataset[i][0])
      incorrect_lines_size.append(len(dataset[i]))
    
  return (len(incorrect_lines) == 0, incorrect_lines, incorrect_lines_size, correct_size)

def sheet_validator(expected_size, sheet):
  pass