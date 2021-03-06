import time


def getName(question):
    return input(str(question))


def welcome():
    print("Welcome to the Rune Isle!\n")
    time.sleep(0.5)
    print("First, what is your name adventurer?")
    playerName = getName("> ")
    print("Good luck, " + playerName)
    return str(playerName)
