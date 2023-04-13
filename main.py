import logging

from googlesearch import search
from requests.exceptions import HTTPError
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "5897028470:AAGjNAVScjNAogLG-yGY76kyPTtElPue1gA"

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logging.info("Starting bot")
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text="Hello. I`m search bot!"
    )


async def bot_search(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_query = update.message.text.split(" ", 1)[1]

    try:
        logging.info("Making request")
        search_result = next(search(user_query, num_results=1, advanced=True))
    except HTTPError as err:
        logging.warning("Google responded with 429 status code")
        if err.response.status_code == 429:
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="You sent too many requests to google :(",
            )
            return
        raise

    await context.bot.send_message(
        chat_id=update.effective_chat.id, text="Here is your result!"
    )
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"{search_result.title}\n{search_result.url}",
    )


if __name__ == "__main__":
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    start_handler = CommandHandler("start", start)
    search_handler = CommandHandler("search", bot_search)

    application.add_handler(start_handler)
    application.add_handler(search_handler)

    application.run_polling()
