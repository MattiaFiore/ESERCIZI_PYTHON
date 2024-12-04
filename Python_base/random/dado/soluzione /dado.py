from random import randint 
 
ripetizioni = 100_000

dizionario = {}

for i in range(ripetizioni): 

    #TODO 1: Generare numero random tra 1 e 6
    numero = randint(1,6)

    #TODO 2: Aggiornare il contatore
    if numero in dizionario: 
        dizionario[numero] += 1
    else: 
        dizionario[numero] = 1
    
#TODO 3: Stampare il risultato del conteggio 
print(dizionario)

lista_errori_relativi = []
valore_teorico = 1/6

for key, value in dizionario.items(): 
    #TODO 4: Calcolare l'errore relativo e aggiungerlo alla lista

    valore_misurato = value/ripetizioni
    errore_relativo = abs(( valore_misurato- valore_teorico)/valore_teorico)
    lista_errori_relativi.append(errore_relativo)

    #TODO 5: stampare l'errore in percentuale 
    print(f"Errore relativo percentuale {key}: {round(errore_relativo*100,3)}%")
