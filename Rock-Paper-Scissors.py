from ast import Return
import random
import re

def play():
    user = input("what's your choice: \n 'R' for rock, 'P' for paper 'S' for scissors").upper()
    comp = random.choice(['R', 'P', 'S'])

    if user == comp:
        return "it's a tie"
    if win(user, comp):
        return "you won!"
    return "you lost"

def win(p, o):
    if (p == 'R' and o =='S') or (p == 'P' and o == 'R') or (p == 'S' and o == 'P'):
        return True
    else:
        return False

print(play())
