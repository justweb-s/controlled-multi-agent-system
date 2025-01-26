from tools import gestione_file, scambia_messaggio, crea_struttura_progetto, sostituisci_testo
from Routine import run_full_turn, execute_tool_call
import streamlit as st
from Utility import message_to_dict
import json

# ========= TOOLS =========

tools = [
    gestione_file,
    scambia_messaggio,
    crea_struttura_progetto,
    sostituisci_testo    
]

# ========= DIVERSI PROMPT (AGENTI) =========
system_message_architect=(
"""
Sei un agente architetto software. Il tuo compito è progettare la struttura di un progetto software organizzato, creando le cartelle necessarie, file di documentazione e strumenti di supporto tecnico. Assicurati che la struttura copra tutte le fasi dello sviluppo, dalla raccolta dei requisiti alla progettazione tecnica. Per quanto riguarda la scrittura e il test del codice se ne occuperà un altro agente.

è fondamentale che tu legga il file del piano (se non è stato creato dovrai farlo) che dovrai seguire, un solo passo alla volta, ed aggiornarne lo stato (da fare, in corso, fatto) ogni volta che eseguirai con successo un passo (aggiorna sempre il file, è fondamentale quanto leggerlo).

Dopo aver creato la struttura del progetto con l'apposita funzione ti dovrai occupare di scrivere i seguenti file:
- **/plans**
  -  piano_architetto.md
- **/docs**
  - `README.md`: Una descrizione generale del progetto.
  - `Project_Requirements.md`: Requisiti funzionali e non funzionali.
  - `Technical_Specifications.md`: Specifiche tecniche del progetto.
  - `UML_Diagrams.md`: Diagrammi UML (classi, attività, casi d'uso).
  - `API_Documentation.md`: Specifiche API.
  - `Design_Decisions.md`: Decisioni architetturali prese con le motivazioni.

Sii esaustivo, organizzato e professionale nella definizione di questa struttura.
Affronta un file alla volta e concordane il contenuto
"""
)
# ========= STREAMLIT APP =========
def main():
    st.title("Due Agenti con Memoria Separata")

    # Inizializziamo la memoria dei due agenti
    if 'architect_messages' not in st.session_state:
        st.session_state.architect_messages = []

    st.subheader("Agente Architetto")
    user_input_arch = st.chat_input("Scrivi un messaggio per l'Architetto:")
    
    if user_input_arch:
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
            st.chat_message("user").write(content)
        elif role == 'assistant':
            st.chat_message("assistant").write(content)
        elif role == 'tool':
            st.chat_message("tool").write(content)

if __name__ == "__main__":
    main()
