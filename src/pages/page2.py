from utils.maps import dataset_map

def search_page_two(page, dataset):
    aggregate_lime = dataset[dataset_map['aggregate_lime']]
    aggregate_portland = dataset[dataset_map['aggregate_portland']]
    aggregate_crusher = dataset[dataset_map['aggregate_crusher']]

    type_binder = dataset[dataset_map['type_binder']]
    binder = dataset[dataset_map['binder']]
    rap = dataset[dataset_map['rap']]
    ras = dataset[dataset_map['ras']]

    type_mix_additive = dataset[dataset_map['type_mix_additive']]
    mix_additive = dataset[dataset_map['mix_additive']]
    type_binder_additive = dataset[dataset_map['type_binder_additive']]
    binder_additive = dataset[dataset_map['binder_additive']]

    text = page.find('div', id='p2-text')
    ingredient_table = text.find('div', id='ingredient-table')
    table = ingredient_table.find('table')
    rows = table.find_all('tr')

    find_aggregate = False
    find_lime = False
    find_portland = False
    find_ras = False
    find_crusher = False

    find_mix_additive = False
    find_bind_additive = False
    find_binder = False
    find_rap = False

    crusher_values = []
    binder_values = []
    ras_values = []
    type_binder_values = []
    mix_additive_values = []
    type_mix_additive_values = []
    binder_additive_values = []
    type_binder_additive_values = []

    for row in rows:
        columns = row.find_all('td')
        if (columns[1].text.count('Mineral fillers')):
            find_aggregate = True
            index = columns[1].text.index('-')
            size = len(columns[1].text)
            type = columns[1].text[index + 2: size]
            value = columns[2].text
            
            if (type == 'Lime'):
                aggregate_lime.append(value)
                find_lime = True

            elif (type == 'Crusher fines'):
                crusher_values.append(value)
                find_crusher = True

            elif (type == 'Portland cement'):
                aggregate_portland.append(value)
                find_portland = True
            
        elif (columns[0].text == 'RAP'):
            find_rap = True
            rap.append(columns[2].text)

        elif (columns[0].text == 'RAS'):
            find_ras = True
            ras_values.append(columns[2].text)

        elif (columns[0].text == 'Binder'):
            type_binder_values.append(columns[1].text)
            binder_values.append(columns[2].text)
            find_binder = True

        elif (columns[0].text == "Binder Additive"):
            find_bind_additive = True
            type_binder_additive_values.append(columns[1].text)
            binder_additive_values.append(columns[2].text)
            
        elif (columns[0].text == "Mix Additive"):
            find_mix_additive = True
            type_mix_additive_values.append(columns[1].text)
            mix_additive_values.append(columns[2].text)
    
    if (not find_binder):
        binder.append('-')
        type_binder.append('-')
    else:
        binder.append(', '.join(binder_values))
        type_binder.append(', '.join(type_binder_values))

    if (not find_bind_additive):
        binder_additive.append('-')
        type_binder_additive.append('-')
    else:
        binder_additive.append(', '.join(binder_additive_values))
        type_binder_additive.append(', '.join(type_binder_additive_values))

    if (not find_mix_additive):
        mix_additive.append('-')
        type_mix_additive.append('-')
    else:
        mix_additive.append(', '.join(mix_additive_values))
        type_mix_additive.append(', '.join(type_mix_additive_values))

    if (not find_rap):
        rap.append('-')

    if (not find_ras):
        ras.append('-')
    else:
        ras.append(', '.join(ras_values))

    if (not find_aggregate):
        aggregate_lime.append('-')
        aggregate_portland.append('-')
        aggregate_crusher.append('-')
    else:
        if (not find_lime):
            aggregate_lime.append('-')

        if (not find_crusher):
            aggregate_crusher.append('-')
        else:
            aggregate_crusher.append(', '.join(crusher_values))

        if (not find_portland):
            aggregate_portland.append('-')
        
