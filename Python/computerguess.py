import random as rn

Max = int(input('What is the Maxinmum Value of our Game?'))

def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != 'c':
        if low != high:
            guess = rn.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} too higher (H) or lower (L) or Correct (C)?').lower()
        if feedback == 'h':
            high = guess -1
        elif feedback == 'l':
            low = guess +1
    print(f'Wow! This computer was able to guess your number as {guess}, correctly')
computer_guess(Max)
        
        
        
        
