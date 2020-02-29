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

# usar [-1] para buscar sempre na ultima mensagem recebida pelo BOT
print(msg[-1])

nome = msg[-1]['message']['from']['first_name'] # recebe o nome da pessoa que enviou a msg
msgID = msg[-1]['message']['chat']['id'] # recebe o ID da conversa
texto = msg[-1]['message']['text'] # recebe o texto da msg 

usuarios = [] # lista com os usuarios que ja mandaram msg

print(usuarios)

# funçao para enviar uma mensagem de apresentaçao no primeiro contato
def apresentaçao():
    desconhecido = f'Olá {nome}! Sejá bem vindo(a), eu sou o @TraderMarketStockBot, um BOT em Python que usa a interface do Telegram \
        para te enviar mensagens sobre o mercado de ações de forma rápida e prática.'
    conhecido = f'Olá {nome}! Tudo bem!? Em que posso te ajudar?'
    if msgID in usuarios:
        bot.sendMessage(msgID, conhecido) # retorna uma mensagem pelo ID da conversa
    elif msgID not in usuarios and texto == '/start':
        bot.sendMessage(msgID, desconhecido)
        usuarios.append(msgID) 


# loop para procurar novas msgs e executar a funçao de apresentaçao
bot.message_loop(apresentaçao()) 
