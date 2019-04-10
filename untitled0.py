import numpy as np
a=input()
w=int(input('Podaj liczby:'))
lista=np.zeros(w)
for i in range(len(lista)):
    for i in range(len(lista)-1):
        if lista[i] > lista[i+1]:
            x= lista[i+1]
            lista[i+1] = lista[i]
            lista[i]=x
                
print(lista)