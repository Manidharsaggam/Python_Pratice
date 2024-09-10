# write a python program on guess game
print('-'*30,"Guess Numbers From 1 to 10",'-'*30)
'''
random is a inbuilt library in python
which can create random number/guesses by the system only
randint means its generate integers/number 
'''
from random import randint
Number = randint(1,10)
# print(Number)
chances = 3 #How many chance do you want play
for chance in range(chances):
    guess_Number = int(input("Guess The correct Number: "))
    if guess_Number == Number:
        print("Congratulations**")
        print("You Won The Game")
    else:
        print("Wrong Guess Please Try again")
print("*"*7,"You Lost The Game","*"*7)

