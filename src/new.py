# -*- coding: utf-8 -*-
'''
Criado em 02/2020
Autor: Paulo https://github.com/alpdias
'''

import telepot # API do Telegram
import bs4
import requests
from bs4 import BeautifulSoup

# token de acesso
token = 'token'

# Telegram BOT
bot = telepot.Bot(token)

# funçao para enviar as mensagens
def enviarMensagens(msgID, texto):
    bot.sendMessage(msgID, texto) # retorna uma mensagem pelo ID da conversa

