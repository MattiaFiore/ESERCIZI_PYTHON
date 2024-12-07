import os 

# Chiedere nome 
nome = input("Inserire il nome: ")
# Chiedere cognome 
cognome = input("Inserire il cognome: ")
# Chiedere eta 
eta = input("Inserire eta: ")
# Chiedere nazionalita 
nazionalita = input("Inserire nazionalita: ")

#Salvare i dati all'interno di un dizionario 
dizionario = {}
dizionario['nome'] = nome 
dizionario['cognome'] = cognome 
dizionario['eta'] = eta
dizionario['nazionalita'] = nazionalita

# Estarre current directory 
path = os.path.dirname(os.path.realpath(__file__))
print(path)

if "dati" in os.listdir(path):
    pass
else: 
    print("ciao")
    os.mkdir(path+"/dati")

with open(path+f'/dati/{nome}_{cognome}.txt', 'w') as f:
    f.write(str(dizionario))
