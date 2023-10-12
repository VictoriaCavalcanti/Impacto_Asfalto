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
    # 'https://asphaltepd.org/published/CA/',
    #'https://asphaltepd.org/published/CO/',
    'https://asphaltepd.org/published/AL/',


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
def tipoMIX_filter (string):
    return string [65:68]

# Linhas para armazenar os dados pag 1 
gradations = ['Graduação']
performances = ['P.G']
temperatures = ['Temperaturas']
tipoMIX = ['Tipo de Mistura'] 
       #tipobinder = ['Tipo de Binder']

## Agregado e tipos:
aggregate_portland = ['Cimento Portland']
aggregate_lime = ['Lime']
aggregate_crusher = ['Crusher']

rap = ['RAP']
tipobinder =[]
binder = ['Binder']
binderadditive = []
mixadditive = []

#GWP_100
co2material = ['CO2 - Material']
co2transport = ['CO2 - Transport']
co2production = ['CO2 - Production']
co2total = ['CO2 - Total']

NRPRfuel_mat = ['material']
NRPRfuel_tra = ['transporte']
NRPRfuel_pro = ['produção']
NRPRfuel_total = ['total']
NRPRmat_mat = ['material']
NRPRmat_tra = ['transporte']
NRPRmat_pro = ['produção']
NRPRmat_total = ['total']
SM_mat = []
SM_tra = []
SM_pro = []
SM_total = []

# Data set
data_set = [
    binder,#teor 
    performances,
    rap,
    # binderadditive,
    # mixadditive,

    gradations,
    tipoMIX, 
    #Tipo MIX
    temperatures,
    aggregate_lime,
    aggregate_portland,
    # aggregate_crusher,porque foi excluido?

    #GWP_100
    co2material,
    co2transport,
    co2production,
    co2total,
    NRPRfuel_mat,
    NRPRfuel_tra,
    NRPRfuel_pro,
    NRPRfuel_total,
    
    # ENRmat_mat,
    # ENRmat_tra,
    # ENRmat_pro,
    # ENRmat_total,
    # SM_mat,
    # SM_tra,
    # SM_pro,
    # SM_total,
]

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
            
        if (element.has_attr('id') and  element['id'] == 'tm_1'):
            tipoMIX.append(tipoMIX_filter(element.text))
            
        

def procura_pagina_2(pagina):
    text = pagina.find('div', id='p2-text')
    div_table = text.find('div', id='ingredient-table')
    tabela = div_table.find('table')
    linhas = tabela.find_all('tr')
    achou_binder = False
    achou_rap = False
    achou_aggregate = False
    achou_lime = False
    achou_portland = False
    achou_crusher = False

    for linha in linhas:
        colunas = linha.find_all('td')
        if (colunas[1].text.count('Mineral fillers')):
            achou_aggregate = True
            indice = colunas[1].text.index('-')
            tamanho = len(colunas[1].text)
            tipo = colunas[1].text[indice + 2: tamanho]
            valor = colunas[2].text
            
            if (tipo == 'Lime'):
                aggregate_lime.append(valor)
                achou_lime = True

            if (tipo == 'Crusher fines'):
                aggregate_crusher.append(valor)
                achou_crusher = True

            if (tipo == 'Portland cement'):
                aggregate_portland.append(valor)
                achou_portland = True
         
            
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

    if (not achou_aggregate):
        aggregate_lime.append('-')
        aggregate_crusher.append('-')
        aggregate_portland.append('-')
    else:
        if (not achou_lime):
            aggregate_lime.append('-')

        if (not achou_crusher):
            aggregate_crusher.append('-')

        if (not achou_portland):
            aggregate_portland.append('-')

def procura_pagina_5(pagina):
    text = pagina.find('div', id='p5-text')
    description = text.find_all('span')

    for element in description:
        if (element.has_attr('id') and element['id'] == 'p5_to_1'):
            valor = element.text[7:12]
            valor = valor.replace('.', ',')
            co2material.append(valor)

        if (element.has_attr('id') and  element['id'] == 'p5_tp_1'): 
            valor = element.text[7:12]
            valor = valor.replace('.', ',')
            co2transport.append(valor)

        if (element.has_attr('id') and  element['id'] == 'p5_tq_1'):
            valor = element.text[7:12]
            valor = valor.replace('.', ',')
            co2production.append(valor)
        
        if (element.has_attr('id') and  element['id'] == 'p5_tr_1'):
            valor = element.text[7:12]
            valor = valor.replace('.', ',')
            co2total.append(valor)

def procura_pagina_6(pagina):
    text = pagina.find('div', id='p6-text')
    description = text.find_all('span')

    for element in description:
        if (element.has_attr('id') and element['id'] == 'p6_t1f_1'):
            #dar um jeito de pegar somente o que está dentro do parenteses 
            valor = element.text[0:4]
            NRPRfuel_mat.append(valor)

        if (element.has_attr('id') and  element['id'] == 'p6_t1h_1'): 
            valor = element.text[0:4]
            NRPRfuel_tra.append(valor)

        if (element.has_attr('id') and  element['id'] == 'p6_t1j_1'):
            valor = element.text[0:4]
            NRPRfuel_pro.append(valor)
        
        if (element.has_attr('id') and  element['id'] == 'p6_t1l_1'):
            valor = element.text[0:5]
            NRPRfuel_total.append(valor)

            
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
                if (pagina['id'] == 'p5'):
                    procura_pagina_5(pagina)
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

    print(f'=========================================== Tipo de Mistura - {len(tipoMIX)} itens =======================================================')
    print()
    print(tipoMIX)
    print()

    print(f'=========================================== Cimento Portland (Weight %) - {len(aggregate_portland)} itens =============================================')
    print()
    print(aggregate_portland)
    print()

    print(f'=========================================== Lime (Weight %) - {len(aggregate_lime)} itens =============================================')
    print()
    print(aggregate_lime)
    print()

    print(f'=========================================== Crusher (Weight %) - {len(aggregate_crusher)} itens =============================================')
    print()
    print(aggregate_crusher)
    print()

    print(f'=========================================== RAP (Weight %) - {len(rap)} itens ==================================================')
    print()
    print(rap)
    print()

    print(f'=========================================== BINDER (Weight %) - {len(binder)} itens ===============================================')
    print()
    print(binder)
    print()

    print(f'=========================================== CO2 - Material - {len(co2material)} itens ===============================================')
    print()
    print(co2material)
    print()

    print(f'=========================================== CO2 - Transport - {len(co2transport)} itens ===============================================')
    print()
    print(co2transport)
    print()

    print(f'=========================================== CO2 - Production - {len(co2production)} itens ===============================================')
    print()
    print(co2production)
    print()

    print(f'=========================================== CO2 - Total - {len(co2total)} itens ===============================================')
    print()
    print(co2total)
    print()

    print(f'===========================================NRPR fuel - Material - {len(NRPRfuel_mat)} itens ===============================================')
    print()
    print(NRPRfuel_mat)
    print()

    print(f'=========================================== NRPR fuel - Transport - {len(NRPRfuel_tra)} itens ===============================================')
    print()
    print(NRPRfuel_tra)
    print()

    print(f'=========================================== NRPR fuel - Production - {len(NRPRfuel_pro)} itens ===============================================')
    print()
    print(NRPRfuel_pro)
    print()

    print(f'=========================================== NRPR fuel - Total - {len(NRPRfuel_total)} itens ===============================================')
    print()
    print(NRPRfuel_total)
    print()

    
def menu_escolha():
    print('Scrappy - Páginas EDP')
    print('Escolha uma opção a seguir: ')
    print(f'1 - Testar usando links de teste ({len(urls_teste)} no total)')
    print(f'2 - Rodar usando links de estado ({len(urls_estado)} no total)')
    print('Sua escolha: ', end='')
    escolha = input()
    return escolha

def menu_escrita():
    print()
    print('Deseja escrever os dados?')
    print('Digite "S" ou "N"')
    print('Sua escolha: ', end='')
    escolha = input()
    return escolha

def escreve_dados():
    import csv
    # Calcula a transposta da matriz
    dados_transpostos = list(map(list, zip(*data_set)))

    # Nome do arquivo CSV de saída
    nome_arquivo = 'dados_transpostos.csv'

    # Escrever os dados transpostos no arquivo CSV
    with open(nome_arquivo, 'w', newline='') as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        escritor.writerows(dados_transpostos)

    print(f'Dados transpostos foram escritos no arquivo {nome_arquivo}')

def main():
    result = menu_escolha()
    while (result != '1' and result != '2'):
        result = menu_escolha()

    write_result = menu_escrita().lower()
    while (write_result != 's' and write_result != 'n'):
        write_result = menu_escrita().lower()

    if (result == '1'):
        run(True)
    else:
        run()

    if (write_result == 's'):
        escreve_dados()

# Salvar em um arquivo Excel
#df.to_excel('noticias.xlsx', index=False)
main()
