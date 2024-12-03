from math import pi, sin, factorial

n = 10
x = [(i*2*pi)/n for i in range(n)]

#TODO: creare una lista con i valori di sin(x) utilizzando 
# la serie di taylor 

sin_x_taylor = [i - (i**3/factorial(3)) + (i**5/factorial(5)) - (i**7/factorial(7)) for i in x]

print(sin_x_taylor)