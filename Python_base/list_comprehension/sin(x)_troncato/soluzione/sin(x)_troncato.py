from math import sin, pi

# TODO: aumentare il numero di punti su cui andare
# ad effettuare il campionamento 
n = 100
x = [(i*2*pi)/n for i in range(n)]

massimo = 0.5
# TODO: settare un valore massimo oltre il quale l'elemento della 
# lista deve prendere sempre il valore massimo 

sin_x = [min(sin(i), massimo) for i in x]

print(sin_x)