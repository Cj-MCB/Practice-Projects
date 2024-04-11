import random, time

print("Welcome to Rock Paper Scissors!")


def askplay():
    if 'play' not in globals():
        global play
    else:
        ...
    play = input("Are you ready to begin? (Yes/No)\n").lower()
    playchecker(play)

def game():
    global computerpoints
    computerpoints = 0
    global playerpoints
    playerpoints = 0

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
        intrandomchoice = random.randint(1, 3)
        #print(f"Random choice: {intrandomchoice}")
        # 1 = R, 2 = P, 3 = S
        return intrandomchoice

    def tiechecker(choice):
        #print("Running tie-checker")
        randomchoice = detrandomchoice()
        if choice == randomchoice:
            #print(f"Duplicate detected, your choice: {choice}, computer's choice: {randomchoice}")
            tiechecker(choice)
        elif choice != randomchoice:
            #print(f"Your choice: {choice}, Computer's choice: {randomchoice}")
            return randomchoice

    choice = askchoice()
    randomchoice = tiechecker(choice)

    def endgamechecker(computerpoints, playerpoints):
        if computerpoints >= 2:
            ...
        elif playerpoints >=2:
            ...
        else:
            # Add round numbers later
            print("Here comes the next round!")
            askchoice()

    def resultchecker(computerpoints, playerpoints):
        if choice == 1: #Rock
            if randomchoice == 2: #Paper
                computerpoints += 1
                print(f"Paper beats rock, Computer wins!\nComputer: {computerpoints}\nPlayer: {playerpoints}")
            elif randomchoice == 3: #Scissors
                playerpoints += 1
                print(f"Rock beats scissors, Player wins!\nComputer: {computerpoints}\nPlayer: {playerpoints}")
        elif choice == 2: #Paper
            if randomchoice == 1: #Rock
                playerpoints += 1
                print(f"Paper beats rock, Player wins!\nComputer: {computerpoints}\nPlayer: {playerpoints}")
            elif randomchoice == 3: #Scissors
                computerpoints += 1
                print(f"Scissors beats paper, Computer wins!\nComputer: {computerpoints}\nPlayer: {playerpoints}")
        elif choice == 3: #Scissors
            if randomchoice == 1: #Rock
                computerpoints += 1
                print(f"Rock beats scissors, Computer wins!\nComputer: {computerpoints}\nPlayer: {playerpoints}")
            elif randomchoice == 2: #Paper
                playerpoints += 1
                print(f"Scissors beats paper, Player wins!\nComputer: {computerpoints}\nPlayer: {playerpoints}")
        endgamechecker(computerpoints, playerpoints)

    resultchecker(computerpoints, playerpoints)
    
def playchecker(play):
    if play == "yes" or play == "y":
        game()
    elif play == "no" or play == "n":
        ...
    else:
        print(f"That was not an option!")
        askplay()

askplay()
# Add results, etc.