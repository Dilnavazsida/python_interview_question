import random

gussing_num = random.randint(1,100)

while True:

    try:
        user = int(input("guess the number "))

        if user > gussing_num:
            print("that is to high ")
        elif user < gussing_num:
            print("that is to low ")
        else:
            print("it's correct for ",user)
            break
    except ValueError:
        print("invalid number")
        