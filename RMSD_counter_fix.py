import os
import math
from glob import glob

def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]


def kk(dir, lis=[]):
    b = get_immediate_subdirectories(dir)
    if b:
        for i in b:
            lis.append(dir + '/' + i)
        for l in b:
            lis = kk(dir + '/' + l, lis)
    else:
        return lis
    return lis


def porownanie(tab1, tab2):
    suma = []

    for col in range(len(tab1)):
        for elem in range(len(tab1[col])):
            tab1[col][elem] = float(tab1[col][elem])
            tab2[col][elem] = float(tab2[col][elem])
            suma.append((tab1[col][elem] - tab2[col][elem]) * (tab1[col][elem] - tab2[col][elem]))
    odp = math.sqrt(3 * sum(suma) / len(suma))

    return odp


a = 'TRIPOS>ATOM'
b = 'TRIPOS>BOND'
pliki = {}
origin = []
soln = []
files = []
start_dir = os.getcwd()
pattern = "*.mol2"

for dir in kk(start_dir):
    files.extend(glob(os.path.join(dir,pattern)))

if True:
    for file in range(len(files)):
        f = open(files[file], 'r')
        try:
            content = f.read()
        except:
            pass
        if a and b in content:
            tablica = content[content.find(a) + len(a):content.find(b)].split()
            tab = [[], [], []]
            for line in tablica:
                temp = line.split()
            list1 = [2 + x * 9 for x in range(0, int(tablica[-10]))]
            list2 = [3 + x * 9 for x in range(0, int(tablica[-10]))]
            list3 = [4 + x * 9 for x in range(0, int(tablica[-10]))]
            tab[0].append(tablica[x] for x in list1)
            tab[1].append(tablica[x] for x in list2)
            tab[2].append(tablica[x] for x in list3)
            tab[0] = list(tab[0][0])
            tab[1] = list(tab[1][0])
            tab[2] = list(tab[2][0])
            if files[file][files[file].find('gold'):] != '2':
                pliki[files[file][files[file].find('gold'):]] = tab

for key in list(pliki.keys()):
    if 'soln' not in key:
        origin.append(key)
    else:
        soln.append(key)

for key in origin:
    print('Origin:', key)
    print()
    for key2 in soln:
        if key[5:key[5:].find('_') + 5] == key2[10:key2[10:].find('_') + 10]:
            print('Soln:', '\t', key2, '\t')
            # print('\t',round(porownanie(pliki[key],pliki[key2]),4))
            print('\t', 'RMSD =', round(porownanie(pliki[key], pliki[key2]), 4))
    print('\n')