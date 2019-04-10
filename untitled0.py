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
                
<<<<<<< HEAD
print(lista)
=======
            list1=[2+x*9 for x in range(0,int(tablica[-10]))]
            list2=[3+x*9 for x in range(0,int(tablica[-10]))]
            list3=[4+x*9 for x in range(0,int(tablica[-10]))]
            tab[0].append(tablica[x] for x in list1)
            tab[1].append(tablica[x] for x in list2)
            tab[2].append(tablica[x] for x in list3)
            tab[0]=list(tab[0][0])
            tab[1]=list(tab[1][0])
            tab[2]=list(tab[2][0])
            if files[file][files[file].find('gold'):]!='2':
                pliki[files[file][files[file].find('gold'):]]=tab


for key in list(pliki.keys()):
    if 'soln' not in key:
        origin.append(key)
    else:
        soln.append(key)
    
for key in origin:
    print('Origin:',key)
    print()
    for key2 in soln:
        if key[5:key[5:].find('_')+5]==key2[10:key2[10:].find('_')+10]:
            print('Soln:', '\t', key2,'\t')
            print('\t',round(porownanie(pliki[key],pliki[key2]),4))
            
    print('\n')
>>>>>>> parent of 5e6327f... Final_v1.1
