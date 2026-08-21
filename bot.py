import os
import threading
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import google.generativeai as genai

# Web Server Render ke liye
app = Flask(__name__)

@app.route('/')
def home():
    return "AASHISH & AJIT VIP AI IS RUNNING!"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

# Gemini AI Setup
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

# Telegram Bot Handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⚡ AASHISH & AJIT VIP AI IS ONLINE! मुझसे कुछ भी पूछो।")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    try:
        response = model.generate_content(user_text)
        await update.message.reply_text(response.text)
    except Exception as e:
        await update.message.reply_text("अरे भाई, कुछ टेक्निकल एरर आ गया! फिर से ट्राई करो।")

if __name__ == "__main__":
    threading.Thread(target=run_web).start()
    bot_token = os.environ.get("TELEGRAM_BOT_TOKEN")
    application = ApplicationBuilder().token(bot_token).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    application.run_polling()
    
  
