from typing import List
from typing import Dict
from functools import reduce
#you can "define the type of a variable" num:int = 3
#numeros:List[int] define list of ints, needs the typing library 


def fatorial(n:int)->int:
    if n==0:
        return 1
    else:
        return n*fatorial(n-1)

def somaNumeros(n):
    if n<0:
        return 0
    else:
        soma=0
        for x in range(1,n+1):
            soma=soma+x
        return soma

def main():
    numeros=[1,2,3,4,True,"eu sou um numero",1.24,"no meu coração eu sou um float","hihi"]
    for x in numeros:
        print(x)
    numeros.append("oi")
    numeros.pop()
    #indexing,append,len,pop,insert
    numeros=[1,2,3,4,5,6,7,8,9,10]
    print(list(map((lambda x:x*x),numeros)))
    print(list(filter((lambda x: x%2==0),numeros)))
    print(reduce(lambda x,y:x+y,numeros,0))

    # numeros=numeros2    numeros2 aponta para a mesma regiao da memoria
    # numeros=numeros2[:] copia [0:len(numeros)] : = slice operator

    codigos:Dict[str,int]={"BR":55,"US":1,"JP":81,"UK":44,"VU":678,"UY":598}
    codigos["TO"]=678
    #codigos.values()

if __name__=="__main__":
    main()