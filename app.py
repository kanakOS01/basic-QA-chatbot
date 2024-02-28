import os
import streamlit as st

from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain_openai import ChatOpenAI

# from dotenv import load_dotenv
# load_dotenv()

st.set_page_config(page_title="Conversational Q&A ChatBot")
st.header("Chat here")

chatllm = ChatOpenAI(temperature=0.5, openai_api_key=os.environ['API_KEY'])

def get_openai_response(question):
    st.session_state['flowmessages'].append(HumanMessage(content=question))
    
    answer = chatllm.invoke(st.session_state['flowmessages'])
    st.session_state['flowmessages'].append(AIMessage(content=answer.content))

    return answer.content

if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages'] = [
        SystemMessage(content="You are an AI chatbot. Help the user with anything it wants.")
    ]

user_input = st.text_input("Input: ")
submit = st.button("Submit")
response = get_openai_response(user_input)

if submit:
    st.subheader("Response: ")
    st.info(response)