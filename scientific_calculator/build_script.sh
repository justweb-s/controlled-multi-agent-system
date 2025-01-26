#!/bin/bash

# Script di build per il progetto Scientific Calculator

# Eseguire i test unitari
python -m unittest discover -s scientific_calculator/src/tests -p '*_test.py' > test_results.txt

# Controllo del risultato dei test
if grep -q 'FAILED' test_results.txt; then
  echo "Alcuni test non sono riusciti. Controlla test_results.txt per i dettagli."
  exit 1
else
  echo "Tutti i test sono stati superati con successo."
fi
