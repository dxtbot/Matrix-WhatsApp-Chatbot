# 🤖 Welcome to the Matrix WhatsApp Chatbot Experience! 🌐🔍

## Overview

Welcome to my repository! This project immerses you into the Matrix world with an AI-powered chatbot for WhatsApp. Utilizing Python, Selenium, and GPT-3, this chatbot simulates interactive and dynamic conversations similar to the Matrix vibe.

## Features 🚀

- **AI-Powered Conversations**: Dive into engaging and evolving conversations with the AI chatbot.
- **Trigger-Based Actions**: Reacts to specific words or triggers in chat messages.
- **Image Sending**: Send images in response to conversation cues.
- **Chat History Management**: Manage chat history and perform various chat-related actions.

## Getting Started 🛠️

### Prerequisites

- Python installed on your machine.
- Chrome WebDriver downloaded and configured.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/dxtbot/matrix-whatsapp-bot.git

Install dependencies:   
pip install -r requirements.txt

🚀 Dexter WhatsApp Chatbot Help Guide 🤖

Overview:
This Python script allows Dexter, the chatbot, to interact on WhatsApp Web using Selenium. Dexter uses AI-powered responses from OpenAI's GPT-3 and handles various message types, including text and images.

Functionalities:
1. Chatbot Initiation:
   - Dexter starts by loading the WhatsApp Web interface and waits for incoming messages.
   - It uses Selenium to interact with the browser and identify unread messages.

2. Message Handling:
   - Dexter reacts differently based on received messages:
       - Responds with emojis if asked to send an image or selfie.
       - Clears conversation history if requested by the user.
       - Generates a response using GPT-3 for other general messages.
       - Tracks conversation history and saves it to files.

3. OpenAI's GPT-3 Integration:
   - Dexter uses GPT-3 for generating text responses.
   - The script sends prompts to the GPT-3 API and receives AI-generated text as responses.
   - Responses are formatted, typed, and sent back to the user via the WhatsApp interface.

Keywords and Actions:
- Sending Image/Attachment Request:
   Keywords: "Heb je een foto?", "picture", "selfie", "plaatje"
   Action: Generates an image and responds with emojis.

- Clearing Conversation Request:
   Keywords: "Wis het gesprek", "wis", "Delete chat"
   Action: Clears conversation history and responds accordingly.

- Regular Chat:
   Dexter engages in conversation by responding to general messages.
   Emphasizes curiosity, emojis, and a 'smart/funny' personality.

File Management:
- `conversation_history_dexter.txt`:
   Stores conversation history.
   Command to load: `load_conversation_history()`

- `conversations_dexter.txt`:
   Records all conversations and responses.
   Command to save: `save_conversation_history()`

Support and Further Assistance:
For any issues, improvements, or new features, please contact the developer.

Note: This script requires a configured Selenium WebDriver, WhatsApp Web login, and an active OpenAI API key to function correctly.

🔗 Relevant Links:
- OpenAI: https://openai.com/
- Selenium WebDriver: https://www.selenium.dev/documentation/en/
- WhatsApp Web: https://web.whatsapp.com/

📌 Developer Information:
- Developer: [Dexter]


