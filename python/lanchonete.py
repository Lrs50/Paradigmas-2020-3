
def main():
    n=int(input())
    catalog={}
    for i in range(0,n):
        led=int(input())
        des=str(input())
        price=float(input())
        catalog[led]=(des,price)

    val=0.0
    
    while True:
        led=int(input())
        if led==0:
            break
        q=int(input())
        if q>0:
            if led in catalog:
                val+=catalog[led][1]*q

    print(format(round(val,2),".2f"))


if __name__=="__main__":
    main()