import logging
import asyncio
import threading
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from cobretad import cobretad
import os
from pathlib import Path
from telegram import Bot
from telegram import ForceReply, Update
from telegram import ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# Enable logging
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

bot = Bot("") # Aquí se debe poner el token

# Define a few command handlers. These usually take the two arguments update and
# context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    if user.id not in user_chat_ids:
        return
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )

async def avisar(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send the message "Ya voy subiendo" using /send_to_all when the command /avisar is issued."""
    message = "Ya voy subiendo"
    for chat_id in user_chat_ids:
        await context.bot.send_message(chat_id=chat_id, text=message)

async def send_to_all(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /send_to_all is issued."""
    message = ' '.join(context.args)
    if not message:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="No se proporcionó ningún mensaje.")
        return

    for chat_id in user_chat_ids:
        await context.bot.send_message(chat_id=chat_id, text=message)

# Lista de todos los ID de chat de los usuarios
user_chat_ids = [] # Aquí se guardan los ID de chat de los usuarios permitidos


async def obtener_id(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /obtener_id is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Tu id es: {user.id}",
        reply_markup=ForceReply(selective=True),
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("""Los comandos disponibles son:
        /start - Saluda al usuario
        /help - Muestra la ayuda
        /send_to_all - Envia un mensaje a todos los usuarios
        /obtener_id - Muestra el id del usuario
        /cobreTads - Muestra el saldo de TADS
        /avisar - Avisa a los usuarios que ya vas subiendo
        /almacenar_en_pc - Almacena un archivo en la PC
        /obtener_archivo - Obtiene un archivo de la PC
                                    """)


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    print(update.message.text)
    await update.message.reply_text("Usa el comando: /help")
    #await update.message.reply_text(update.message.text)

async def cobreTads(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /cobretads is issued."""
    result = cobretad(["", ""]) # Aquí se deben poner los datos de acceso
    result = "Vehiculo: " + result
    await update.message.reply_text(result)

async def job():
    result = cobretad(["", ""]) # Aquí se deben poner los datos de acceso
    result = "Mitsubishi (Checo): " + result

    # Enviar el resultado a todos los usuarios
    for chat_id in user_chat_ids:
        await bot.send_message(chat_id=chat_id, text=result)

#async def solicitar_ruta(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    await bot.send_message(chat_id=update.effective_chat.id, text="Indique la ruta donde se almacenará el archivo")

#async def almacenar_en_pc(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    carpetas = os.listdir(Path.home())
    mensaje = ', '.join(carpetas)
    await bot.send_message(chat_id=update.effective_chat.id, text=mensaje)
    
    await solicitar_ruta(update, context)
    print("a")
    time.sleep(10)
    ruta = update.message.text
    print(ruta)
    try:
        os.makedirs(Path.home() / ruta, exist_ok=True)
    except:
        await bot.send_message(chat_id=update.effective_chat.id, text="Ruta inválida")
        return
    await bot.send_message(chat_id=update.effective_chat.id, text="Envíe el archivo")

    file = update.message.document.get_file()
    file_path = Path.home() / ruta / file.file_path
    await file.download(file_path)

    await bot.send_message(chat_id=update.effective_chat.id, text="Archivo guardado con éxito")


#async def obtener_archivo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await bot.send_message(chat_id=update.effective_chat.id, text=str(Path.home()))
    await bot.send_message(chat_id=update.effective_chat.id, text="Indique la ruta del archivo")
    ruta = input()
    try:
        with open(Path.home() / ruta, "rb") as f:
            await bot.send_document(chat_id=update.effective_chat.id, document=f)
    except:
        await bot.send_message(chat_id=update.effective_chat.id, text="No se pudo obtener el archivo")
        return

async def almacenar_en_pc(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await bot.send_message(chat_id=update.effective_chat.id, text="Comando en construcción")

async def obtener_archivo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await bot.send_message(chat_id=update.effective_chat.id, text="Comando en construcción")

def start_schedule():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    scheduler = AsyncIOScheduler(event_loop=loop)
    scheduler.add_job(job, 'cron', hour=5)
    scheduler.start()

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()

def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token("").build() # Aquí se debe poner el token

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("send_to_all", send_to_all))
    application.add_handler(CommandHandler("obtener_id", obtener_id))
    application.add_handler(CommandHandler("cobreTads", cobreTads))
    application.add_handler(CommandHandler("avisar", avisar))
    application.add_handler(CommandHandler("almacenar_en_pc", almacenar_en_pc))
    application.add_handler(CommandHandler("obtener_archivo", obtener_archivo))


    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Start the scheduler in a separate thread
    threading.Thread(target=start_schedule).start()

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)
    


if __name__ == "__main__":
    main()