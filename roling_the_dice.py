import random

while True:

    user=input("roll the dice (y/n) ").lower()

    if user == 'y':
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        print(f'({dice1},{dice2})')

    elif user == 'n':
        print("Thanks for playing ")
        break
    else:
        print("invelid choice")



