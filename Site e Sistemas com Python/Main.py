# titulo
# input do chat
# A cada mensagem enviada:
    # mostrar a mensagem que o usuario enviou no chat
    # enviar essa mensagem para a IA responder
    # aparece na tela a resposta da IA

# streamlit - frontend e backend

import os
import streamlit as st
from openai import OpenAI

modelo = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("ChatBot com IA")  # markdown

# session_state -> é a memória do streamlit
if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []

# adicionar uma mensagem:
# st.session_state["lista_mensagens"].append(mensagem)


# Exibir o histórico de mensagens:
for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)


# variável que armazena a última mensagem do usuário:
mensagem_usuario = st.chat_input("Escreva a sua mensagem aqui")

if mensagem_usuario:
    # user -> ser humano
    # assistant -> inteligencia artificial
    st.chat_message("user").write(mensagem_usuario)
    mensagem = {"role": "user", "content": mensagem_usuario}
    st.session_state["lista_mensagens"].append(mensagem)
    
    # resposta da IA:
    try:
        resposta_modelo = modelo.chat.completions.create(
            messages=st.session_state["lista_mensagens"],
            model="gpt-4o"
        )
    
        resposta_ia = resposta_modelo.choices[0].message.content
    except Exception as e:
        resposta_ia = "Erro ao conectar com a IA: " + str(e)
    
    

    # exibir a resposta da IA na tela:
    st.chat_message("assistant").write(resposta_ia)
    mensagem_ia = {"role": "assistant", "content": resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem_ia)

    print(st.session_state["lista_mensagens"])

    
