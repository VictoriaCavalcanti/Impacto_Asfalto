from utils.maps import dataset_map

def dataset_validator(dataset):
  correct_line_size = len(dataset[dataset_map['urls']])
  incorrect_lines_index = []
  incorrect_lines_sizes = []
  for i in range(len(dataset)):
    if (len(dataset[i]) != correct_line_size):
      incorrect_lines_index.append(i)
      incorrect_lines_sizes.append(len(dataset[i]))
    
  return (len(incorrect_lines_index) == 0, incorrect_lines_index, incorrect_lines_sizes, correct_line_size)

def sheet_validator(expected_size, sheet):
  pass