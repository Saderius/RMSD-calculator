# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 18:44:54 2019

@author: porto
"""
'''
#wpisuje długo
import os
import mmap
x=[]
for file in os.listdir("."):
    if file.endswith(".mol2"):
       x.append(os.path.join(".", file))

print(x)

for file in os.listdir("."):
    if 'TRIPOS>ATOM' in open(x)).read():
        print('true')

f = open(file)
s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
for file in os.listdir("."):
    if file.endswith(".mol2"):
        y=s.find('@<TRIPOS>ATOM')
        print(y)
        
        
  #      open()).read():
   #       print('true')
'''
import os
import mmap
import re
#x=[]
d='dobrze'
for file in os.listdir("."):
    if file.endswith(".mol2"):
        f = open(file,'r')
        s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
        a='TRIPOS>ATOM'
        b='TRIPOS>BOND'
        print(d)
        if a and b in f.read():
            print(f.read())'''
           #with f.read() as ort:
           #print(d)
            for lin in range(2): #f.read():
               print('d')
               line = re.findall(r'c', line)
               if line:
                   line = line[0].split('"')[1]
                   print(line)
                   print(d)
                   with f as origin_file:
                       for line in origin_file:

                           line = re.findall(r'TRIPOS>ATOM', line)
                    #if line:
                     #line = line[0].split('"')[1]
                           print(line)
           # print('true')
       # z=s.find('TRIPOS>BOND'.encode())
       # for i in range(y,z):
        #    with open(file, 'rb') as f:
                           c = [i.decode('utf8').strip() for i in f.readlines()]
                           print(c)
            
            
 #           b = [i.decode('utf8').strip() for i in f.readlines()]
#            print(b)





        with open(file, 'rb') as f:
            b = [y.decode('utf8').strip() for y in f.readlines()]
            print(b)
        
       #x.append(os.path.join(".", file))
#lines = [x.decode('utf8').strip() for x in f.readlines()]

def check():
    datafile = file('example.txt')
    found = False #this isn't really necessary 
    for line in datafile:
        if blabla in line:
            #found = True #not necessary 
            return True
    return False #because you finished the search without finding 






















