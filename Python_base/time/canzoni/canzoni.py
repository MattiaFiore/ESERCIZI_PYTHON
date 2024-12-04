import time 
import os 

start = time.time()

path = "/home/mattiafiore/Desktop/Esercizi_Python/Python_base/time/canzoni/data"

parole = {}

for file in os.listdir(path): 
    print(f'Currently working on: {file}')

    #TODO 1: Leggi ogni file 
    with open(path+"/"+file, 'r') as f: 
        testo = 

        #TODO 2: Estrai la lista delle parole 
        lista_parole = 

        #TODO 3: Descrivi come scrivere aumentare il contatore all'interno
        # del dizionario 
        

    print(f'Fineshed file {file}')



massimo_valore = 0 
massimo_key = 0 

for key,valore in parole.items(): 
    #TODO 4: Trova il massimo usando un semplice for loop
    

end = time.time()

# TODO 5: print how much time passed and the result 
print(f'Il tempo impiegato: {}s')
print(f'La parola piu utilizzata : \'{massimo_key}\' ripetuta {massimo_valore} volte')