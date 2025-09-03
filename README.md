🤖 Gemini Chatbot with Streamlit
A simple chatbot built using Google Gemini LLM (gemini-1.5-flash), LangChain, and Streamlit.
This project demonstrates how to integrate an LLM into a web app, with a sidebar API key loader and a chat-style interface.

📌 Features
Load Google Gemini API key via Streamlit sidebar (no hardcoding needed)
Chat interface with user/assistant chat bubbles
Powered by LangChain and Google Generative AI
Simple UI built using Streamlit

🛠️ Installation
Clone this repository and move into the project folder:
git clone https://github.com/Kain2503/QnA-Chatbot-with-LLM.git
cd QnA-Chatbot-with-LLM

Install dependencies:
pip install -r requirements.txt

▶️ Usage
Run the Streamlit app:
streamlit run main.py

Then open your browser at http://localhost:8501.

🔑 API Key Setup
Go to Google AI Studio
Generate an API key.
Copy it.
Paste it into the Streamlit sidebar when running the app.
