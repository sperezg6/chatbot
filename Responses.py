from datetime import datetime

def sample_responses(input_text): 
    user_messages = str(input_text).lower()
    if user_messages in ("hola", "que onda"): 
        return "Hola! Cómo estás?"
    
    return "No te endiendo"