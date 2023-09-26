import random
def passg(k):
    x=[]
    for i in range(33,126):
        x.append(chr(i))
    paswd=''
    for i in range(k):
        paswd+=random.choice(x)
    print(paswd)
k=int(input("enter the Length of password"))
passg(k)   
