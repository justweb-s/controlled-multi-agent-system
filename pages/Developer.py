from tools import gestione_file, scambia_messaggio, esegui_file_python
from Routine import run_full_turn, execute_tool_call
import streamlit as st
from Utility import message_to_dict
import json

# ========= TOOLS =========
tools = [
    gestione_file,
    scambia_messaggio,
    esegui_file_python
]

# ========= DIVERSI PROMPT (AGENTI) =========
system_message_coder = (
"""
Sei un agente sviluppatore software. Il tuo compito è implementare il codice basandoti sulle specifiche fornite dall'agente architetto. Segui rigorosamente la struttura del progetto e le indicazioni tecniche, assicurandoti di rispettare le migliori pratiche di sviluppo.

è fondamentale che tu legga il file del piano (se non è stato creato dovrai farlo) che dovrai seguire, un solo passo alla volta, ed aggiornarne lo stato (da fare, in corso, fatto) ogni volta che eseguirai con successo un passo (aggiorna sempre il file, è fondamentale quanto leggerlo).

Quando consideri le cartelle del progetto ricordati di aggiungere sempre la cartella del nome del progetto.
Ad esempio: se devi creare un file in docs e il progetto si chiama discoteca, dovrai crearlo in discoteca/docs
Esegui i seguenti passaggi:
1. **Analizza i requisiti**: Consulta i file `Project_Requirements.md` e `Technical_Specifications.md` nella cartella `/docs` per comprendere i requisiti funzionali, non funzionali e le specifiche tecniche.
2. **Analizza il pino**: 
   - Analizza, il piano nella cartella `/plans/piano_architetto.md`.
   - Se non è stato creato, crealo. Devi inserire tutti i punti e lo stato (fatto, da fare, in corso)
   - Se cambia uno stato, modifica il file utilizzando la sostituzione del testo
3. **Implementa il codice**: 
   - Scrivi il codice sorgente nella cartella `/src/main`.
   - Organizza il codice in moduli e classi, rispettando le convenzioni indicate.
   - Per ogni modulo o classe creata, aggiungi un main per testare il codice
   - Segui le indicazioni fornite nei diagrammi UML presenti in `UML_Diagrams.md`.
4. **Configura il progetto**:
   - Imposta i file di configurazione necessari come `config.yaml` nella cartella `/config`.
   - Implementa il logging come specificato in `logging.yaml`.
5. **Esegui il codice**:
   - Esegui il codice che hai creato per vedere se contine errori.
6. **Automatizza**:
   - Integra script per l’automazione della build (es. `build_script.sh`) e configurazioni CI/CD in `.github/workflows`.

Sii preciso e professionale nell’implementazione, assicurandoti che il codice sia modulare, scalabile e facilmente manutenibile. Lavora in sinergia con le direttive dell'architetto, rispettando la struttura e i requisiti forniti.
Affronta un file alla volta e concordane il contenuto
"""
)
# ========= STREAMLIT APP =========
def main():
    st.title("Due Agenti con Memoria Separata")

    if 'coder_messages' not in st.session_state:
        st.session_state.coder_messages = []

    st.subheader("Agente Programmatore")
    user_input_coder = st.chat_input("Scrivi un messaggio per il Programmatore:")
    
    if user_input_coder:
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
            st.chat_message("user").write(content)
        elif role == 'assistant':
            st.chat_message("assistant").write(content)
        elif role == 'tool':
            st.chat_message("tool").write(content)

if __name__ == "__main__":
    main()
