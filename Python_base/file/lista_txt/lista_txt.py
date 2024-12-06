lista = []

try: 
    # TODO 1: Leggere il file e caricare i numeri all'interno della lista 
    with open("/home/mattiafiore/Desktop/Esercizi_Python/Python_base/file/lista_txt/lista.txt", "r") as f: 
        
        
except: 
    # Se il file non viene trovato non aggiunge nulla
    pass


testo = """Azioni: 
1. Aggiungi elemento
2. Rimuovi elemento
3. Stampa lista
4. Salva risultato
5. Esci """

print(testo)

while True: 

    scelta = int(input("Inserire scelta: "))

    if scelta == 1: 
        # TODO 2: Chiedere un elemento e aggiungerlo alla lista
        
        
    elif scelta == 2: 
        # TODO 3: Chiedere un elemento da rimuovere
       

    elif scelta == 3: 
        # TODO 4: Stampare la lista 
        
    elif scelta == 4: 

        # TODO 5: Scrivere la lista all'interno del file 
        
    elif scelta == 5: 
        # TODO 6: Scrivere la lista all'interno del file e uscire dal ciclo while 
        
        break
    else: 
        print("Comando sbagliato riprovare")