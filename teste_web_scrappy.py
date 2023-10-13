#preciso de uma lista para tirar o nome das empresas e o nome da mistura
# diferenciar os tipos de material filer: caso encontre, anote o nome e o teor
# diferenciar os tipos de binder additive e mix additive: caso encontre, escrever o nome e o teor 
#printar a lista de links 

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
def gradations_filter(text):
    return text[16 : len(text)]

def performances_filter(text):
    result = ''
    try:
        size = len(text)
        start = text.index('PG')
        return text[start + 3 : size]
    except ValueError:
        return 'Not Reported'

def temperatures_filter(string):
    min_range = string[151 : 154]
    max_range = string[158 : 161]
    result = min_range + '-' + max_range
    return result

# Filtro para pegar dados em parênteses
def parentheses_filter(text):
    left = text.index('(')
    right = text.index(')')
    return text[left + 1: right]


#existem dois casos: HMA e WMA e não terão o mesmo intervalo de letras 
def tipoMIX_filter (string):
    return string [65:68]

urls = ['URLS']

# Linhas para armazenar os dados pag 1 
gradations = ['Graduação']
performances = ['P.G']
temperatures = ['Temperaturas']
tipoMIX = ['Tipo de Mistura'] 

## Agregado e tipos:
aggregate_portland = ['Cimento Portland']
aggregate_lime = ['Lime']
aggregate_crusher = ['Crusher']

rap = ['RAP']
tipobinder =['Tipo de binder']
binder = ['Binder']
tipobinderadditive=['Binder additive- Tipo'] 
binderadditive = ['Binder additive - teor ']
tipomixadditive = ['Mix additive - tipo']
mixadditive =['Mix additive - teor'] 

#GWP_100
co2material = ['CO2 - Material']
co2transport = ['CO2 - Transport']
co2production = ['CO2 - Production']
co2total = ['CO2 - Total']

NRPRfuel_mat = ['NRPR Fuel - Material']
NRPRfuel_tra = ['NRPR Fuel - Transport']
NRPRfuel_pro = ['NRPR Fuel - Production']
NRPRfuel_total = ['NRPR Fuel - Total']

NRPRmat_mat = ['NRPR Mat - Material']
NRPRmat_tra = ['NRPR Mat - Transport']
NRPRmat_pro = ['NRPR Mat - Production']
NRPRmat_total = ['NRPR Mat - Total']

SM_mat = ['SM - Material']
SM_tra = ['SM - Transport']
SM_pro = ['SM - Production']
SM_total = ['SM - Total']

# Data set
data_set = [
    urls,
    tipobinder, 
    binder,#teor 
    performances,
    rap,
    tipobinderadditive,
    binderadditive,
    tipomixadditive,
    mixadditive,

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

    NRPRmat_mat,
    NRPRmat_tra,
    NRPRmat_pro,
    NRPRmat_total,

    SM_mat,
    SM_tra,
    SM_pro,
    SM_total, 
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
            tipoMIX.append(parentheses_filter(element.text))   
        

def procura_pagina_2(pagina):
    text = pagina.find('div', id='p2-text')
    div_table = text.find('div', id='ingredient-table')
    tabela = div_table.find('table')
    linhas = tabela.find_all('tr')
    achou_binder = False
    achou_tipobinder = False 
    achou_rap = False
    achou_aggregate = False
    achou_lime = False
    achou_portland = False
    achou_crusher = False
    achou_tipobinderadditive = False 
    achou_tipomixadditive = False 
    achou_binderadditive = False 
    achou_mixadditive = False 

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
            achou_tipobinder = True
            achou_binder = True
            tipobinder.append(colunas[1].text)
            binder.append(colunas[2].text)

        elif (colunas [0].text == "Binder Additive"):
            achou_tipobinderadditive = True
            tipobinderadditive.append(colunas[1].text)
            achou_binderadditive= True 
            binderadditive.append(colunas[2].text[0,1])
            
        elif (colunas [0].text == "Mix Additive"):
            achou_tipomixadditive = True
            achou_mixadditive = True
            tipomixadditive.append (colunas[1].text)
            mixadditive.append(colunas[2].text[-1])
            
    
    if (not achou_binder):
        binder.append('-') #acho que dá pra excluir toda a função, todos tem algum binder 
    if (not achou_tipobinder):
        tipobinder.append('-')

    if (not achou_rap):
        rap.append('-')

    if (not achou_tipobinderadditive):
        tipobinderadditive.append ('-')
    if (not achou_binderadditive):
        binderadditive.append('-')
        
    if (not achou_tipomixadditive):
        tipomixadditive.append('-')
    if (not achou_mixadditive):
        mixadditive.append ('-')
        
        
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
            valor = parentheses_filter(element.text)
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
    acerto_parcial = 0
    text = pagina.find('div', id='p6-text')
    description = text.find_all('span')

    #NRPRfuel 
    for element in description:
        if (element.has_attr('id') and element['id'] == 'p6_t1f_1'):
            valor = parentheses_filter(element.text)
            NRPRfuel_mat.append(valor)

        if (element.has_attr('id') and  element['id'] == 'p6_t1h_1'): 
            valor = parentheses_filter(element.text)
            NRPRfuel_tra.append(valor)

        if (element.has_attr('id') and  element['id'] == 'p6_t1j_1'):
            valor = parentheses_filter(element.text)
            NRPRfuel_pro.append(valor)
        
        if (element.has_attr('id') and  element['id'] == 'p6_t1l_1'):
            valor = parentheses_filter(element.text)
            NRPRfuel_total.append(valor)

        #NRPRmaterial 
        if (element.has_attr('id') and element['id'] == 'p6_t1s_1'):
            valor = parentheses_filter(element.text)
            NRPRmat_mat.append(valor)

        if (element.has_attr('id') and  element['id'] == 'p6_t1t_1'):#printar N/A em todas as colunas
            valor = element.text [0:3]
            NRPRmat_tra.append(valor)

        if (element.has_attr('id') and  element['id'] == 'p6_t1v_1'): #printar N/A em todas as colunas
            valor = element.text [0:3]
            NRPRmat_pro.append(valor)
        
        if (element.has_attr('id') and  element['id'] == 'p6_t1y_1'):
            valor = parentheses_filter(element.text)
            NRPRmat_total.append(valor)

        #SM
        if (element.has_attr('id') and element['id'] == 'p6_t23_1'):
            valor = parentheses_filter(element.text)
            SM_mat.append(valor)


        if (element.has_attr('id') and  element['id'] == 'p6_t24_1'): 
            valor = element.text  
            SM_tra.append(valor)

        if (element.has_attr('id') and  element['id'] == 'p6_t26_1'):
            valor = element.text
            SM_pro.append(valor)
        
        if (element.has_attr('id') and  element['id'] == 'p6_t29_1'):
            valor = parentheses_filter(element.text)
            SM_total.append(valor)
            
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
                if (pagina['id'] == 'p6'):
                    procura_pagina_6(pagina)
            acertos += 1
            urls.append(url)
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

    print(f'=========================================== Gradação - {len(gradations) - 1} itens =======================================================')
    print()
    print(gradations)
    print()

    print(f'=========================================== Performace (P.G) - {len(performances) - 1} itens ================================================')
    print()
    print(performances)
    print()
    
    print(f'=========================================== Range de Temperatura - {len(temperatures) - 1} itens ============================================')
    print()
    print(temperatures)
    print()

    print(f'=========================================== Tipo de Mistura - {len(tipoMIX) - 1} itens =======================================================')
    print()
    print(tipoMIX)
    print()

    print(f'=========================================== Cimento Portland (Weight %) - {len(aggregate_portland) - 1} itens =============================================')
    print()
    print(aggregate_portland)
    print()

    print(f'=========================================== Lime (Weight %) - {len(aggregate_lime) - 1} itens =============================================')
    print()
    print(aggregate_lime)
    print()

    print(f'=========================================== Crusher (Weight %) - {len(aggregate_crusher) - 1} itens =============================================')
    print()
    print(aggregate_crusher)
    print()

    print(f'=========================================== RAP (Weight %) - {len(rap) - 1} itens ==================================================')
    print()
    print(rap)
    print()

    print(f'=========================================== BINDER - tipo - {len(tipobinder) - 1} itens ===============================================')
    print()
    print(tipobinder)
    print()
    
    print(f'=========================================== BINDER (Weight %) - {len(binder) - 1} itens ===============================================')
    print()
    print(binder)
    print()

    print(f'=========================================== BINDER ADDITIVE - tipo -{len(tipobinderadditive) - 1} itens =======================================================')
    print()
    print(tipobinderadditive)
    print()

    print(f'=========================================== BINDER ADDITIVE - teor -{len(binderadditive) - 1} itens =======================================================')
    print()
    print(binderadditive)
    print()

    print(f'=========================================== MIX ADDITIVE - tipo -{len(tipomixadditive) - 1} itens =======================================================')
    print()
    print(tipomixadditive)
    print()

    print(f'=========================================== MIX ADDITIVE - teor -{len(mixadditive) - 1} itens =======================================================')
    print()
    print(mixadditive)
    print()

    print(f'=========================================== CO2 - Material - {len(co2material) - 1} itens ===============================================')
    print()
    print(co2material)
    print()

    print(f'=========================================== CO2 - Transport - {len(co2transport) - 1} itens ===============================================')
    print()
    print(co2transport)
    print()

    print(f'=========================================== CO2 - Production - {len(co2production) - 1} itens ===============================================')
    print()
    print(co2production)
    print()

    print(f'=========================================== CO2 - Total - {len(co2total) - 1} itens ===============================================')
    print()
    print(co2total)
    print()

    print(f'===========================================NRPR fuel - Material - {len(NRPRfuel_mat) - 1} itens ===============================================')
    print()
    print(NRPRfuel_mat)
    print()

    print(f'=========================================== NRPR fuel - Transport - {len(NRPRfuel_tra) - 1} itens ===============================================')
    print()
    print(NRPRfuel_tra)
    print()

    print(f'=========================================== NRPR fuel - Production - {len(NRPRfuel_pro) - 1} itens ===============================================')
    print()
    print(NRPRfuel_pro)
    print()

    print(f'=========================================== NRPR fuel - Total - {len(NRPRfuel_total) - 1} itens ===============================================')
    print()
    print(NRPRfuel_total)
    print()

    print(f'===========================================NRPR material - Material - {len(NRPRmat_mat) - 1} itens ===============================================')
    print()
    print(NRPRmat_mat)
    print()

    print(f'=========================================== NRPR material - Transport - {len(NRPRmat_tra) - 1} itens ===============================================')
    print()
    print(NRPRmat_tra)
    print()

    print(f'=========================================== NRPR material - Production - {len(NRPRmat_pro) - 1} itens ===============================================')
    print()
    print(NRPRmat_pro)
    print()

    print(f'=========================================== NRPR material - Total - {len(NRPRmat_total) - 1} itens ===============================================')
    print()
    print(NRPRmat_total)
    print()

    print(f'=========================================== SM - Material - Total - {len(SM_mat) - 1} itens ===============================================')
    print()
    print(SM_mat)
    print()
    
    print(f'=========================================== SM- Transport - Total - {len(SM_tra) - 1} itens ===============================================')
    print()
    print(SM_tra)
    print()

    print(f'=========================================== SM - Production - Total - {len(SM_pro) - 1} itens ===============================================')
    print()
    print(SM_pro)
    print()

    print(f'=========================================== SM - Total - Total - {len(SM_total) - 1} itens ===============================================')
    print()
    print(SM_total)
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



#fazer uma lista anotando o nome do binder
# nome e teor de binder additive e mix additive, caso encontrre
#traduzir todos os "dense, open e not reported" para portugues 


