#This code shows how to use Random module in python
import random # I can use from random import choice i can use choice directly 
coin = random.choice(["Head", "Tail"])
input("Press Enter to flip the coin: ")
print(coin)

print()

DiceCube = int(random.choice([1, 2, 3, 4, 5, 6]))
input("Press Enter to throw the dice cube: ")
print(DiceCube)
while True:
    if DiceCube == 6:    
        DiceCube = int(random.choice([1, 2, 3, 4, 5, 6])) # I put again so i don't fall in an infinite loop 
        input("Press Enter to play again: ")
        print(DiceCube)
    else:
        break

print()

x = int(random.randint(1, 1000))
input("Press Enter to choose a random number between 1 to 1000: ")
print(x)

print()

cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]
random.shuffle(cards) #The shuffle function require lists
input("Press Enter to shuffle your cards: ")
for card in cards:
    print(card, end = ", ")

