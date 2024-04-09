import random, time


print("Welcome to Rock Paper Scissors!")

def askplay():
    play = input("Are you ready to begin? (Yes/No)\n").lower()
    return play

def game():
    def rpsshoot():
        wait = time.sleep(1)
        print("Rock..")
        wait
        print("Paper..")
        wait
        print("Scissors..")
        wait
        print("Shoot!")
    print("This is going to be a 2 out of 3 game, so be prepared!")
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
        #intrandomchoice = random.randint(1,3)
        #Temporary Line to test tie checker
        intrandomchoice = int(1)
        # 1 = R, 2 = P, 3 = S
        return intrandomchoice
    randomchoice = detrandomchoice()
    choice = askchoice()
    if choice == randomchoice:
        print(randomchoice, "Duplicate Detected")
        #randomchoice = 0
        detrandomchoice()
    elif choice != randomchoice:
        print(randomchoice, "NON-Duplicate")
    print(choice)
    
play = askplay()
if play == "yes" or play == "y":
    game()
elif play == "no" or play == "n":
    ...
else:
    ...

# Add results, points, no tie, etc.