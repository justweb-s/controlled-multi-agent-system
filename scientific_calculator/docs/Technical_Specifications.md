# Specifiche Tecniche

## Architettura del Sistema
La Calcolatrice Scientifica sarà costruita utilizzando un'architettura modulare, consentendo di separare le diverse funzionalità e facilitando la manutenzione del codice.

## Tecnologie Utilizzate
- **Linguaggio**: Python 3.x
- **Librerie**:
  - `math`: per calcoli matematici avanzati.
  - `tkinter`: per la creazione dell'interfaccia grafica.

## Struttura del Codice
La struttura del codice avrà la seguente organizzazione:
```
src/
  main/
    calculator.py        # Logica principale della calcolatrice
    gui.py               # Interfaccia grafica (se applicabile)
  tests/
    test_calculator.py   # Test unitari per la logica della calcolatrice
```

## Gestione degli Errori
La calcolatrice deve gestire eccezioni comuni come divisione per zero e input non validi, fornendo messaggi di errore chiari all'utente.