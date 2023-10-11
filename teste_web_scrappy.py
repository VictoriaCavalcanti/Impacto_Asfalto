# parãmetros fixos de todas as misturas: PG, temperatura, graduação, tipo de mistura, binder, teor de Co2 do material, transporte e usinagem, energia renovavel fue, material
#e materiais secundários
#preciso de uma lista para tirar o nome das empresas e o nome da mistura
# diferenciar os tipos de material filer: caso encontre, anote o nome e o teor
# diferenciar os tipos de binder additive e mix additive: caso encontre, escrever o nome e o teor 
#printar a lista de links 
#relacionar as posições de cada elemento nas listas criadas em novas listas de forma a conter todas as informações sobre cada mistura e anexar em linhas no excel 

import requests
from bs4 import BeautifulSoup

# Lista de URLs de exemplo
urls_estado = [
    'https://asphaltepd.org/published/CA/',
]
#exemplo: Arizona (AZ) 

#PARA TESTAR SEU PROGRAMA - Vai rodas apenas esses links:
urls_teste = [
    'https://asphaltepd.org/epd/d/OPUDGb/',
]

# urls = [
#     'https://asphaltepd.org/epd/d/OPUDGb/',
#     'https://asphaltepd.org/epd/d/4RUE6g/',
#     'https://asphaltepd.org/epd/d/REUdPg/',
#     'https://asphaltepd.org/epd/d/mYUrRG/',
#     'https://asphaltepd.org/epd/d/rQUraO/',
#     'https://asphaltepd.org/epd/d/pMU9yv/',
#     'https://asphaltepd.org/epd/d/eBUxv/'
# ]

# Constantes auxiliares
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

# Funções auxiliares:
def gradations_filter(string):
    return string[16 : len(string)]

def performances_filter(string):
    return string[-5 : len(string)]

def temperatures_filter(string):
    min_range = string[151 : 154]
    max_range = string[158 : 161]
    result = min_range + '-' + max_range
    return result

#existem dois casos: HMA e WMA e não terão o mesmo intervalo de letras 
def tipomixHMA (string):
    return string [64:68]
def tipomizWMA (string):
    return string [65:69]


# Lista para armazenar os dados
gradations = []
performances = []
temperatures = []
teste = []
aggregate = [] #somente cimento portland 
materialfiller=[]
rap = []
binder = []
binderadditive =[]
mixadditive =[]
co2material
co2transport =[]
co2production =[]
co2total= []
ENRfuel_mat=[]
ENRfuel_tra =[]
ENRfuel_pro=[]
ENRfuel_total=[]
ENRmat_mat=[]
ENRmat_tra=[]
ENRmat_pro=[]
ENRmat_total=[]
SM_mat=[]
SM_tra=[]
SM_pro=[]
SM_total=[] 

# Loop pelas URLs

def acha_links(urls):
    links = []
    prefixo = 'https://asphaltepd.org'
    erros = 0
    for url in urls:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            elements = soup.find_all('a', class_='btn btn-success')
            for link in elements:
                links.append(prefixo + link.get('href'))
            # elements = soup.find_all('span', class_='t s3')
            # for element in elements:
            #     if (element['id']== 'th_1'): pages_brute.append(element.string)
            # for page in pages:
            #     pages_brute.append(pages.text)
        else:
            print(f'Falha na solicitação HTTP para {url}')
            erros += 1
    if (erros != 0):
        print(f'Ao todo {erros} links de estados falharam')
    return links

def procura_pagina_1(pagina):
    text = pagina.find('div', id='p1-text')
    description = text.find_all('span')

    for element in description:
        if (element.has_attr('id') and element['id'] == 'th_1'): 
            gradations.append(gradations_filter(element.text))

        if (element.has_attr('id') and  element['id'] == 'tk_1'): 
            performances.append(performances_filter(element.text))

        if (element.has_attr('id') and  element['id'] == 'tm_1'): 
            temperatures.append(temperatures_filter(element.text))
        
        if (element.has_attr('id') and  element['id'] == 'ti_1'): 
            teste.append(element.text)

def procura_pagina_2(pagina):
    text = pagina.find('div', id='p2-text')
    tabela = text.find('table')
    linhas = tabela.find_all('tr')
    achou_binder = False
    achou_rap = False
    achou_agregate = False

    for linha in linhas:
        colunas = linha.find_all('td')
        if (colunas[1].text.count('Mineral fillers')):
            achou_agregate = True
            aggregate.append(colunas[2].text)
        elif (colunas[0].text == 'RAP'):
            achou_rap = True
            rap.append(colunas[2].text)
        elif (colunas[0].text == 'Binder'):
            binder.append(colunas[2].text)
            achou_binder = True
    
    if (not achou_binder):
        binder.append('-')
    if (not achou_rap):
        rap.append('-')
    if (not achou_agregate):
        aggregate.append('-')

def procura_pagina_5(pagina):
    text = pagina.find ( 
        

def run_scrappy(links):
    acertos = 0
    for url in links:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            paginas = soup.find_all('div', class_='page')
            for pagina in paginas:
                if (pagina['id'] == 'p1'):
                    procura_pagina_1(pagina)
                if (pagina['id'] == 'p2'):
                    procura_pagina_2(pagina)
            acertos += 1
        else:
            print(f'Falha na solicitação HTTP para {url}')

    imprime_listas(len(links))

    if (acertos == len(links)):
        print('Sucesso! Todos os links passaram')
    else:
        print(f'Falha! Ao todo {len(links) - acertos} links falharam!')
    

def get_all_links():
    for url in urls_estado:
        acha_links(url)

def run(teste = False):
    if (teste):
        run_scrappy(urls_teste)
    else:
        links = acha_links(urls_estado)
        run_scrappy(links)

def imprime_listas(num):
    print()
    print(f'Ao todo usou-se {num} links:')
    print()

    print(f'=========================================== Gradação - {len(gradations)} itens =======================================================')
    print()
    print(gradations)
    print()

    print(f'=========================================== Performace (P.G) - {len(performances)} itens ================================================')
    print()
    print(performances)
    print()
    
    print(f'=========================================== Range de Temperatura - {len(temperatures)} itens ============================================')
    print()
    print(temperatures)
    print()

    print(f'=========================================== Cimento Portland (Weight %) - {len(aggregate)} itens =============================================')
    print()
    print(aggregate)
    print()

    print(f'=========================================== RAP (Weight %) - {len(rap)} itens ==================================================')
    print()
    print(rap)
    print()

    print(f'=========================================== BINDER (Weight %) - {len(binder)} itens ===============================================')
    print()
    print(binder)
    print()


def menu_escolha():
    print('Scrappy - Páginas EDP')
    print('Escolha uma opção a seguir: ')
    print(f'1 - Testar usando links de teste ({len(urls_teste)} no total)')
    print(f'2 - Rodar usando links de estado ({len(urls_estado)} no total)')
    print('Sua escolha: ', end='')
    escolha = input()
    return escolha

def main():
    result = menu_escolha()
    while (result != '1' and result != '2'):
        result = menu_escolha()

    if (result == '1'):
        run(True)
    else:
        run()
# Criar um DataFrame com os títulos
#df = pd.DataFrame({'P.': pages_brute})

# Salvar em um arquivo Excel
#df.to_excel('noticias.xlsx', index=False)
main()

#Mudei algo
#Mudei pela internet
