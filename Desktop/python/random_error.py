import random


def guess(x):
    number = random.randint(1 ,x)
    guess=0
    print(number)

    while guess!=number:
        guess= int (input(f'give an input between 1 to  {x}: '))
        if(guess<number):
            print(" too low ")
        elif(guess>number):
            print("too high")


    print(f'you did it {number}') 
       
def  hello(x):
    low=1 
    high =x
    feedback=''


     
