import streamlit as st
import requests

# URL do servidor Rasa
RASA_URL = 'http://localhost:5005/webhooks/rest/webhook'

# Função para enviar mensagens ao Rasa
def enviar_mensagem(message, sender='user'):
    response = requests.post(RASA_URL, json={'sender': sender, 'message': message})
    return response.json()

# Configuração da página
st.set_page_config(page_title="Chatbot Lady Gaga", page_icon="🎤")

# Exibição do título
st.title("🎤 Chatbot Lady Gaga")
st.write("Olá! Sou seu assistente musical. Como posso ajudá-lo?")

# Inicialização do histórico de mensagens
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Exibição das mensagens anteriores
for msg in st.session_state.messages:
    if msg['role'] == 'user':
        st.chat_message("user").markdown(msg['content'])
    else:
        st.chat_message("assistant").markdown(msg['content'])

# Entrada de texto do usuário
user_input = st.chat_input("Digite sua mensagem...")

# Envio da mensagem ao Rasa e exibição da resposta
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.spinner("Pensando..."):
        bot_response = enviar_mensagem(user_input)
        st.chat_message("user").markdown(user_input)
        for message in bot_response:
            if 'text' in message:
                st.session_state.messages.append({"role": "assistant", "content": message['text']})
                st.chat_message("assistant").markdown(message['text'])
