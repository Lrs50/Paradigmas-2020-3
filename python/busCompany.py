
def avarageAge(registry):
    res=0
    for x in registry:
        res+=x[6]
    
    return res/(len(registry))

def main():
    registry=[[]]
    while True:
        n=int(input())
        if n==-1:
            condition=False
            break
        temp=[]
        temp.append(n)
        for x in range(0,7):
            if x==4 or x==5:
                temp.append(int(input()))
            else:
                temp.append(str(input()))
        registry.append(temp)

    registry.pop(0)
    av=avarageAge(registry)
    for x in registry:
        if x[6]>av and x[5]%2==0:
            print(x[7])

if __name__=="__main__":
    main()