from utils.filters import parentheses_filter
from utils.maps import dataset_map

def search_page_five(page, dataset):
    CO2material = dataset[dataset_map['CO2material']]
    CO2transport = dataset[dataset_map['CO2transport']]
    CO2production = dataset[dataset_map['CO2production']]
    CO2total = dataset[dataset_map['CO2total']]

    text = page.find('div', id='p5-text')
    description = text.find_all('span')

    for element in description:
        if (element.has_attr('id') and element['id'] == 'p5_to_1'):
            value = parentheses_filter(element.text)
            value = value.replace('.', ',')
            CO2material.append(value)

        if (element.has_attr('id') and  element['id'] == 'p5_tp_1'): 
            value = parentheses_filter(element.text)
            value = value.replace('.', ',')
            CO2transport.append(value)

        if (element.has_attr('id') and  element['id'] == 'p5_tq_1'):
            value = parentheses_filter(element.text)
            value = value.replace('.', ',')
            CO2production.append(value)
        
        if (element.has_attr('id') and  element['id'] == 'p5_tr_1'):
            value = parentheses_filter(element.text)
            value = value.replace('.', ',')
            CO2total.append(value)
