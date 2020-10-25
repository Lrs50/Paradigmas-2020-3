

def superSoma(a,b):
    return int(a)+int(b)

def super(num):
    if len(num)>1:
        resul=0
        for x in num:
            resul=superSoma(resul,x)
        return super(str(resul))
    else:
        return num

def main():
    n,k = input().split()
    print(super(n*int(k)))

if __name__=="__main__":
    main()