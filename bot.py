import os
import logging
from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(_name_)

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def handle_message(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    message = update.effective_message
    if not message or not message.text:
        return

    signal = message.text
    logger.info("Signal received: %s", signal)

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Signal received and recorded for testing. "
             "No trade has been placed."
    )

def main():
    if not BOT_TOKEN:
        raise RuntimeError("TELEGRAM_BOT_TOKEN is not configured")

    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    )
    logger.info("Telegram signal listener started")
    app.run_polling()

if _name_ == "_main_":
    main()
