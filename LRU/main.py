from GeoDistributedLRU import Lru

key=['a','b','c''d','e','f','g']

value=['abc.txt','def.txt','sheet.xlsx','val.ppt','jun.py','ulx.xlsx']

lru=Lru()

for i in key:
    lru.add(i,value[key.index(i)])
print (lru.mem)
