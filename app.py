
import os
import telegram
from pymongo import MongoClient

mongo_uri = os.environ['mongodb+srv://2234act:2234act@cluster0.rwjacbj.mongodb.net/?retryWrites=true&w=majority']  
owner_id = os.environ['5062124930']

client = MongoClient(mongo_uri)
db = client['mydatabase']

bot = telegram.Bot(token=os.environ['7138647395:AAHtOzZ7pimS0JgEIS1Fkm7DXPRiE8bItPQ'])

@bot.message_handler(commands=['start'])  
def start(update, context):
   update.message.reply_text("Hello!")

   # authorize owner  
   if update.message.from_user.id == int(owner_id):
      # additional owner commands
      pass

bot.polling()