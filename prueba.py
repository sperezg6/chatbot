from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, Trainer
import torch

model = AutoModelForSeq2SeqLM.from_pretrained('SantiagoPG/chatbot_customer_service')
tokenizer = AutoTokenizer.from_pretrained("Kaludi/Customer-Support-Assistant-V2")


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

def main(): 
    user_input= "Wheres my order"
    response = generate_response(user_input)
    print("Chatbot: ", response)

main()