#game though loops

import random
n = 20
to_be_gussesed = int(n * random.random()) +  1
guess = 0
while guess  != to_be_gussesed:
    guess = int(input("New number:"))
    if guess > 0:
        if guess > to_be_gussesed:
            print("Number too large")
        elif guess < to_be_gussesed:
            print("Number too small")


        else:
            print("Sorry that youre giving up!")
            break
else:
    print("congralution.u made it")


#this is example of whilw loop