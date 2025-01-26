from tools import crea_file, scrivi_file, aggiungi_a_file, leggi_file, elimina_file, crea_cartella, elimina_cartella, scambia_messaggio
import streamlit as st
from Agent import create_agent_page

def initialize_session_state(agent_name):
    """
    Inizializza lo stato della sessione per un agente specifico.
    
    Args:
        agent_name (str): Nome dell'agente per cui inizializzare lo stato.
    """
    if f"{agent_name}_messages" not in st.session_state:
        st.session_state[f"{agent_name}_messages"] = []


def main():
    st.title("Due Agenti con Memoria Separata")

    # Configurazioni specifiche per ciascun agente
    agent_configurations = {
        "architetto": {
            "system_message": "Sei l'Agente Architetto: definisci i requisiti di un progetto in modo chiaro e organizzato.",
            "tools": [crea_file, elimina_file, crea_cartella, elimina_cartella]
        },
        "programmatore": {
            "system_message": "Sei l'Agente Programmatore: scrivi il codice del progetto in base ai requisiti.",
            "tools": [scrivi_file, aggiungi_a_file, leggi_file, scambia_messaggio]
        }
    }

    # Inizializza lo stato per ogni agente
    for agent_name in agent_configurations.keys():
        initialize_session_state(agent_name)

    # Crea le schede per gli agenti
    tab1, tab2 = st.tabs(["Architetto", "Programmatore"])

    with tab1:
        create_agent_page(
            agent_name="architetto",
            system_message=agent_configurations["architetto"]["system_message"],
            tools=agent_configurations["architetto"]["tools"]
        )

    with tab2:
        create_agent_page(
            agent_name="programmatore",
            system_message=agent_configurations["programmatore"]["system_message"],
            tools=agent_configurations["programmatore"]["tools"]
        )


if __name__ == "__main__":
    main()
