
from math import sin, pi

n = 10
x = [(i*2*pi)/n for i in range(n)]
print(x)
# TODO: creare una lista con i valori di sin(x)
# usando i valori di x 

sin_x = [sin(i) for i in x]

print(sin_x)