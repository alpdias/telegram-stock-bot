# -*- coding: utf-8 -*-

'''
Criado em 02/2020
Autor: Paulo https://github.com/alpdias
'''

from time import sleep
import emoji

# bibliotecas para a API do telegram 'telepot' https://github.com/nickoala/telepot
import telepot
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

# bibliotecas utilizadas para fazer o webscraping, exemplo: https://github.com/alpdias/raspagem-web-python
import bs4
import requests
from bs4 import BeautifulSoup

token = 'token' # token de acesso

bot = telepot.Bot(token) # telegram bot

def enviarMensagens(msgID, texto, botao=''): # funçao para enviar as mensagens atravez do bot
    bot.sendChatAction(msgID, 'typing') # mostra a açao de 'escrever' no chat
    sleep(1)
    bot.sendMessage(msgID, texto, reply_markup=botao) # retorna uma mensagem pelo ID da conversa + um texto + um botao

    
'''
def padrao(n=0): # funçao para formatar os numeros de acordo com o padrao pt-BR
    import locale
    locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")
    return (locale.format_string("%", n, grouping=True))
'''

def empresa(codigo): # funçao para realizar o webscraping de empresas no site https://finance.yahoo.com/
    r = requests.get(f'https://finance.yahoo.com/quote/{codigo}.SA/')
    soup = bs4.BeautifulSoup(r.content, 'html.parser')
    listaNomeEmpresa = soup.find_all('div',{'class': 'D(ib) Mt(-5px) Mend(20px) Maw(56%)--tab768 Maw(52%) Ov(h) smartphone_Maw(85%) smartphone_Mend(0px)'})[0].find('h1').text.split()
    del listaNomeEmpresa[0]
    del listaNomeEmpresa[0]
    nomeEmpresa = ' '.join(listaNomeEmpresa)
    valorEmpresa = float(soup.find_all('div',{'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text)
    empresa = (emoji.emojize(f'Empresa: {nomeEmpresa} :office_building: \
\n\
\n{codigo.upper()} :money_bag: {valorEmpresa:.2f} - Valor em BRL', use_aliases=True))
    return empresa 


def indice(codigo): # funçao para realizar o webscraping de indices no site https://finance.yahoo.com/
    r = requests.get(f'https://finance.yahoo.com/quote/^{codigo}/')
    soup = bs4.BeautifulSoup(r.content, 'html.parser')
    nomeIndice = soup.find_all('div',{'class': 'D(ib) Mt(-5px) Mend(20px) Maw(56%)--tab768 Maw(52%) Ov(h) smartphone_Maw(85%) smartphone_Mend(0px)'})[0].find('h1').text.split()
    valorIndice = soup.find_all('div',{'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    indice = (emoji.emojize(f'Índice: {nomeIndice[2]} :chart_increasing:\
\n\
\n{codigo.upper()} :label: {valorIndice} - Valor em pontos', use_aliases=True))
    return indice 


def paridade(moeda): # funçao para realizar o webscraping de paridade no site https://finance.yahoo.com/
    r = requests.get(f'https://finance.yahoo.com/quote/{moeda}=X?p={moeda}=X&.tsrc=fin-srch')
    soup = bs4.BeautifulSoup(r.content, 'html.parser')
    nomeMoeda = soup.find_all('div',{'class': 'D(ib) Mt(-5px) Mend(20px) Maw(56%)--tab768 Maw(52%) Ov(h) smartphone_Maw(85%) smartphone_Mend(0px)'})[0].find('h1').text.split()
    valorMoeda = soup.find_all('div',{'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    moeda = (emoji.emojize(f'Paridade: {nomeMoeda[2]} :currency_exchange:\
\n\
\n:dollar_banknote: {valorMoeda} - valor em {moeda}', use_aliases=True))
    return moeda


listaComandos = ['/start', '/consultar', '/dados', '/menu', '/info', '/ajuda'] # lista com o menu de comandos do bot dentro do telegram

menu = (emoji.emojize('Você pode me controlar enviando esses comandos :page_with_curl: \
\n \
\n /start - Começar \
\n /consultar - Consultar valores \
\n /dados - Fonte de dados \
\n /menu - Menu de comandos \
\n /info - Info sobre o bot \
\n /ajuda - Obter ajuda', use_aliases=True)) # msg com o menu de comandos do bot dentro do telegram

fonte = (emoji.emojize('Fonte de dados utilizada para obter os valores :chart_decreasing: \
\n \
\n \
https://finance.yahoo.com/', use_aliases=True)) # msg com info sobre a fonte de dados utilizada no webscraping

info = (emoji.emojize('Para saber mais sobre o meu funcionamento e criação, visite meu repositório no GitHub :globe_showing_Americas: \
\n \
\n \
https://github.com/alpdias/bot-telegram-python', use_aliases=True)) # msg com info sobre o BOT e o seu funcionamento

ajuda = (emoji.emojize('Se precisar de alguma ajuda ou quiser relatar alguma coisa, entre em contato com o meu desenvolvedor pelo telegram :mobile_phone_with_arrow: \
\n \
\n \
https://t.me/alpdias', use_aliases=True)) # msg com info de ajuda para o usuario

empresas = ['ABCB4','ABEV3','AGRO3','AHEB3','AHEB5','AHEB6','ALPA3','ALPA4','ALSC3','ALUP11','AMAR3','ANIM3','APTI3','APTI4','ARTR3',
'ARZZ3','AZEV3','AZEV4','BAHI3','BAUH4','BBAS3','BBDC3','BBDC4','BBSE3','BBTG11','BDLL4','BDLL4','BEEF3','BEES3','BEES4','BGIP3',
'BGIP4','BIOM3','BMEB3','BMEB4','BMIN3','BMIN4','BMKS3','BMTO3','BMTO4','BNBR3','BOBR4','BPAN4','BPAR3','BPHA3','BRAP3','BRAP4',
'BRFS3','BRGE11','BRGE12','BRGE3','BRGE5','BRGE6','BRGE7','BRGE8','BRIN3','BRIV3','BRIV4','BRKM3','BRKM5','BRKM6','BRML3','BRPR3',
'BRSR3','BRSR5','BRSR6','BSEV','BSLI3','BTOW3','BTTL3','BTTL4','BUET3','BUET4','BVMF3','CAMB4','CARD3','CASN3','CASN4','CCPR3','CCRO3',
'CCXC3','CEDO3','CEDO4','CEGR3','CELP7','CEPE3','CEPE5','CEPE6','CESP3','CESP6','CGAS3','CGAS5','CGRA3','CGRA4','CIEL3','CLSC3','CLSC4',
'CMIG3','CMIG4','COCE3','COCE5','COCE6','CORR3','CORR4','CPFE3','CPLE3','CPLE6','CPRE3','CREM3','CRIV3','CRIV4','CSAB3','CSAB4','CSAN3',
'CSMG3','CSNA3','CSRN3','CTAX3','CTAX4','CTIP3','CTKA3','CTKA4','CTNM3','CTNM4','CTSA3','CTSA4','CTSA8','CVCB3','DASA3','DAYC4','DHBI3',
'DHBI4','DHBI4','DOHL3','DOHL4','DTCY3','DTEX3','DUQE3','DUQE4','EALT3','EALT3','EALT4','EALT4','ECOR3','ECPR3','ECPR4','EGIE3','ELEK3',
'ELEK4','ELET3','ELET6','ELPL4','EMBR3','ENBR3','ENGI11','EQTL3','ESTC3','ESTR3','ESTR4','FBMC3','FBMC4','FESA3','FESA4','FHER3','FIBR3',
'FIGE3','FIGE4','FJTA3','FJTA3','FJTA4','FJTA4','FLRY3','FRAS3','FRAS3','FRIO3','FRIO3','FRTA3','GGBR3','GGBR4','GOAU3','GOAU4','GOLL4',
'GPCP3','GRND3','GSHP3','GUAR3','GUAR4','HBTS5','HETA3','HETA4','HGTX3','HOOT4','HYPE3','IDNT3','IDVL3','IDVL4','IGBR3','IGTA3','IMBI3',
'IMBI4','INEP3','INEP3','INEP4','INEP4','ITEC3','ITSA3','ITSA4','ITUB3','ITUB4','JBDU3','JBDU4','JBSS3','JHSF3','JOPA3','JOPA4','JSLG3',
'KEPL3','KEPL3','KLBN11','KLBN3','KLBN4','KROT3','LAME3','LAME4','LCAM3','LEVE3','LEVE3','LFFE3','LFFE4','LHER3','LHER4','LIGT3','LINX3',
'LIPR3','LIXC3','LIXC4','LLIS3','LOGN3','LREN3','LUPA3','LUPA3','LUXM3','LUXM4','MAPT3','MAPT4','MDIA3','MEAL3','MEND3','MEND5','MEND6',
'MERC3','MERC3','MERC4','MERC4','MGEL3','MGEL4','MGLU3','MILS3','MLFT3','MLFT4','MMAQ3','MMAQ3','MMAQ4','MMAQ4','MMXM11','MMXM3','MNDL3',
'MNPR3','MOAR3','MPLU3','MRFRG3','MSPA3','MSPA4','MTSA3','MTSA3','MTSA4','MTSA4','MULT3','MWET3','MWET3','MWET4','MWET4','MYPK3','MYPK3',
'NAFG3','NAFG4','NATU3','NORD3','NORD3','ODPV3','OFSA3','OGSA3','OGSA3','OGXP3','OIBR3','OIBR4','OSXB3','PARC3','PATI3','PATI4','PCAR3',
'PCAR4','PEAB3','PEAB4','PETR3','PETR4','PFRM3','PINE4','PLAS3','PLAS3','PMAM3','PNVL3','PNVL4','POMO3','POMO3','POMO4','POMO4','POSI3',
'PPAR3','PRIO3','PRML3','PSSA3','PTNT3','PTNT4','QGEP3','QUAL3','RADL3','RANI3','RANI4','RAPT4','RAPT4','RCSL4','RENT3','RLOG3','RNEW11',
'ROMI3','ROMI3','RPAD3','RPAD5','RPAD6','RPMG3','RUMO3','SANB11','SANB4','SAPR3','SAPR4','SBSP3','SCAR3','SCLO3','SCLO4','SEDU3','SEER3',
'SGPS3','SHOW3','SHUL4','SHUL4','SJOS3','SJOS4','SLCE3','SLED3','SLED4','SMLE3','SMTO3','SNSL3','SOND3','SOND5','SOND6','SPRI3','SPRI5',
'SPRI6','SSBR3','STBP11','SULA11','SULT3','SULT4','SUZB5','SUZB6','TAEE11','TCNO3','TCNO4','TECN3','TEKA3','TEKA4','TELB3','TELB4','TEMP3',
'TENE5','TENE6','TENE7','TERI3','TGMA3','TIET11','TIMP3','TKNO3','TKNO4','TOYB3','TOYB4','TPIS3','TRPN3','TRPN3','TTS3','TUPY3','TUPY3',
'TXRX3','TXRX4','UCAS3','UGPA3','UNIP3','UNIP5','UNIP6','USIM3','USIM5','USIM6','VAGR3','VALE3','VALE5','VIGR3','VIVT3','VIVT4','VLID3',
'VSPT3','VULC3','VVAR11','VVAR3','WEGE3','WEGE3','WHRL3','WHRL4','WMBY3'] # lista com as empresas listadas na B3

indices = ['GSPC', 'DJI', 'IXIC', 'NYA', 'XAX', 'BUK100P', 'RUT', 'VIX', 'FTSE', 'GDAXI', 'FCHI', 'STOXX50E', 'N100', 'BFX', 'IMOEX.ME', 
'N225', 'HSI', '000001.SS', 'STI', 'AXJO', 'AORD', 'BSESN', 'JKSE', 'KLSE', 'NZ50', 'KS11', 'TWII', 'GSPTSE', 'BVSP', 'MXX', 'IPSA', 'MERV', 
'TA125.TA', 'CASE30', 'JN0U.JO'] # lista com os principais indices mundiais

moedas = ['USD', 'BRL', 'JYP', 'GBP', 'CAD', 'EUR', 'CHF', 'ZAR', 'AUD', 'NOK', 'NZD', 'RUB', 'PLN', 'HKD', 'SGD', 'INR', 'TRY'] # lista com as principais moedas mundiais

def receberMensagens(msg): # funçao para buscar as mensagens recebidas pelo bot e executar os comandos
    msgID = msg['chat']['id'] # variavel para receber o ID da conversa
    nome = msg['chat']['first_name'] # variavel para receber o nome do usuario que enviou a msg
    botao = '' # variavel para receber o botao a ser enviado dentro da interface do telegram

    if msg['text'] == '/start':
        botao = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=(emoji.emojize('Consultar Valores :magnifying_glass_tilted_left:', use_aliases=True)), callback_data='consultar')]])
        apresentacao = (f'Olá {nome}, sejá bem vindo(a)! Eu sou o @TraderMarketStockBot, um bot em python que usa a interface do telegram para te enviar informações sobre o mercado financeiro em tempo real de forma rápida e prática.') # msg de aprensentaçao
        começar = (emoji.emojize(f'Você pode iniciar uma consulta apertando o botão abaixo :backhand_index_pointing_down: ou se quiser ser mais rápido apenas me envie um código para consulta a qualquer momento :eyes:', use_aliases=True))
        enviarMensagens(msgID, apresentacao)
        enviarMensagens(msgID, começar, botao)

    elif msg['text'] == '/consultar':
        botao = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Ação', callback_data='consultarEmpresas')], [InlineKeyboardButton(text='Índice', callback_data='consultarIndices')], [InlineKeyboardButton(text='Moeda', callback_data='consultarMoedas')]])
        consultar = (emoji.emojize('Você quer consultar uma ação, um índice ou uma paridade de moeda? :thinking_face:', use_aliases=True)) # msg para identificar o tipo da consulta no webscraping
        enviarMensagens(msgID, consultar, botao)

    elif msg['text'] == '/dados':
        enviarMensagens(msgID, fonte)

    elif msg['text'] ==  '/menu':
        enviarMensagens(msgID, menu)

    elif msg['text'] == '/info':  
        enviarMensagens(msgID, info)

    elif msg['text'] == '/ajuda':
        enviarMensagens(msgID, ajuda)

    elif msg['text'].upper() in empresas:
        try:
            botao = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=(emoji.emojize('Nova Consulta :clipboard:', use_aliases=True)), callback_data='novaConsulta')]]) # botao para uma nova consulta
            enviarMensagens(msgID, empresa(msg['text']), botao)
            
        except IndexError:
            enviarMensagens(msgID, 'Desculpe, aconteceu um erro inesperado, tente novamente!') # erro caso a fonte/site do webxcraping não funcione (não testado)

    elif msg['text'].upper() in indices:
        try:
            botao = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=(emoji.emojize('Nova Consulta :clipboard:', use_aliases=True)), callback_data='novaConsulta')]]) # botao para uma nova consulta
            enviarMensagens(msgID, indice(msg['text']), botao)
            
        except IndexError:
                enviarMensagens(msgID, 'Desculpe, aconteceu um erro inesperado, tente novamente!') # erro caso a fonte/site do webscraping não funcione (não testado)
                
    elif msg['text'].upper() in moedas:
        try:
            botao = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=(emoji.emojize('Nova Consulta :clipboard:', use_aliases=True)), callback_data='novaConsulta')]]) # botao para uma nova consulta
            enviarMensagens(msgID, paridade(msg['text']), botao)
            
        except IndexError:
            enviarMensagens(msgID, 'Desculpe, aconteceu um erro inesperado, tente novamente!') # erro caso a fonte/site do webscraping não funcione (não testado)
            
    else:
        botao = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=(emoji.emojize('Relatar Problema :prohibited:', use_aliases=True)), url='https://t.me/alpdias')]])
        invalido = (emoji.emojize(f'{nome}, desculpe mas não entendi o seu comando, ainda estou em construção e não consigo compreender muitas \
coisas, tente usar uma das opções dentro do meu menu de comandos.' + '\n' + '\n' + menu + '\n' + '\n' + 'Para informar um erro \
ou problema entre em contato com o meu desenvolvedor via telegram, é só clicar no botão abaixo :backhand_index_pointing_down:', use_aliases=True)) # msg para textos ou comandos nao compreendidos/invalidos
        enviarMensagens(msgID, invalido, botao)


def responderMensagens(msg): # funçao para interagir com os botoes do bot dentro do telegram
    msgID, respostaID, resposta = telepot.glance(msg, flavor='callback_query') # variaveis que recebem o 'callback query' da resposta (necessario 3 variaveis, o ID da conversa e o da resposta sao diferentes)
    
    if resposta == 'consultar':
        bot.answerCallbackQuery(msgID, text=(emoji.emojize('Carregando... :gear:', use_aliases=True))) # mostra um texto/alerta na tela do chat
        sleep(2)
        botao = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Ação', callback_data='consultarEmpresas')], [InlineKeyboardButton(text='Índice', callback_data='consultarIndices')], [InlineKeyboardButton(text='Moeda', callback_data='consultarMoedas')]])
        consultar = (emoji.emojize('Você quer consultar uma ação, um índice ou uma paridade de moeda? :thinking_face:', use_aliases=True)) # msg para identificar o tipo da consulta no webscraping
        enviarMensagens(respostaID, consultar, botao)

    elif resposta == 'consultarEmpresas':
        consultarEmpresas = 'Qual o código da ação que você quer consultar?'
        enviarMensagens(respostaID, consultarEmpresas)

    elif resposta == 'consultarIndices':
        consultarIndices = 'Qual o código do índice que você quer consultar?'
        enviarMensagens(respostaID, consultarIndices)

    elif resposta == 'novaConsulta':
        botao = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Ação', callback_data='consultarEmpresas')], [InlineKeyboardButton(text='Índice', callback_data='consultarIndices')], [InlineKeyboardButton(text='Moeda', callback_data='consultarMoedas')]])
        consultar = (emoji.emojize('Você quer consultar uma ação, um índice ou uma paridade de moeda? :thinking_face:', use_aliases=True)) # msg para identificar o tipo da consulta no webscraping
        enviarMensagens(respostaID, consultar, botao)

    elif resposta == 'consultarMoedas':
        moeda = (emoji.emojize('Qual a moeda você quer consultar? :money_with_wings:', use_aliases=True))
        enviarMensagens(respostaID, moeda)
        obsMoeda = (emoji.emojize('Atenção :exclamation mark: Envie apenas a sigla da moeda que você quer consultar, as moedas são equiparadas diante ao dólar americano.'))
        enviarMensagens(respostaID, obsMoeda)
        
    else:
        pass

# loop do modulo 'telepot' para procurar e receber novas mensagens, executando as funçoes
bot.message_loop({'chat': receberMensagens, 'callback_query': responderMensagens}) 

# loop em python para manter o programa rodando
while True:
    pass
