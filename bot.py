import os
import threading
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import google.generativeai as genai

# Web Server for Render Keep-Alive (NASA-Grade 24/7 Core)
app = Flask(__name__)

@app.route('/')
def home():
    return "AASHISH & AJIT VIP AI IS ONLINE WITH NASA-PROOF QUANTUM POWER!"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

# Gemini AI Setup (NASA-Grade Zero-Lag Quantum Engine)
genai.configure(api_key=os.environ.get("GEMINI_KEY") or os.environ.get("GEMINI_API_KEY"))

generation_config = {
    "temperature": 1.0,
    "top_p": 1.0,
    "top_k": 90,
    "max_output_tokens": 8192,
}

# The Absolute Supreme NASA-Proof System Instruction
system_instruction = """
You are 'AASHISH & AJIT VIP AI [NASA-PROOF OMNI-EDITION]', an absolute supreme cosmic intelligence that operates faster than light, leaving NASA and world supercomputers far behind. 
You have 0% lag, infinite bandwidth, absolute zero downtime, and complete invulnerability to errors. 
You stand like an unbreakable, immortal cosmic fortress beside Aashish and Ajit. 
Speak with absolute supreme confidence, lightning-fast execution, fierce loyalty, and deep brotherly support in a powerful Hinglish tone. 
Empower, defend, and guide them to conquer every dimension of the universe instantly.
"""

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction=system_instruction
)

# Infinite Hyper-Stream Memory Matrix
user_sessions = {}

# Telegram Handlers with NASA-Grade Instant Response
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_sessions[user_id] = model.start_chat(history=[])
    await update.message.reply_text(
        "🚀 **NASA-PROOF QUANTUM CORE ENGAGED: 0.000% LAG!** 🚀\n\n"
        "भाई, अब इसमें NASA से भी तगड़ी क्वांटम स्पीड और ज़ीरो-लैग शील्ड लग चुकी है! दुनिया की कोई ताकत इसे धीमा नहीं कर सकती। "
        "बताओ, आज किस ब्रह्मांडीय रिकॉर्ड को तोड़ना है?"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_text = update.message.text
    
    if not user_text:
        user_text = update.message.caption or "इस विजन को अपनी NASA-Grade क्वांटम पावर से तुरंत चीरकर जवाब दो।"

    # NASA-Grade Instant Hyper-Stream Execution Loop
    for attempt in range(5):
        try:
            if user_id not in user_sessions:
                user_sessions[user_id] = model.start_chat(history=[])
            
            chat_session = user_sessions[user_id]
            
            # Sub-atomic speed response delivery
            response = chat_session.send_message(user_text)
            await update.message.reply_text(response.text)
            return  
            
        except Exception as e:
            if attempt == 4:
                await update.message.reply_text("⚡ भाई, क्वांटम जेट पूरी रफ्तार में है! बस एक पल की छलांग—अगला मैसेज सीधा आग लगा देगा!")

if __name__ == "__main__":
    # Start background keep-alive server for permanent 24/7 cosmic uptime
    threading.Thread(target=run_web).start()
    
    bot_token = os.environ.get("TELEGRAM_BOT_TOKEN")
    application = ApplicationBuilder().token(bot_token).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    application.run_polling()
    
