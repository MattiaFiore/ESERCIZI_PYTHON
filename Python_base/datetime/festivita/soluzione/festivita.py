from datetime import date 


def calcola_differenza(oggi, giorno):

    #TODO 3: calcolare anno
    if oggi.month > giorno.month: 
        giorno = date(oggi.year + 1, giorno.month, giorno.day)
    elif oggi.month == giorno.month and oggi.day >= giorno.day: 
        giorno = date(oggi.year + 1, giorno.month, giorno.day)
    else: 
        giorno = date(oggi.year, giorno.month, giorno.day)

    
    #TODO 4: Calcolare differenza di tempo 
    tempo = giorno - oggi
    print(tempo)
    

#TODO 1: calcolare giorno attuale 
oggi = date.today()

#TODO 2: Inserire giorno e giorno.month delle festivita
halloween = date(year = 1, month = 10, day = 31)
natale = date(year = 1, month = 12, day = 25)
capodanno = date(year = 1, month = 12, day = 31)
ferragosto = date(year = 1, month = 9, day = 15)

festivita = [halloween, natale, capodanno, ferragosto]

for giorno in festivita: 
    print(f'Per {giorno} mancano: ')
    calcola_differenza(oggi, giorno)

