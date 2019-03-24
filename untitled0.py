# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 17:21:24 2019

@author: porto
"""

import os
import mmap
import re
import numpy as np
#x=[]
d='dobrze'
for file in os.listdir("."):
    if file.endswith(".mol2"):
        f = open(file,'r')
        s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
        a='TRIPOS>ATOM'
        b='TRIPOS>BOND'
        print(d)
        content=f.read()
        if a and b in content:
            tab=content[content.find(a)+len(a):content.find(b)]
tabela=spl


'''
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
                           '''
                           
                           