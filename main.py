import telegram.ext
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI
load_dotenv()
from telegram import Update


# API-key
TOKEN=os.getenv('TOKEN_TEL')
GOOGLE_API_KEY=os.getenv('GEMINI_API_KEY')





async def start(update, context):
    await update.message.reply_text("Hello! Welcone to Finance Management system :)")


async def llm_response(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text=update.message.text
    model = ChatGoogleGenerativeAI(model="gemini-2.5-flash",
                            google_api_key=GOOGLE_API_KEY,
                             )
    print(f"User messsage: {user_text}")
    
    ai_msg = model.invoke(user_text)
    
    await update.message.reply_text(ai_msg.content)



def main():
    app=ApplicationBuilder().token(token=TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, llm_response))
    app.run_polling()


if __name__=='__main__':
    main()



