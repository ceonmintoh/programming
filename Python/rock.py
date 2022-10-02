import random

def play():
    user = input("Whats Your Choice? r for rock, p for paper, s for scissors: ")
    computer = random.choice(['r', 'p', 's'])

    if user==computer:
        return 'Its a tie'

    if is_win(user, computer):
        return 'You Won'
    return 'You Lost'

def is_win(player1, player2):
    #r>s, s>p, p>r
    if(player1=='r' and player2 == 's') or (player1=='s' and player2=='p') or (player1=='p' and player2=='r'):
        return True