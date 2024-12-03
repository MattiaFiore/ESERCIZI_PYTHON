from datetime import date


#TODO 1: Chiedere il mese 
mese = int(input('Inserire mese del compleanno: '))

#TODO 2: Chiedere il giorno 
giorno = int(input('Inserire giorno del compleanno: '))

#TODO 3: Ottenere il giorno di oggi 
oggi = date.today()

#TODO 4-5: Calcolare se bisogna effettuare il conto con l'anno 
# attuale o con il successivo 

if oggi.month > mese: 
    compleanno = date(oggi.year + 1, mese, giorno)

elif oggi.month == mese and oggi.day >= giorno: 
    compleanno = date(oggi.year + 1, mese, giorno)
else: 
    compleanno = date(oggi.year, mese, giorno)

#TODO 6: effettuare la differenza tra compleanno e oggi
tempo = compleanno - oggi

#TODO 7: restituire il risultato 
print(tempo)