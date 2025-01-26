import streamlit as st
import os
import json
from openai import OpenAI
from pydantic import BaseModel
from typing import Optional
from Utility import function_to_schema

# ========= UTILITY PER CONVERTIRE OGGETTI A DIZIONARI =========
def message_to_dict(msg):
    """
    Converte un messaggio (es. ChatCompletionMessage) in dizionario.
    """
    if isinstance(msg, dict):
        return msg
    return {
        "role": getattr(msg, "role", None),
        "content": getattr(msg, "content", None),
        "tool_calls": getattr(msg, "tool_calls", None),
    }

# ========= CODICE ORIGINALE (LOGICA INVARIATA) =========
client = OpenAI()

def run_full_turn(system_message, tools, messages):
    num_init_messages = len(messages)
    messages = messages.copy()

    while True:
        tool_schemas = [function_to_schema(tool) for tool in tools]
        tools_map = {tool.__name__: tool for tool in tools}

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "system", "content": system_message}] + messages,
            tools=tool_schemas or None,
        )
        message = response.choices[0].message
        messages.append(message)

        if message.content:
            print("Assistant:", message.content)

        if not message.tool_calls:
            break

        for tool_call in message.tool_calls:
            result = execute_tool_call(tool_call, tools_map)
            result_message = {
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": result,
            }
            messages.append(result_message)

    return messages[num_init_messages:]

def execute_tool_call(tool_call, tools_map):
    name = tool_call.function.name
    args = json.loads(tool_call.function.arguments)
    print(f"Assistant: {name}({args})")
    return tools_map[name](**args)

def crea_file(percorso_file: str) -> str:
    try:
        with open(percorso_file, 'w'):
            pass
        return f"File '{percorso_file}' creato con successo."
    except Exception as e:
        return f"Errore durante la creazione del file: {e}"

def scrivi_file(percorso_file: str, testo: str) -> str:
    try:
        with open(percorso_file, 'w', encoding='utf-8') as f:
            f.write(testo)
        return f"Testo scritto con successo nel file '{percorso_file}'."
    except Exception as e:
        return f"Errore durante la scrittura del file: {e}"

def aggiungi_a_file(percorso_file: str, testo: str) -> str:
    try:
        with open(percorso_file, 'a', encoding='utf-8') as f:
            f.write(testo)
        return f"Testo aggiunto con successo al file '{percorso_file}'."
    except Exception as e:
        return f"Errore durante l'aggiunta di testo al file: {e}"

def leggi_file(percorso_file: str) -> str:
    try:
        with open(percorso_file, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"Errore durante la lettura del file: {e}"

def elimina_file(percorso_file: str) -> str:
    try:
        if os.path.exists(percorso_file):
            os.remove(percorso_file)
            return f"File '{percorso_file}' eliminato con successo."
        else:
            return f"Il file '{percorso_file}' non esiste."
    except Exception as e:
        return f"Errore durante l'eliminazione del file: {e}"

def crea_cartella(percorso_cartella: str) -> str:
    try:
        if not os.path.exists(percorso_cartella):
            os.mkdir(percorso_cartella)
            return f"Cartella '{percorso_cartella}' creata con successo."
        else:
            return f"La cartella '{percorso_cartella}' esiste già."
    except Exception as e:
        return f"Errore durante la creazione della cartella: {e}"

def elimina_cartella(percorso_cartella: str) -> str:
    try:
        if os.path.exists(percorso_cartella):
            os.rmdir(percorso_cartella)
            return f"Cartella '{percorso_cartella}' eliminata con successo."
        else:
            return f"La cartella '{percorso_cartella}' non esiste."
    except Exception as e:
        return f"Errore durante l'eliminazione della cartella: {e}"

def scambia_messaggio(agente_destinatario: str, contenuto: str) -> str:
    """
    Permette a un agente di inviare un messaggio all'altro agente.
    """
    try:
        if agente_destinatario == "architetto":
            st.session_state.architect_messages.append({"role": "user", "content": contenuto})
            return f"Messaggio inviato all'architetto: {contenuto}"
        elif agente_destinatario == "programmatore":
            st.session_state.coder_messages.append({"role": "user", "content": contenuto})
            return f"Messaggio inviato al programmatore: {contenuto}"
        else:
            return "Errore: destinatario non valido. Usare 'architetto' o 'programmatore'."
    except Exception as e:
        return f"Errore durante lo scambio del messaggio: {e}"

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
system_message_architect = "Sei l'Agente Architetto: definisci i requisiti di un progetto in modo chiaro e organizzato."
system_message_coder = "Sei l'Agente Programmatore: scrivi il codice del progetto in base ai requisiti."

# ========= STREAMLIT APP =========
def main():
    st.title("Due Agenti con Memoria Separata")

    # Inizializziamo la memoria dei due agenti
    if 'architect_messages' not in st.session_state:
        st.session_state.architect_messages = []
    if 'coder_messages' not in st.session_state:
        st.session_state.coder_messages = []

    # Layout a colonne per i due agenti
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Agente Architetto")
        user_input_arch = st.text_input("Messaggio per l'Architetto:")
        if st.button("Invia al Architetto"):
            st.session_state.architect_messages.append({"role": "user", "content": user_input_arch})
            new_msgs = run_full_turn(system_message_architect, tools, st.session_state.architect_messages)
            new_msgs_dict = [message_to_dict(m) for m in new_msgs]
            st.session_state.architect_messages.extend(new_msgs_dict)

        st.write("---")
        st.write("**Conversazione Architetto:**")
        for msg in st.session_state.architect_messages:
            role = msg.get("role", "")
            content = msg.get("content", "")
            if role == 'user':
                st.write(f"**Utente**: {content}")
            elif role == 'assistant':
                st.write(f"**Architetto**: {content}")
            elif role == 'tool':
                st.write(f"**Tool**: {content}")

    with col2:
        st.subheader("Agente Programmatore")
        user_input_coder = st.text_input("Messaggio per il Programmatore:")
        if st.button("Invia al Programmatore"):
            st.session_state.coder_messages.append({"role": "user", "content": user_input_coder})
            new_msgs = run_full_turn(system_message_coder, tools, st.session_state.coder_messages)
            new_msgs_dict = [message_to_dict(m) for m in new_msgs]
            st.session_state.coder_messages.extend(new_msgs_dict)

        st.write("---")
        st.write("**Conversazione Programmatore:**")
        for msg in st.session_state.coder_messages:
            role = msg.get("role", "")
            content = msg.get("content", "")
            if role == 'user':
                st.write(f"**Utente**: {content}")
            elif role == 'assistant':
                st.write(f"**Programmatore**: {content}")
            elif role == 'tool':
                st.write(f"**Tool**: {content}")

if __name__ == "__main__":
    main()
