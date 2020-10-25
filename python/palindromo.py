
def main():

    word=input()
    word=word.lower()
    word=list(word)
    word=list(filter(lambda a: a!=" ",word))
    
    word2=[]
    for i in range(1,len(word)+1):
        word2.append(word[i*(-1)])

    if word==word2:
        print("SIM")
    else:
        print("NAO")
        
if __name__=="__main__":
    main()