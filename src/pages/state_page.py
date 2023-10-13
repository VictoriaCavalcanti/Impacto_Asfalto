from utils.maps import dataset_map

def search_state_page(page, dataset):
    mix = dataset[dataset_map['mix']]
    plants = dataset[dataset_map['plants']]
    urls = dataset[dataset_map['urls']]

    prefix = 'https://asphaltepd.org'
    data_table = page.find('table', id='data-table')
    data_table_body = data_table.find('tbody')
    rows = data_table_body.find_all('tr')

    for row in rows:
        columns = row.find_all('td')
        plants.append(columns[1].text)
        mix.append(columns[2].text)
        link = columns[4].find('a')
        urls.append(prefix + link.get('href'))