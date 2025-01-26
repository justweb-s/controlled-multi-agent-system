import os
import streamlit as st

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
    
def execute_code_from_file(file_name: str):
    """
    Execute Python code from a specified file.
    """
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            code = f.read()
        exec(code, {})
        return "Code executed successfully"
    except Exception as e:
        return f"Execution failed: {e}"
    

import subprocess

def esegui_file_python(percorso_file: str) -> str:
    """
    Esegue un file Python e restituisce una stringa che indica se il codice funziona o no.
    
    Args:
        percorso_file (str): Il percorso del file Python da eseguire.
        
    Returns:
        str: "funziona" se il codice è stato eseguito correttamente, "non funziona" altrimenti.
    """
    try:
        # Esegui il file utilizzando il comando python
        result = subprocess.run(
            ['python', percorso_file],  # Comando per eseguire il file Python
            stdout=subprocess.PIPE,    # Cattura l'output standard
            stderr=subprocess.PIPE     # Cattura gli errori
        )
        
        # Verifica se l'esecuzione è avvenuta senza errori (codice di ritorno 0)
        if result.returncode == 0:
            return "funziona"
        else:
            # Stampa l'errore in caso di fallimento
            print(f"Errore nell'esecuzione del file:\n{result.stderr.decode('utf-8')}")
            return "non funziona"
    except Exception as e:
        print(f"Errore durante l'esecuzione: {e}")
        return "non funziona"

    
def crea_struttura_progetto(base_path: str) -> str:
    """
    Crea la struttura di un progetto software basata su una specifica organizzazione di cartelle e file.
    
    Args:
        base_path (str): Il percorso base dove creare la struttura del progetto.

    Returns:
        str: Messaggio che indica se la struttura è stata creata con successo o se si è verificato un errore.
    
    La struttura include:
    - Cartelle principali come /docs, /src, /config, ecc.
    - File di documentazione, configurazione e script predefiniti.

    Ogni file chiave contiene un template iniziale o un'intestazione come punto di partenza.
    """
    try:
        # Creazione delle cartelle principali
        cartelle = [
            "plans",
            "/docs",
            "/src/main",
            "/src/tests",
            "/config",
            "/requirements",
            "/build",
            "/scripts",
            "/data/raw",
            "/data/processed",
            "/.github/workflows"
        ]
        for cartella in cartelle:
            crea_cartella(os.path.join(base_path, cartella))

        # Creazione dei file all'interno delle cartelle
        file_e_contenuti = {
            "/plans/piano_architetto.md": "# Piano Architetto",
            "/plans/piano_developer.md": "# Piano Developer",
            "/docs/README.md": "# Descrizione del progetto",
            "/docs/Project_Requirements.md": "# Requisiti di progetto",
            "/docs/Technical_Specifications.md": "# Specifiche tecniche",
            "/docs/UML_Diagrams.md": "# Diagrammi UML",
            "/docs/API_Documentation.md": "# Documentazione API",
            "/docs/Design_Decisions.md": "# Decisioni di design",
            "/src/tests/test_plan.md": "# Piano di test",
            "/config/config.yaml": "configurazioni: []",
            "/config/logging.yaml": "logging: []",
            "/requirements/requirements.txt": "",
            "/requirements/dev-requirements.txt": "",
            "/build/build_script.sh": "#!/bin/bash\n# Script per automatizzare la build",
            "/scripts/setup_env.sh": "#!/bin/bash\n# Script per configurare l'ambiente",
            "/scripts/data_preprocessing.py": "# Script per il preprocessing dei dati",
            "/src/tests/unit_tests.py": "# Test unitari",
            "/src/tests/integration_tests.py": "# Test di integrazione",
        }

        for file, contenuto in file_e_contenuti.items():
            percorso_file = os.path.join(base_path, file)
            crea_file(percorso_file)
            scrivi_file(percorso_file, contenuto)

        return f"Struttura del progetto creata con successo in '{base_path}'."
    except Exception as e:
        return f"Errore durante la creazione della struttura del progetto: {e}"
    
def sostituisci_testo(percorso_file: str, testo_da_sostituire: str, testo_sostitutivo: str) -> str:
    """
    Sostituisce un testo specifico in un file con un altro testo e restituisce un messaggio sul risultato.
    
    Args:
        percorso_file (str): Il percorso del file in cui eseguire la sostituzione.
        testo_da_sostituire (str): Il testo da sostituire.
        testo_sostitutivo (str): Il testo sostitutivo.
        
    Returns:
        str: Messaggio che indica se la sostituzione è stata completata o se c'è stato un errore.
    """
    try:
        # Legge il contenuto del file
        with open(percorso_file, 'r', encoding='utf-8') as file:
            contenuto = file.read()
        
        # Sostituisce il testo
        contenuto_modificato = contenuto.replace(testo_da_sostituire, testo_sostitutivo)
        
        # Salva il contenuto modificato nel file
        with open(percorso_file, 'w', encoding='utf-8') as file:
            file.write(contenuto_modificato)
        
        return "Sostituzione completata con successo!"
    except Exception as e:
        return f"Errore durante la sostituzione del testo: {e}"

