from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.environ.get("telegram_bot_token")


async def start(update : Update, context : ContextTypes.DEFAULT_TYPE):
  await update.message.reply_text("This is a Telegram bot that requires to know what are your needs\nand this bot currently doesn't do anything\n improving new features into it")
async def msg(update: Update, context:ContextTypes.DEFAULT_TYPE):
  lines = list(map(str, update.message.text.split("\n")))
  await update.message.reply_text(lines[0])
async def adduser(update:Update, Context:ContextTypes.DEFAULT_TYPE):
  await update.message.reply_text("this is add user function")
  
tg_app = Application.builder().token(TELEGRAM_TOKEN).build()
tg_app.add_handler(CommandHandler("start", start))
tg_app.add_handler(CommandHandler("adduser", adduser))
tg_app.add_handler(MessageHandler(filters.TEXT, msg))

tg_app.run_polling()