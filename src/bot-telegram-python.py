# -*- coding: utf-8 -*-
'''
Criado em 02/2020
Autor: Paulo https://github.com/alpdias
'''

import telepot # API do Telegram

# token de acesso
token = 'token'

# Telegram BOT
bot = telepot.Bot(token)

# recebe a msg/info do BOT em um formato de arquivo JSON
msg = bot.getUpdates()

# usar [-1] para buscar a ultima mensagem recebida pelo BOT
nome = msg[-1]['message']['from']['first_name'] # recebe o nome da pessoa que enviou a msg
msgID = msg[-1]['message']['chat']['id'] # recebe o ID da conversa
texto = msg[-1]['message']['text'] # recebe o texto da msg 

# msg de aprensetaçao
apresentacao = f'Olá {nome}! Sejá bem vindo(a), eu sou o @TraderMarketStockBot, um BOT em Python que usa a interface do Telegram \
para te enviar informações sobre o mercado de ações, de forma rápida e prática.'

# msg com o menu de controles dentro do Telegram
menu = ('Você pode me controlar enviando estes comandos: \
\n \
\n /cotacao - Consultar o valor de ações \
\n /indice - Consultar o valor de índices \
\n /dados - Info sobre a fonte de dados \
\n /menu - Menu de comandos \
\n /info - Info sobre o BOT \
\n /ajuda - Obter ajuda')

# msg para textos ou comandos nao compreendidos / invalidos
invalido = f'{nome}, desculpe mas não entendi seu comando, ainda estou em construção e não consigo compreender muitas coisas, \
tente usar uma das opções dentro do meu menu de controles.'

# funçao para enviar mensagem de apresentaçao e a interaçao com o menu de controles
def comandos():
    if texto == '/start':
        bot.sendMessage(msgID, apresentacao) # retorna uma mensagem pelo ID da conversa 
        bot.sendMessage(msgID, controles)
    elif texto == '/cotacao':
        bot.sendMessage()
    elif texto == '/indice':
        bot.sendMessage()
    elif texto == '/dados':
        bot.sendMessage()
    elif texto ==  '/menu':
        bot.sendMessage()
    elif texto == '/info':  
        bot.sendMessage()
    elif texto == '/ajuda':
        bot.sendMessage()
    else:
        bot.sendMessage(msgID, invalido + '\n' + '\n' + menu)


# loop para procurar novas msgs e executar uma funçao
bot.message_loop(comandos()) 
