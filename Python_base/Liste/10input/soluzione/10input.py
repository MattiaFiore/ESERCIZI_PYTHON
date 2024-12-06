from statistics import mean, stdev 

n = 10
lista = []
# TODO 1: Aggiungere gli 10 elementi inseriti manualmente dall'utente 
for i in range(n): 
    lista.append(int(input("Inserisci un numero: ")))

# TODO 2: Stampare media
print(f"Media: {mean(lista)}")
# TODO 3: Stampare deviazione standard 
print(f"Stdev: {stdev(lista)}")