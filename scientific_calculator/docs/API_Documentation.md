# Documentazione API

Questa sezione fornisce dettagli sulle API utilizzate nel progetto e sulla struttura degli endpoint (se applicabile).

## API Principali
Anche se il progetto attuale è principalmente una calcolatrice da riga di comando o GUI, è possibile implementare un'API REST in futuro. Ecco una proposta per le possibili API:

### Endpoint
1. **`POST /calculate`**
   - **Descrizione**: Esegue un calcolo basato sull'input dell'utente.
   - **Request Body**:
     ```json
     {
       "expression": "2 + 2"
     }
     ```
   - **Response**:
     ```json
     {
       "result": 4
     }
     ```

2. **`GET /operations`**
   - **Descrizione**: Restituisce un elenco delle operazioni matematiche supportate.
   - **Response**:
     ```json
     {
       "operations": ["add", "subtract", "multiply", "divide", "sin", "cos", "tan"]
     }
     ```

## Autenticazione
Se l'API richiede autenticazione, specificare qui il metodo (es. token JWT).

## Error Handling
Descrivere i codici di stato e i messaggi di errore restituibili.