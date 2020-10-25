
def main():

    ano=int(input())
    
    if ano%4==0:
        if ano%100==0:
            if ano%400==0:
                print("BISSEXTO")
            else:
                print("NAOBISSEXTO")
        else:
            print("BISSEXTO")
    else:
        print("NAOBISSEXTO")
        
if __name__=="__main__":
    main()