import logging
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


running_apps = {}

async def sub_bot_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أهلاً بك! هذا البوت تم إنشاؤه بواسطة بوت 𓄂Almansi𖢳.")

async def launch_new_bot(token):
    try:
        sub_app = Application.builder().token(token).build()
        sub_app.add_handler(CommandHandler("start", sub_bot_start))
        
        await sub_app.initialize()
        await sub_app.start_polling()
        running_apps[token] = sub_app
        return True
    except Exception as e:
        print(f"خطأ في التوكن {token}: {e}")
        return False


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أهلاً 𓄂Almansi𖢳! أرسل لي توكن البوت (API Token) لأقوم بتشغيله لك فوراً.")

async def handle_token(update: Update, context: ContextTypes.DEFAULT_TYPE):
    token = update.message.text
    if ":" in token and len(token) > 20: 
        await update.message.reply_text("جاري تشغيل بوتك... انتظر لحظة.")
        success = await launch_new_bot(token)
        if success:
            await update.message.reply_text("مبروك! بوتك الآن يعمل بنجاح.")
        else:
            await update.message.reply_text("فشل التشغيل، تأكد من أن التوكن صحيح.")
    else:
        await update.message.reply_text("هذا لا يبدو توكن صحيحاً.")


if __name__ == '__main__':
    main_token = "8458264998:AAGpd2KPzzsBvOxtIpjUErgC4EYshgC09XQ"
    
    app = Application.builder().token(main_token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_token))
    
    print("البوت الأساسي يعمل...")
    app.run_polling()
