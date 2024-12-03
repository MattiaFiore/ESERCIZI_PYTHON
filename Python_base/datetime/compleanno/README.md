# Compleanno 
In questo esercizio bisogna chiedere all'utente tramite input il giorno del suo compleanno e restituirgli quanti giorni, ore e secondi mancano a tale data. 
Per far questo bisogna utilizzare la libreria datetime di python. 

Cose da fare: 

1. Chiedere il mese
2. Chiedere il giorno 
3. Ottenere datetime.date di oggi 
4. Calcolare se bisogna effettuare il conto l'anno attuale o con il porssimo
5. Impostare l'anno del compleanno  
6. Effettuare la differenza tra il giorno del suo compleanno e oggi 
7. Restituire il risultato 


Per calcolare il giorno di oggi utilizzare datetime.date.today()

``` python 
from datetime import date

oggi = date.today()
```

## Verifica della soluzione 

La verifica va effettuata a mano dato che il risultato del codice cambiera in base al momento in cui viene eseguito. 