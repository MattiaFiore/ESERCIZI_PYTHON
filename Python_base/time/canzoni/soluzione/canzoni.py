import time 
import os 

start = time.time()

path = "/home/mattiafiore/Desktop/Esercizi_Python/Python_base/time/canzoni/data"

parole = {}

for file in os.listdir(path): 
    print(f'Currently working on: {file}')

    #TODO : Read each file 
    with open(path+"/"+file, 'r') as f: 
        testo = f.read()
        lista_parole = testo.split()

        #TODO : Descrivi come scrivere aumentare il contatore all'interno
        # del dizionario 
        for parola in lista_parole: 

            if parola in parole: 
                parole[parola] += 1
            else: 
                parole[parola] = 1 
        

    print(f'Fineshed file {file}')


#TODO : Trova il massimo usando un semplice for loop
massimo_valore = 0 
massimo_key = 0 

for key,valore in parole.items(): 
    if valore > massimo_valore:
        massimo_key = key 
        massimo_valore = valore

end = time.time()

# TODO : print how much time passed and the result 
print(f'Il tempo impiegato: {round(end-start, 4)}s')
print(f'La parola piu utilizzata : \'{massimo_key}\' ripetuta {massimo_valore} volte')