from livegram import Livegram

bot = Livegram(token='')

@bot.command('/start')
def start(update):
  update.message.reply_text('Hello!')

@bot.handled_update()  
def handle_updates(update):
  print(update)

bot.run()