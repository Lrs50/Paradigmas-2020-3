
def main():

    n=int(input())
    res=[]
    for i in range(0,n):
        res.append('0')

    for i in range(0,n):
        k,c = input().split()
        res[int(k)-1]=str(c)

    res2=''

    for c in res:
        res2+=c

    print(res2)

if __name__=="__main__":
    main()