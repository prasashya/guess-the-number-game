import random
n=random.randint(1,100)

a=-1
guesses=0
while(a!=n):
    a=int(input("Guess a number between from 1 to 100: "))
    if(a<n):
        print("Higher number please")
    else:
        print("Lower numnber please")
    
        
    guesses+=1
    print(f"Guess no: {guesses}")
print(f"Next Shrlock Holmes !")

    
        
