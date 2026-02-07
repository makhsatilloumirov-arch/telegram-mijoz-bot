from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, ContextTypes, filters

TOKEN = "8247035853:AAHI9JPbu4FvI6X6JNmp-75Xdn5jyBW4qAM"
ADMIN_ID = 8294387279

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Assalomu alaykum! Xabaringiz qabul qilindi, tez orada javob beramiz."
    )

async def forward_all(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    msg = update.message

    info = (
        f"👤 Yangi mijoz xabari\n"
        f"Ismi: {user.first_name}\n"
        f"Username: @{user.username}\n"
        f"ID: {user.id}"
    )

    await context.bot.send_message(chat_id=ADMIN_ID, text=info)
    await msg.forward(chat_id=ADMIN_ID)

async def reply_from_admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.reply_to_message:
        original = update.message.reply_to_message.forward_from
        if original:
            await update.message.copy(chat_id=original.id)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, forward_all))
app.add_handler(MessageHandler(filters.REPLY & filters.ALL, reply_from_admin))

app.run_polling()
