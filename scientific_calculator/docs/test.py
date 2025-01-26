import os

def leggi_file(percorso_file: str) -> str:
    try:
        with open(percorso_file, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"Errore durante la lettura del file: {e}"
    
if __name__ == "__main__":
    contenuto = leggi_file("Project_Requirements.md")
    print(contenuto)