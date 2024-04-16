import random, time
import os

#Temporary to find issues with recursion
#import sys
#sys.setrecursionlimit(10)

os.system('cls')
print("Welcome to Rock Paper Scissors!")


def askplay():
    if 'play' not in globals():
        global play
    else:
        ...
    play = input("Are you ready to begin? (Yes/No)\n").lower()
    playchecker(play)

def game():
    # global computerpoints
    # computerpoints = 0
    # global playerpoints
    # playerpoints = 0

    def rpsshoot():
        os.system('cls')
        print("Rock..")
        time.sleep(1)
        os.system('cls')
        print("Paper..")
        time.sleep(1)
        os.system('cls')
        print("Scissors..")
        time.sleep(1)
        os.system('cls')
        print("Shoot!")
        time.sleep(1)
        os.system('cls')

    def askchoice():
        choose = input("Pick rock, paper, or scissors.\n").lower()
        if choose == "rock" or choose == "r":
            intchoice = int(1)
        elif choose == "paper" or choose == "p":
            intchoice = int(2)
        elif choose == "scissors" or choose == "s":
            intchoice = int(3)
        return intchoice

    def detrandomchoice():
        intrandomchoice = random.randint(1, 3)
        # 1 = R, 2 = P, 3 = S
        return intrandomchoice

    def tiechecker(choice):
        randomchoice = detrandomchoice()
        if choice == randomchoice:
            tiechecker(choice)
        elif choice != randomchoice:
            return randomchoice

    choice = askchoice()
    randomchoice = tiechecker(choice)

    def resultchecker():
        rpsshoot()
        if choice == 1: #Rock
            if randomchoice == 2: #Paper
                print(f"Computer chose paper")
                print(f"Paper beats rock, Computer wins!")
            elif randomchoice == 3: #Scissors
                print(f"Computer chose scissors")
                print(f"Rock beats scissors, Player wins!")
        elif choice == 2: #Paper
            if randomchoice == 1: #Rock
                print("Computer chose rock")
                print(f"Paper beats rock, Player wins!")
            elif randomchoice == 3: #Scissors
                print("Computer chose scissors")
                print(f"Scissors beats paper, Computer wins!")
        elif choice == 3: #Scissors
            if randomchoice == 1: #Rock
                print("Computer chose rock")
                print(f"Rock beats scissors, Computer wins!")
            elif randomchoice == 2: #Paper
                print("Computer chose paper")
                print(f"Scissors beats paper, Player wins!")

    resultchecker()

def asknoplay():
    askrules = input("Would you like to see the rules or quit? (Rules/Quit)\n").lower()
    noplay(askrules)

def noplay(askrules):
    if askrules == "rules" or askrules == "r":
        print("If you don't understand the rules of rock paper scissors, I'm very sorry for you.\nHowever, I'm too lazy to type out the rules for a practice project.")
        time.sleep(1.5)
        ready = input("Type anything when you are ready to begin!\n")
        if ready == "anything":
            print("Ok smart guy, let's get this game started.")
            time.sleep(3)
        os.system('cls')
        game()
    elif askrules == "quit" or askrules == "q":
        print("See you next time!")
        quit()
    else:
        print("That wasn't an option!")
        asknoplay()

def playchecker(play):
    if play == "yes" or play == "y":
        game()
    elif play == "no" or play == "n":
        asknoplay()
    else:
        print(f"That was not an option!")
        askplay()
askplay()

#I am aware there's no way to play again, I got this far and just wanted to move on to the next project.