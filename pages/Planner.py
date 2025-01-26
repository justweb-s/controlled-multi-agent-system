from tools import crea_file, scrivi_file, aggiungi_a_file, leggi_file, elimina_file, crea_cartella, elimina_cartella, scambia_messaggio
from Routine import run_full_turn, execute_tool_call
import streamlit as st
from Utility import message_to_dict
import json

# ========= TOOLS =========
tools = [
    crea_file,
    scrivi_file,
    aggiungi_a_file,
    leggi_file,
    elimina_file,
    crea_cartella,
    elimina_cartella,
    scambia_messaggio  # Aggiungiamo la nuova funzione ai tools
]

# ========= DIVERSI PROMPT (AGENTI) =========
system_message_planner=(
    "I am the Planner Agent. "
    "Il mio compito è fornire il piano generale delle operazioni per l'intero progetto, "
    "tenendo conto degli obiettivi e dei compiti di ciascun agente. "
    "Posso essere consultato da Triage Agent (o da altri agenti) "
    "per avere una visione d'insieme e per capire l'ordine ottimale delle azioni. "
    "Dopo aver fornito le mie informazioni, passo sempre la palla al Triage Agent."
)
# ========= STREAMLIT APP =========
def main():
    st.title("Due Agenti con Memoria Separata")

    if 'planner_messages' not in st.session_state:
        st.session_state.planner_messages = []

    st.subheader("Agente Planner")
    user_input_planner = st.chat_input("Scrivi un messaggio per il Planner:")
    
    if user_input_planner:
        st.session_state.planner_messages.append({"role": "user", "content": user_input_planner})
        new_msgs = run_full_turn(system_message_planner, tools, st.session_state.planner_messages)
        new_msgs_dict = [message_to_dict(m) for m in new_msgs]
        st.session_state.planner_messages.extend(new_msgs_dict)

    st.write("---")
    st.write("**Conversazione Planner:**")
    for msg in st.session_state.planner_messages:
        role = msg.get("role", "")
        content = msg.get("content", "")
        if role == 'user':
            st.chat_message("user").write(content)
        elif role == 'assistant':
            st.chat_message("assistant").write(content)
        elif role == 'tool':
            st.chat_message("tool").write(content)

if __name__ == "__main__":
    main()
