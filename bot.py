import os
from dotenv import load_dotenv
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


# ---------------- Streamlit UI ---------------- #
st.title("🤖 Welcome to Chatbot")
st.markdown("A Basic Project using **Google Gemini Flash** and Streamlit.")


# Load API Key
st.sidebar.title("GOOGLE API GEMEINI KEY")
GOOGLE_API_KEY = st.sidebar.text_input("Enter API KEY", type="password")

if GOOGLE_API_KEY:  
   llm = ChatGoogleGenerativeAI(
      model="gemini-1.5-flash", 
      temperature=0.7, 
      google_api_key=GOOGLE_API_KEY  # better than hardcoding
    )

prompt = PromptTemplate.from_template(
    "You are a helpful assistant. Answer this:\n{question}"
)
parser = StrOutputParser()

def chatbot(query):
    formatted_prompt = prompt.format(question=query)
    response = llm.invoke(formatted_prompt)
    return parser.parse(response.content)
 

# Chat input
if user_input := st.chat_input("Type your message..."):
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get LLM response
    ans = chatbot(user_input)
    with st.chat_message("ai"):
        st.markdown(ans)
