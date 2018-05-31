import random

"""
this program will allow the user to enter his/her name
and give clues in order to guess a number between 0 and 100.
"""
guessesTaken = 0
username = input("what is your name?:")

rand_number = random.randint(0, 100)

print("well, " + username + " , im thinking of a number between 0 and 100.")

guess = -1
while guess != rand_number:
    print("take a guess: ")
    guess = input()
    guess = int(guess)

    if guess < rand_number:
        print("" + str(guess) + " is too small of a number " + username + "")
    elif guess > rand_number:
        print("" + str(guess) + " is too big of a number " + username + "")
    else:
        print("Great job " + username + " " + str(guess) + " is correct")

print("thanks for playing " + username + " !")
