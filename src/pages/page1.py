from utils import filters
from utils.definitions import PageOneDefinitions
from utils.maps import dataset_map

def search_page_one(page, dataset):
    gradations = dataset[dataset_map['gradations']]
    performances = dataset[dataset_map['performances']]
    temperatures = dataset[dataset_map['temperatures']]
    type_mix = dataset[dataset_map['type_mix']]

    text = page.find('div', id='p1-text')
    description = text.find_all('span')

    for element in description:
        if (element.has_attr('id') and element['id'] == 'th_1'): 
            gradations.append(filters.gradations_filter(element.text))

        if (element.has_attr('id') and  element['id'] == 'tk_1'): 
            performances.append(filters.performances_filter(element.text))

        if (element.has_attr('id') and  element['id'] == 'tm_1'): 
            temperatures.append(filters.temperatures_filter(element.text))
            
        if (element.has_attr('id') and  element['id'] == 'tm_1'):
            type_mix.append(filters.parentheses_filter(element.text))