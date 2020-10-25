from functools import reduce

def getresult(a):
    res=(0,a[0])
    for i in range(0,len(a)):
        if res[1]>a[i]:
            res=(i,a[i])

    return res[0]+1


def main():
    n,m=input().split()
    resul=[]
    for i in range(0,int(n)):
        v=input().split()
        v=list(map(int,v))
        v=reduce(lambda a,b: a+b,v,0)
        resul.append(v)

    print(getresult(resul))
if __name__=="__main__":
    main()