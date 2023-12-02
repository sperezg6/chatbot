import Constants as keys
from telegram.ext import *
import Responses as r 
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, Trainer
import torch

model = AutoModelForSeq2SeqLM.from_pretrained('SantiagoPG/chatbot_customer_service')
tokenizer = AutoTokenizer.from_pretrained("Kaludi/Customer-Support-Assistant-V2")
print("Bot started...")

def generate_response(input_text):
    # Asegúrate de que el modelo y el tokenizador estén en el dispositivo correcto (GPU o CPU)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)

    # Tokeniza el texto de entrada: convierte el texto en un formato que el modelo pueda entender
    input_ids = tokenizer.encode(input_text, return_tensors="pt").to(device)

    # Genera una respuesta usando el modelo
    output = model.generate(input_ids)

    # Decodifica la respuesta generada de nuevo a texto legible por humanos
    response = tokenizer.decode(output[0], skip_special_tokens=True)

    return response


def start_command(update, context): 
    update.message.reply_text("Ask me something!")

def help_command(update, context): 
    update.message.reply_text("How can I help you?")

def handle_message(update, context): 
    text = str(update.message.text).lower()
    response = generate_response(text)

    update.message.reply_text(response)

def error(update, context): 
    print(f"Update {update} caused error {context.error}")

def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()