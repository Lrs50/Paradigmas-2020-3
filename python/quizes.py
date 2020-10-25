from functools import reduce

def menor(a,b):
    if a>b:
        return b
    else:
        return a

v=[5,1,2]
v=int(reduce(menor,v,1000001))

print(v)