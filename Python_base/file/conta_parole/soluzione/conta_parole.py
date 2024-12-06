
from statistics import mean 

try: 
    #TODO 1: Aprire il file e leggerlo 
    with open("/home/mattiafiore/Desktop/Esercizi_Python/Python_base/file/conta_parole/fairlies.txt", 'r') as f: 
        testo = f.read()
except Exception as e: 
    print(f'Somthing wrong happened: {e}')


removed = ""
# TODO 2: Rimuovere la punteggiatura
for carattere in testo: 
    if carattere not in ",.:;!?\"\'-":
        removed += carattere

# TODO 3: Creare una lista con le parole separate
parole = removed.split()
# TODO 4: Stampare il numero di parole 
print(f"Numero di parole: {len(parole)}")

# TODO 5: creare una lista contente la lunghezza di tutte le 
# parole presenti in removed 
lista_lunghezze = []
for i in parole: 
    lista_lunghezze.append(len(i))

# TODO 6: stampare la media della lungehzza delle parole 
# Utilizzare la libreria statistics 
print(f"Media lunghezza parole: {mean(lista_lunghezze)}")