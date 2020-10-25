
def main():
    h=input()
    _min=input()
 
    t="am"


    h=int(h)
    if h>=12:
        t="pm"
    if h>12:
        h-=12

    h=str(h)
    if(len(h)==1):
        h="0"+h
    if(len(_min)==1):
        _min="0"+_min

    if h=="00":
        h="12"

    print(h+"\n"+_min+"\n"+t)


if __name__=="__main__":
    main()