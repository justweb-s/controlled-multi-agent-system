from Routine import run_full_turn
import streamlit as st
from Utility import message_to_dict
import json

# ========= FUNZIONE GENERICA =========
def create_agent_page(agent_name, system_message, tools):
    """
    Crea una pagina di Streamlit per un agente con memoria separata e tools personalizzati.

    Args:
        agent_name (str): Il nome dell'agente da visualizzare nella UI.
        system_message (str): Il messaggio di sistema per configurare l'agente.
        tools (list): La lista di strumenti specifici per l'agente.
    """
    # Inizializza la memoria per l'agente
    if f'{agent_name}_messages' not in st.session_state:
        st.session_state[f'{agent_name}_messages'] = []

    # Interfaccia utente per l'agente
    st.subheader(f"Agente {agent_name.capitalize()}")
    user_input = st.chat_input(f"Scrivi un messaggio per l'{agent_name.capitalize()}:")
    
    if user_input:
        st.session_state[f'{agent_name}_messages'].append({"role": "user", "content": user_input})
        # Esegui il ciclo di comunicazione con l'agente
        new_msgs = run_full_turn(system_message, tools, st.session_state[f'{agent_name}_messages'])
        new_msgs_dict = [message_to_dict(m) for m in new_msgs]
        st.session_state[f'{agent_name}_messages'].extend(new_msgs_dict)

    # Mostra la conversazione
    st.write("---")
    st.write(f"**Conversazione {agent_name.capitalize()}:**")
    for msg in st.session_state[f'{agent_name}_messages']:
        role = msg.get("role", "")
        content = msg.get("content", "")
        if role == 'user':
            st.chat_message("user").write(content)
        elif role == 'assistant':
            st.chat_message("assistant").write(content)
        elif role == 'tool':
            st.chat_message("tool").write(content)
