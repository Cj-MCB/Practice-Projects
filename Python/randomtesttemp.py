import random

def pickedone():
    print("1")

def pickedtwo():
    print("2")

def pickedother():
    print("Other")

numberpicked = int(input("Pick 1 or 2"))

if numberpicked == 1:
    pickedone()
elif numberpicked == 2:
    pickedtwo()
else:
    pickedother()