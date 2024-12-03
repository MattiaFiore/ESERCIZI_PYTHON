# sin(x) Taylor 

Consiste nel calcolare il valore della funzione $sin(x)$ tramite approssimazione di Taylor. 
Infatti, e possibile scomporre una funzione in una somma di polinomi che all'aumentare del grado riescono ad approssimare meglio il comportamento della funzione. 
In questo caso bisogna utilizzare i primi 4 termini della serie di Taylor per la funzione seno. 

$sin(x) \simeq x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} $

$n!$ e una notazione matematica chiamata fattoriale che esprime la seguente operazione

$n! = 1 \cdot 2 \cdot ... \cdot n $

In python la funzione fattoriale e presente nel modulo math
```python 
from math import factorial
```
## Verifica della soluzione
Il codice deve avere il seguente output
```
[0.0, 0.5877852103843443, 0.951035288276224, 0.9502548158759504, 0.5773680514538426, -0.07522061590362306, -0.9615454714942988, -2.383637293463014, -5.486379937841956, -12.984325443484256]
```
Come si puo notare rispetto al risultato dell'esercizion che utilizza la funzione built-in i risultati variano all'inizio leggermente e all'aumentare del valore di x in modo sostanziale. 
```
[0.0, 0.5877852522924731, 0.9510565162951535, 0.9510565162951536, 0.5877852522924732, 1.2246467991473532e-16, -0.587785252292473, -0.9510565162951535, -0.9510565162951536, -0.5877852522924734]
```