#from aiogram.utils import executor
#from executor.app import CHAT_ID
#from executor.handlers import *
#from executor.app import app
from fastapi import FastAPI



app = FastAPI() 
  
  
 @app.get("/") 
 async def root(): 
     return {"message": "Hello World"}
#a
# def notify_message(dp):
#    print('Bot is starting')
#    await dp.bot.send_message(CHAT_ID, text="Bot is starting")

#if __name__ == "__main__":
    # executor.start_polling(dp, skip_updates=True, on_startup=notify_message)
    #app = FastAPI()