# time

La libreria time e molto utile. Ecco alcune delle features piu importanti di questa libreria 

## Elenco esercizi
- [Tempo impiegato per creare lista di numeri random](./timing_random/)
- [Tempo impiegato per operare su file di testo ](./canzoni/)
## time.time()
Restituisce un float che rappresenta il numero di secondi tra oggi e il 1 Gennaio del 1970. 
```python 
import time 
current = time.time()
```
E' possibile calcolare con questo quanto tempo e passato durante l'esecuzione di un programma nel seguente modo: 
```python 
start = time.time()
# IL TUO PROGRAMMA
end = time.time()
print(f"Tempo impiegato: {round(end-start, 2)}")
```
## time.sleep()
Permette di mettere in pausa l'esecuzione di un programma 
```python
print("ciao")
time.sleep(10)
print("mondo")
```
## time.process_time()
Permette di calcolcare a differenza di time.time() quanto tempo del processore e stato utilizzato dal programma. 
Esempio 
```python 
import time 

start = time.time()
print("ciao")
time.sleep(2)
end = time.time()

print(f"Tempo impiegato: {round(end-start, 5)}")

start = time.process_time()
print("ciao")
time.sleep(2)
end = time.process_time()

print(f"Tempo impiegato: {round(end-start, 5)}")
```

Dovresti ritrovarti con un risultato simile a: 
```python 
ciao
Tempo impiegato: 2.00215
ciao
Tempo impiegato: 6e-05
```