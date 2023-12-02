# Customer Service Chatbot

```markdown
# Customer Support Chatbot

This project demonstrates the process of building a customer support chatbot using Python and the Hugging Face Transformers library. The chatbot is trained on a dataset of conversation logs to understand and respond to customer inquiries.

## Installation

First, ensure that you have Python installed. Then, install the required libraries:

```bash
pip install transformers numpy pandas datasets sklearn torch logging accelerate
```

## Setting Up the Environment

The notebook automatically sets the computing device to GPU or CPU based on availability:

```python
device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(device)
```

## Data Preparation

1. **Load your dataset**:
   Load conversation data from a CSV file.

   Link to dataset: `https://huggingface.co/datasets/SantiagoPG/customer_service_chatbot`

3. **Data Preprocessing**:
   Perform text preprocessing such as lowercasing and NaN removal.

4. **Train-Test Split**:
   Split the conversation data into training and testing sets.

5. **Tokenization**:
   Tokenize the conversations for model training using `AutoTokenizer`.

## Parsing Conversations

Implement a function to separate customer inputs and agent responses from the conversation logs.

## Model Training

1. **Load Pre-Trained Model**:
   Use `AutoModelForSeq2SeqLM` from Hugging Face for the chatbot.

2. **Training Setup**:
   Configure training arguments and initialize a `Trainer` with the model and training dataset.

3. **Custom Metrics**:
   Include accuracy as a metric for model evaluation.

4. **Model Training**:
   Fine-tune the model on the conversation dataset.

## Model Saving and Uploading

Save the trained model and demonstrate how to upload it to a Hugging Face repository.

## Inference and Interaction

1. **Load the Model**:
   Instructions on how to load the model for inference.

2. **Generate Responses**:
   Implement a function to generate chatbot responses to user inputs.

3. **Interactive Testing**:
   Provide a script for interactive testing of the chatbot.

------------------------------------------------------------

```markdown
# Telegram Chatbot with AI Response Generation

This project showcases a Telegram chatbot that uses a pre-trained conversational AI model from Hugging Face's Transformers library to generate responses. The bot is designed to interact with users by processing their messages and responding with relevant answers.

## Features

- Integration with Telegram Bot API.
- AI-powered response generation using a pre-trained model.
- Commands for starting interaction and seeking help.

## Requirements

- Python 3
- `python-telegram-bot` library
- `transformers` library
- `torch` library

## Installation

Install the required Python libraries:

```bash
pip install python-telegram-bot transformers torch
```

## Usage

1. **Model and Tokenizer Initialization**:
   Load a pre-trained Seq2Seq model and tokenizer from Hugging Face.

2. **Bot Initialization**:
   Start the bot and print a message to indicate that the bot is running.

3. **Response Generation Function**:
   - Ensure the model and tokenizer are on the correct device (GPU or CPU).
   - Tokenize input text and generate a response using the model.
   - Decode the generated response to human-readable text.

4. **Telegram Bot Handlers**:
   - `start_command`: Greets the user when they start interacting with the bot.
   - `help_command`: Offers help to the user.
   - `handle_message`: Processes user messages and responds using the AI model.
   - `error`: Logs errors.

5. **Main Function**:
   - Sets up the Telegram bot with handlers for different commands and messages.
   - Starts the bot and keeps it running.

## Configuration

Replace `keys.API_KEY` with your Telegram Bot API key. You can obtain this key from the BotFather on Telegram.

## Running the Bot

Execute the script to start the bot. Interact with the bot on Telegram by sending messages or commands.

