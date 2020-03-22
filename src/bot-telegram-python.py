# -*- coding: utf-8 -*-
'''
Criado em 02/2020
Autor: Paulo https://github.com/alpdias
'''

# biblioteca para a API do Telegram 'telepot' https://github.com/nickoala/telepot
import telepot

# bibliotecas utilizadas para fazer o webscraping https://github.com/alpdias/raspagem-web-python
import bs4
import requests
from bs4 import BeautifulSoup

# token de acesso
token = 'token'

# Telegram BOT
bot = telepot.Bot(token)

# funçao para enviar as mensagens atravez do BOT
def enviarMensagens(msgID, texto):
    bot.sendMessage(msgID, texto) # retorna uma mensagem pelo ID da conversa + um texto


# funçao para receber o ID + nome do usuario + texto para ser enviado ao BOT
def receberMensagens(texto):
    msg = bot.getUpdates() # recebe a msg/info do BOT em um formato de arquivo JSON
    msgID = msg[-1]['message']['chat']['id'] # recebe o ID da conversa
    nome = msg[-1]['message']['from']['first_name'] # recebe o nome da pessoa que enviou a msg

    # msg de aprensetaçao
    apresentacao = f'Olá {nome}! Sejá bem vindo(a), eu sou o @TraderMarketStockBot, um BOT em Python que usa a interface do Telegram \
para te enviar informações sobre o mercado de ações, de forma rápida e prática.'

    # msg para textos ou comandos nao compreendidos/invalidos
    invalido = f'{nome}, desculpe mas não entendi seu comando, ainda estou em construção e não consigo compreender muitas coisas, \
tente usar uma das opções dentro do meu menu de controles.'

    if texto == 'apresentacao':
        texto = apresentacao
    elif texto == 'invalido':
        texto = invalido + '\n' + '\n' + menu
    
    enviarMensagens(msgID, texto) 


# funçao para formatar os numeros de acordo com o padrao pt-BR
def tratamento(n=0):
    import locale
    locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")
    return (locale.format_string("%.2f", n, grouping=True))


# funçoes para realizar WebScraping
def empresas(codigo):
    r = requests.get(f'https://finance.yahoo.com/quote/{codigo}.SA/')
    soup = bs4.BeautifulSoup(r.content, 'html.parser')
    nomeEmpresa = soup.find_all('div',{'class': 'D(ib) Mt(-5px) Mend(20px) Maw(56%)--tab768 Maw(52%) Ov(h) smartphone_Maw(85%) smartphone_Mend(0px)'})[0].find('h1').text
    valorEmpresa = float(soup.find_all('div',{'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text)
    empresa = f'Empresa: {nomeEmpresa} \
\nPreço atual {codigo.upper()}: {tratamento(valorEmpresa)} - Valor em BRL'
    return empresa


def indices(codigo):
    r = requests.get(f'https://finance.yahoo.com/quote/^{codigo}/')
    soup = bs4.BeautifulSoup(r.content, 'html.parser')
    nomeIndice = soup.find_all('div',{'class': 'D(ib) Mt(-5px) Mend(20px) Maw(56%)--tab768 Maw(52%) Ov(h) smartphone_Maw(85%) smartphone_Mend(0px)'})[0].find('h1').text.split()
    valorIndice = soup.find_all('div',{'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    indice = f'Índice: {nomeIndice[2]} \
\nValor atual {codigo.upper()}: {valorIndice}'
    return indice


# lista com o menu de controles do BOT dentro do Telegram
listaComandos = ['/cotacao', '/dados', '/menu', 'info', '/ajuda']

# msg com o menu de controles do BOT dentro do Telegram
menu = ('Você pode me controlar enviando esses comandos: \
\n \
\n /cotacao - Consultar valores \
\n /dados - Info sobre a fonte de dados \
\n /menu - Menu de comandos \
\n /info - Info sobre o BOT \
\n /ajuda - Obter ajuda')

# msg para perguntar o codigo a ser utilizado no WebScraping
acao = 'Qual o código da ação/índice que você quer consultar?'

# msg com info sobre a fonte de dados utilizada no WebScraping
fonte = 'Fonte de dados: \
\n \
\n \
https://finance.yahoo.com/'

# msg com info sobre o BOT e seu funcionamento
info = 'Para saber mais sobre o meu funcionamento e criação, visite: \
\n \
\n \
https://github.com/alpdias/bot-telegram-python'

# msg com info de ajuda para o usuario
ajuda = 'Se precisar de ajuda ou quiser relatar algum problema, entre em contato: \
\n \
\n \
https://t.me/alpdias'

# funçao para buscar a ultima mensagem recebida pelo BOT e executar os comandos
def comandos(msg):
    if msg['text'] == '/start':
        receberMensagens('apresentacao')
    elif msg['text'] == '/cotacao':
        receberMensagens(acao)
    elif msg['text'] == '/dados':
        receberMensagens(fonte)
    elif msg['text'] ==  '/menu':
        receberMensagens(menu)
    elif msg['text'] == '/info':  
        receberMensagens(info)
    elif msg['text'] == '/ajuda':
        receberMensagens(ajuda)
    elif msg['text'] not in listaComandos:
        try:
            print(empresas(msg['text']))
        except IndexError:
            try:
                print(indices(msg['text']))
            except IndexError:
                receberMensagens('Desculpe, mas não encontrei essa ação/índice com esse código, tente novamente!')
    else:
        receberMensagens('invalido')


# loop para procurar novas msgs e executar as funçoes
bot.message_loop(comandos) 

while True:
    pass
