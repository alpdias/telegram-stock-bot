# -*- coding: utf-8 -*-
'''
Criado em 03/2020
Autor: Paulo https://github.com/alpdias
'''

import bs4
import requests
from bs4 import BeautifulSoup

def indice(codigo):
    r = requests.get(f'https://finance.yahoo.com/quote/^{codigo}/')
    soup = bs4.BeautifulSoup(r.content, 'html.parser')
    nomeIndice = soup.find_all('div',{'class': 'D(ib) Mt(-5px) Mend(20px) Maw(56%)--tab768 Maw(52%) Ov(h) smartphone_Maw(85%) smartphone_Mend(0px)'})[0].find('h1').text.split()
    valorIndice = soup.find_all('div',{'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    print(f'Índice: {nomeIndice[2]} \
\nValor atual {codigo.upper()}: {valorIndice}')
