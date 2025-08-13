import random
number = random.randint(2,10)


while True:
   
    sub = input("guess a number b/w 2 and 10:\n")
   

    try :  #got this method from google
        newnum = int(sub)
    except: 
        print("enter a valid number:")
        exit()  
    
    if newnum < number:
        print("too low:")

    elif newnum == number:
        print("you got it..")
        exit()
       
    elif newnum > number:
      print("too high:")

    
#final


#check the screenshots i had taken ton of this proccess on how i reached this final one by undo adn redo :)
# 9:39pm / twelve/8/2025

# again soo fuckign proud of myslef for doing this maaan :)
