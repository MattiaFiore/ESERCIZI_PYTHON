# Dado

Un dado a 6 facce, non truccato, ha per ogni possibile risultato una probabilita di $\frac{1}{6} \simeq 1.667$. Teoricamente lanciando un dado per 1000 volte dovremmo ritrovarci con una situazione del tipo: 

| Faccia | Occorrenze |
|--------|------------|
| 1      | 166,6...   |
| 2      | 166,6...   |
| 3      | 166,6...   |
| 4      | 166,6...   |
| 5      | 166,6...   |
| 6      | 166,6...   |

Cerchiamo di verificare quanto ci avviciniamo al risultato teorico. Per generare il numero random useremo: 
```python 
from random import randint 

# generare un numero casuale tra 1 e 6
numero = randint(1,6) 
```

Bisogna lanciare il dado per un totale di 1000 volte e tener conto di quante volte ogni faccia esce (preferibilmente utilizzando un dizionario). 

Una volta effettuato il verificare l'errore relativo. 

$\text{Errore relativo} = |\frac{\text{Errore misurato }-\text{valore teorico}}{\text{valore teorico}}|$

Esprimere questo valore in percentuale.

Inoltre verificare che se si aumenta il numero di ripetizioni l'errore relativo diminuisce. 

## Verifica dell'esercizio 
L'output del codice con numero di ripetizioni pare a 1_000 dovrebbe essere simile al seguente: 
```
{1: 188, 3: 158, 6: 158, 5: 162, 2: 163, 4: 171}
Errore relativo percentuale 1: 12.8%
Errore relativo percentuale 3: 5.2%
Errore relativo percentuale 6: 5.2%
Errore relativo percentuale 5: 2.8%
Errore relativo percentuale 2: 2.2%
Errore relativo percentuale 4: 2.6%
```
L'output del codice con numero di ripetizioni pare a 100_000 dovrebbe essere simile al seguente: 
```
{5: 16601, 2: 16707, 6: 16501, 3: 16851, 4: 16713, 1: 16627}
Errore relativo percentuale 5: 0.394%
Errore relativo percentuale 2: 0.242%
Errore relativo percentuale 6: 0.994%
Errore relativo percentuale 3: 1.106%
Errore relativo percentuale 4: 0.278%
Errore relativo percentuale 1: 0.238%
```