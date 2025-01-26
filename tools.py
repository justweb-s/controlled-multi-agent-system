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
        os.makedirs(percorso_cartella, exist_ok=True)
        print(f"Cartella creata: {percorso_cartella}")  # Messaggio di debug
        return f"Cartella '{percorso_cartella}' creata con successo."
    except Exception as e:
        print(f"Errore durante la creazione della cartella {percorso_cartella}: {e}")
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
            "docs",
            "src/main",
            "src/tests",
            "config",
            "requirements",
            "build",
            "scripts",
            "data/raw",
            "data/processed",
            ".github/workflows"
        ]
        for cartella in cartelle:
            percorso_completo = os.path.join(base_path, cartella)  # Usa il percorso base
            os.makedirs(percorso_completo, exist_ok=True)  # Crea la cartella
            print(f"Cartella creata: {percorso_completo}")  # Debug

        # Creazione dei file all'interno delle cartelle
        file_e_contenuti = {
            "plans/piano_architetto.md": "# Piano Architetto",
            "plans/piano_developer.md": "# Piano Developer",
            "docs/README.md": "# Descrizione del progetto",
            "docs/Project_Requirements.md": "# Requisiti di progetto",
            "config/config.yaml": "configurazioni: []",
        }

        for file, contenuto in file_e_contenuti.items():
            percorso_file = os.path.join(base_path, file)  # Usa il percorso base
            with open(percorso_file, 'w', encoding='utf-8') as f:
                f.write(contenuto)
            print(f"File creato: {percorso_file}")  # Debug

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


def gestione_file(azione: str, percorso: str, contenuto: str = "") -> str:
    """
    Gestisce operazioni sui file e cartelle come creazione, scrittura, lettura, eliminazione, ecc.
    
    Args:
        azione (str): L'azione da eseguire (crea_file, scrivi_file, aggiungi_a_file, leggi_file,
                      elimina_file, crea_cartella, elimina_cartella).
        percorso (str): Il percorso del file o della cartella.
        contenuto (str, opzionale): Il contenuto da scrivere o aggiungere (richiesto solo per scrittura o aggiunta).
        
    Returns:
        str: Messaggio che descrive il risultato dell'operazione.
    """
    try:
        if azione == "crea_file":
            with open(percorso, 'w'):
                pass
            return f"File '{percorso}' creato con successo."
        
        elif azione == "scrivi_file":
            with open(percorso, 'w', encoding='utf-8') as f:
                f.write(contenuto)
            return f"Testo scritto con successo nel file '{percorso}'."
        
        elif azione == "aggiungi_a_file":
            with open(percorso, 'a', encoding='utf-8') as f:
                f.write(contenuto)
            return f"Testo aggiunto con successo al file '{percorso}'."
        
        elif azione == "leggi_file":
            with open(percorso, 'r', encoding='utf-8') as f:
                return f.read()
        
        elif azione == "elimina_file":
            if os.path.exists(percorso):
                os.remove(percorso)
                return f"File '{percorso}' eliminato con successo."
            else:
                return f"Il file '{percorso}' non esiste."
        
        elif azione == "crea_cartella":
            if not os.path.exists(percorso):
                os.mkdir(percorso)
                return f"Cartella '{percorso}' creata con successo."
            else:
                return f"La cartella '{percorso}' esiste già."
        
        elif azione == "elimina_cartella":
            if os.path.exists(percorso):
                os.rmdir(percorso)
                return f"Cartella '{percorso}' eliminata con successo."
            else:
                return f"La cartella '{percorso}' non esiste."
        
        else:
            return "Azione non riconosciuta. Specifica un'azione valida."
    
    except Exception as e:
        return f"Errore durante l'operazione '{azione}': {e}"

if __name__ == "__main__":
    base_path = os.path.abspath("progetto1")
    print(f"Creazione struttura in: {base_path}")
    risultato = crea_struttura_progetto(base_path)
    print(risultato)


