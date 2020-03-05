import telepot

token = 'token'

bot = telepot.Bot(token)


def manda(id, texto):
    bot.sendMessage(id, texto)

def mandamerda():
    msg = bot.getUpdates()
    nome = msg[-1]['message']['from']['first_name']
    msgID = msg[-1]['message']['chat']['id']
    texto = msg[-1]['message']['text'] 

    manda(msgID, texto)

def  ultimamerda(msg):
    if msg['text'] == '/start':
        mandamerda()


bot.message_loop(ultimamerda) 

while True:
    pass