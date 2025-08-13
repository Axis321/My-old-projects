#did this myslef :)
#i am soo fucking proud of myself.
import random

did = True
while did == True:
    numbers = random.randint(2,7)
    numbers2 =random.randint(2,7)
    first = input("roll the dice? (y/n) ")

    if first == "y":
        msg = f"({numbers},{numbers2})"
        print(msg)

    elif first == "n":
        print("thank you for playing")
        exit()

    else:
        print("invalid input")