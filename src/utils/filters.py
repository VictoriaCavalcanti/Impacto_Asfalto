numbers = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')

def state_abbreviation_filter(state_url):
    size = len(state_url)
    return state_url[-3: size - 1]

def gradations_filter(string):
    return string[16 : len(string)]

def performances_filter(text):
    try:
        size = len(text)
        start = text.index('PG')
        return text[start + 3 : size]
    except ValueError:
        return 'Não reportado'
    
def temperatures_filter(string):
    start = string.index('1')

    min_range = string[start : start + 3]
    max_range = string[start + 7 : start + 10]
    result = min_range + '-' + max_range
    return result

# Filtro para pegar dados em parênteses (apenas a primeira ocorrência é pega)
def parentheses_filter(text):
    left = text.index('(')
    right = text.index(')')
    return text[left + 1: right]
