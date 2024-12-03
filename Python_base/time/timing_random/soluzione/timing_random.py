import random 
import time 


def crea_lista(n): 

    #TODO 4: completare la funzione 
    lista = [random.randint(1,100) for i in range(10**n)]
    return lista

for i in range(2,7):

    #TODO 1: Calcolare tempo di inizio
    start =  time.time()

    lista = crea_lista(i)
    #TODO 2: Calcolare il tempo di fine 
    end =  time.time()
    #TODO 3: stampare tempo impiegato 
    print(f"Tempo di esecuzione per lista lunga {10**i}")
    print(f"{round(end-start, 4)}")