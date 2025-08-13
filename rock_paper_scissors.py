import random
while True:
    list = ['rock','paper','scissors']

    stuff = random.choice(list)

    player = input("rock paper or scissors = r/s/p : ")
    if player not in ("r","s","p"): #got this"not in" ffrom chat gpt
        print("chose a valdi option")
        break
    player_status = 0
    dumb = 0
    if player == "r" and stuff == "paper":

        player_status = "lost"

    if player == "r" and stuff == "scissors":

        player_status = "won"

    if player == "r" and stuff == "rock":
        player_status = "draw"



    if player == "s" and stuff == "paper":

        player_status = "won"

    if player == "s" and stuff == "scissors":

        player_status = "draw"

    if player == "s" and stuff == "rock":
        player_status = "lost"


    if player == "p" and stuff == "paper":

        player_status = "draw"

    if player == "p" and stuff == "scissors":

        player_status = "lost"

    if player == "p" and stuff == "rock":
        player_status = "won"

    r = "rock"
    p = "paper"
    s = "scissors"

    if player == "r":
        dumb = "rock"

    if player == "s":
        dumb = "scissors"

    if player == "p":
        dumb = "paper "
    print(f"you choose: {dumb} \ncomputer choose:{stuff}")
    print(player_status)
    doufus = input("continue? (y/n): ")

    if doufus == "n":
        break




    
 

    