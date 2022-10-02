"""
  This is a simple guess Game, with Value from User  
"""
import random as rn

range_num = int(input('What is the Maximum Value in your Game? '))
def guess(x):
    random_num = rn.randint(1, x)
    guess = 0
    while guess != random_num:
        
        guess = int(input(f'Guess the Number between 1 and {x}: '))
        counnt =+ 1
        
        if guess <random_num:
            print('Try Again, with higher vaue')
        elif guess > random_num:
            print('Try Again with a Lower Value')
    print(f'Nice one, The Correct Number was {random_num} and you got it after {counnt} times')
guess(range_num)
