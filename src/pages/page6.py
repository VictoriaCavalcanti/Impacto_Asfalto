from utils.filters import parentheses_filter
from utils.maps import dataset_map


def search_page_six(page, dataset):
    NRPRfuel_mat = dataset[dataset_map['NRPRfuel_mat']]
    NRPRfuel_tra = dataset[dataset_map['NRPRfuel_tra']]
    NRPRfuel_pro = dataset[dataset_map['NRPRfuel_pro']]
    NRPRfuel_total = dataset[dataset_map['NRPRfuel_total']]

    NRPRmat_mat = dataset[dataset_map['NRPRmat_mat']]
    NRPRmat_tra = dataset[dataset_map['NRPRmat_tra']]
    NRPRmat_pro = dataset[dataset_map['NRPRmat_pro']]
    NRPRmat_total = dataset[dataset_map['NRPRmat_total']]

    SM_mat = dataset[dataset_map['SM_mat']]
    SM_tra = dataset[dataset_map['SM_tra']]
    SM_pro = dataset[dataset_map['SM_pro']]
    SM_total = dataset[dataset_map['SM_total']]

    text = page.find('div', id='p6-text')
    description = text.find_all('span')

    #NRPRfuel 
    for element in description:
        if (element.has_attr('id') and element['id'] == 'p6_t1f_1'):
            value = parentheses_filter(element.text)
            NRPRfuel_mat.append(value)

        if (element.has_attr('id') and  element['id'] == 'p6_t1h_1'): 
            value = parentheses_filter(element.text)
            NRPRfuel_tra.append(value)

        if (element.has_attr('id') and  element['id'] == 'p6_t1j_1'):
            value = parentheses_filter(element.text)
            NRPRfuel_pro.append(value)
        
        if (element.has_attr('id') and  element['id'] == 'p6_t1l_1'):
            value = parentheses_filter(element.text)
            NRPRfuel_total.append(value)

        #NRPRmaterial 
        if (element.has_attr('id') and element['id'] == 'p6_t1s_1'):
            value = parentheses_filter(element.text)
            NRPRmat_mat.append(value)

        if (element.has_attr('id') and  element['id'] == 'p6_t1t_1'):
            value = element.text
            NRPRmat_tra.append(value)

        if (element.has_attr('id') and  element['id'] == 'p6_t1v_1'):
            value = element.text
            NRPRmat_pro.append(value)
        
        if (element.has_attr('id') and  element['id'] == 'p6_t1y_1'):
            value = parentheses_filter(element.text)
            NRPRmat_total.append(value)

        #SM
        if (element.has_attr('id') and element['id'] == 'p6_t23_1'):
            value = parentheses_filter(element.text)
            SM_mat.append(value)


        if (element.has_attr('id') and  element['id'] == 'p6_t24_1'): 
            value = element.text[0:3]
            SM_tra.append(value)

        if (element.has_attr('id') and  element['id'] == 'p6_t26_1'):
            value = element.text[0:2]
            SM_pro.append(value)
        
        if (element.has_attr('id') and  element['id'] == 'p6_t29_1'):
            value = parentheses_filter(element.text)
            SM_total.append(value)