import random
n=random.randrange(1,10)
guess=int(input("enter any number"))
while n!= guess:
    if guess<n:
        print("too low")
        guess=int(input("enter number"))
    elif guess > n:
        print("too high")
        guess = int(input("enter number"))
    else:
        break; 