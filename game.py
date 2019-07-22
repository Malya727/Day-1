''' program for dice game '''
''' by malya '''

import random

q=0
print("********** Welcome to my game **********")
while(q==0):
    n=random.randint(1,9)
    at=1
    while(True):
        inp=int(input("Enter guessed Number :"))
        if(at>3):
            print("Oh!! Sorry You lost your chances")
            print(f"Generated number is {n} ")
            break
        else:
            if(n==inp):
                print(f"Congrats You guessed in {at} attempt")
                break
            else:
                at+=1
    p=input("Want to Continue game (y/n)")
    if(p=='n'):
        q=1

