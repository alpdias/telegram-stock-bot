# -*- coding: utf-8 -*-
'''
Criado em 02/2020
Autor: Paulo https://github.com/alpdias
'''

# biblioteca para a API do Telegram https://github.com/nickoala/telepot
import telepot

# bibliotecas utilizadas para fazer o webscraping, repositorio de como usar --> https://github.com/alpdias/raspagem-web-python
import bs4
import requests
from bs4 import BeautifulSoup

# token de acesso
token = 'token'

# Telegram BOT usando 'telepot'
bot = telepot.Bot(token)

# funçao para enviar as mensagens atravez do BOT
def enviarMensagens(msgID, texto):
    bot.sendMessage(msgID, texto) # retorna uma mensagem pelo ID da conversa + um texto


# funçao para buscar a ultima mensagem recebida pelo BOT e executar os comandos
def comandos(msg):
    if msg['text'] == '/start': 
        msg = bot.getUpdates() # recebe a msg/info do BOT em um formato de arquivo JSON
        nome = msg[-1]['message']['from']['first_name'] # recebe o nome da pessoa que enviou a msg
        # msg de aprensetaçao
        apresentacao = f'Olá {nome}! Sejá bem vindo(a), eu sou o @TraderMarketStockBot, um BOT em Python que usa a interface do Telegram \
para te enviar informações sobre o mercado de ações, de forma rápida e prática.'
        # msg com o menu de controles do BOT dentro do Telegram
        menu = ('Você pode me controlar enviando estes comandos: \
\n \
\n /cotacao - Consultar o valor de ações \
\n /indice - Consultar o valor de índices \
\n /dados - Info sobre a fonte de dados \
\n /menu - Menu de comandos \
\n /info - Info sobre o BOT \
\n /ajuda - Obter ajuda')
    elif msg['text'] == '/cotacao':
        açao = 'Qual o código da ação que você quer consultar?'
    elif msg['text'] == '/indice':
        indice = 'Qual o código do índice que você quer consultar?'
    elif msg['text'] == '/dados':
        pass
    elif msg['text'] ==  '/menu':
        # msg com o menu de controles do BOT dentro do Telegram
        menu = ('Você pode me controlar enviando estes comandos: \
\n \
\n /cotacao - Consultar o valor de ações \
\n /indice - Consultar o valor de índices \
\n /dados - Info sobre a fonte de dados \
\n /menu - Menu de comandos \
\n /info - Info sobre o BOT \
\n /ajuda - Obter ajuda')
    elif msg['text'] == '/info':  
        pass
    elif msg['text'] == '/ajuda':
        pass
    else: 
        msg = bot.getUpdates() # recebe a msg/info do BOT em um formato de arquivo JSON
        nome = msg[-1]['message']['from']['first_name'] # recebe o nome da pessoa que enviou a msg
        # msg para textos ou comandos nao compreendidos / invalidos
        invalido = f'{nome}, desculpe mas não entendi seu comando, ainda estou em construção e não consigo compreender muitas coisas, \
tente usar uma das opções dentro do meu menu de controles.'
        # msg com o menu de controles do BOT dentro do Telegram
        menu = ('Você pode me controlar enviando estes comandos: \
\n \
\n /cotacao - Consultar o valor de ações \
\n /indice - Consultar o valor de índices \
\n /dados - Info sobre a fonte de dados \
\n /menu - Menu de comandos \
\n /info - Info sobre o BOT \
\n /ajuda - Obter ajuda')


# loop para procurar novas msgs e executar as funçoes
bot.message_loop(comandos) 

while True:
    pass