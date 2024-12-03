# sin(x)
In questo esercizio bisogna calcolare i valori della funzione $sin(x)$. Bisogna calcolare i valori tra 0 e $2\pi$. Per risolvere questo esercizio bisogna usare le list comprehension. 
Il codice calcola gia i valori di x, campionando 10 punti tra 0 e $2\pi$.
```python
n = 10
x = [(i*2*pi)/n for i in range(n)]
```
Il cui risultato risulta
```
[0.0, 0.6283185307179586, 1.2566370614359172, 1.8849555921538759, 2.5132741228718345, 3.141592653589793, 3.7699111843077517, 4.39822971502571, 5.026548245743669, 5.654866776461628]
```

## Verifica della soluzione 
Il codice deve avere il seguente output 
```
[0.0, 0.5877852522924731, 0.9510565162951535, 0.9510565162951536, 0.5877852522924732, 1.2246467991473532e-16, -0.587785252292473, -0.9510565162951535, -0.9510565162951536, -0.5877852522924734]
```