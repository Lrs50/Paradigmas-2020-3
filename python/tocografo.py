
def main():
    n=int(input())
    dist=0
    for i in range(0,n):
        t,v= input().split()
        t=int(t)
        v=int(v)
        dist+= (t*v)
    
    print(dist)
if __name__=="__main__":
    main()