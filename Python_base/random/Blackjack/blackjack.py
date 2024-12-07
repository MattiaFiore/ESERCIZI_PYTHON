import random 

carte = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'Jack': 10,
    'Queen': 10,
    'King': 10,
    'Ace': [1, 11] 
}

mazzo = []
# TODO 1: Generare il mazzo con 52 carte 


# TODO 2: Pescare randomicamente due carte e rimuovile dal mazzo
mano = []

print(mano)

#Print the value: 
valore = 0 

def calcola_somma(mano): 

    valori = [0]
    for carta in mano: 
        
        if carta == 'Ace':
            # TODO 3: Implementare la logica dell'asso che puo valere sia 1 che 11

        else: 
            valori = [x + carte[carta] for x in valori if x + carte[carta] <=21 ]
    
    return valori

valori = calcola_somma(mano)
print(f"Valori: {valori}")

while True: 
    scelta = input("Carta (y/n)?")
    if scelta == "y":
        # TODO 4: Pescare un'altra carta e rimuoverla dal mazzo 
        # e calcolare il punteggio 
        
    elif scelta == "n":
        #TODO 5: Stampare il punteggio ottenuto (massimo)
        
    else: 
        print("rispondere y o n")

    # TODO 6: Spiegare perche verificando che la lista sia vuota si puo determinare
    # che il giocatore ha sballato 
    if valori == []:
        print("SBALLATO")
        break
    else: 
        print(f"Valori: {valori}")
