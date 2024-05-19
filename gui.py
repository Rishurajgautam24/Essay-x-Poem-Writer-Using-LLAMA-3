import requests
import streamlit as st

def get_openai_response(input_text):
    response = requests.post(
        "http://localhost:8000/essay/invoke",
        json={'input': {'topic': input_text}}
    )
    return response.json()['output']

def get_ollama_response(input_text):
    response = requests.post(
        "http://localhost:8000/poem/invoke",
        json={'input': {'topic': input_text}}
    )
    return response.json()['output']


# Sidebar with options
option = st.sidebar.radio("Choose an option", ("Essay writer", "Poem writer"))

if option == "Essay writer":
    st.title('Essay Generator with LLAMA2 API')
    input_text = st.text_input("Write an essay on")
    if input_text:
        st.write(get_openai_response(input_text))

elif option == "Poem writer":
    st.title('Poem Generator with LLAMA2 API')
    input_text1 = st.text_input("Write a poem on")
    if input_text1:
        st.write(get_ollama_response(input_text1))
