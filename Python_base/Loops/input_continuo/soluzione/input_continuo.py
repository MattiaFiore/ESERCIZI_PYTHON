
lista = []
# TODO 1: Deciidi che loop utilizzare in modo che il loop 
# si interrompa quando viene inserito la stringa vuota in input. 

while True: 
    parola = input("Inserisci una parola: ")
    if parola == "":
        break
    lista.append(parola)

print(lista)
    