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
for i in range(4):
    mazzo += carte.keys()

# Prima Mano 
mano = []
mano.append(mazzo.pop(random.randint(0,len(mazzo)-1)))
mano.append(mazzo.pop(random.randint(0,len(mazzo)-1)))
print(mano)

#Print the value: 
valore = 0 

def calcola_somma(mano): 

    valori = [0]
    for carta in mano: 
        
        if carta == 'Ace':
            valori = [x + 1 for x in valori if x + 1 <= 21] + [x + 11 for x in valori if x + 11 <= 21]

        else: 
            valori = [x + carte[carta] for x in valori if x + carte[carta] <=21 ]
    
    return valori

valori = calcola_somma(mano)
print(f"Valori: {valori}")

while True: 
    scelta = input("Carta (y/n)?")
    if scelta == "y":
        mano.append(mazzo.pop(random.randint(0, len(mazzo)-1)))
        print(mano)
        valori = calcola_somma(mano)
    elif scelta == "n":
        print(max(valori))
        break
    else: 
        print("rispondere y o n")

    if valori == []:
        print("SBALLATO")
        break
    else: 
        print(f"Valori: {valori}")

    



