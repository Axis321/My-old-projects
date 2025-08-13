import random
number = random.randint(2,10)


while True:
   
    sub = input("guess a number b/w 2 and 10:\n")
   

    try :  
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

    
