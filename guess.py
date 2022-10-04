import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"guess the Number between 1 and {x}: "))
        if(guess < random_number):
            print("Sorry! the number is too low!")
        elif(guess > random_number):
            print("Sorry! the number is too high!")
    print(f"Yay! you guessed the right number {guess} correctly")
# a = int(input("enter the range for the game: "))
# guess(a)

def comp_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"The Number is {guess} Enter C if the guessed no. is correct, L for less & H for more: ").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print("Yay! you guessed the right number {guess} correctly")

a = int(input("enter the range for the game: "))
comp_guess(a)
