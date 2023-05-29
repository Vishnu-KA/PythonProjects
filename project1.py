#import necessary modules
import random

#print(random.randint(1,200))

def play():
    user = input("enter the Input ")
    computer = random.choice(['R','P','S'])

    if user == computer:
        return "it is a tie"

    if game_win(user,computer):
        return "you won"

    else:
        return "you lost"

def game_win(player , opponent):
    #R>S, S>P ,P>R
    if(player == 'R' and opponent == 'S') or (player == 'S' and opponent == 'P') or (player == 'P' and opponent == 'R'):
        return True

print(play())