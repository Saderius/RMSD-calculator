#wpisuje długo
import os
import mmap
x=[]
for file in os.listdir("."):
    if file.endswith(".mol2"):
        x.append(os.path.join(".", file))

print(x)

#for file in os.listdir("."):
#    if '@<TRIPOS>ATOM' in open(x)).read():
#        print('true')

f = open(file)
s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
for file in os.listdir("."):
    if file.endswith(".mol2"):
        y=s.find('@<TRIPOS>ATOM')
        print(y)
        
        
  #      open()).read():
   #       print('true')
