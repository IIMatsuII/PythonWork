import random
#from playsound import playsound

def again():
    dices = 0
    roll_again = print()
    while dices == 0:
        chosen_dices = int(input("How many dices do you want to roll? (form 1 to 5): "))
        if chosen_dices > 0 and chosen_dices < 6:
            break

    if chosen_dices == 1:
        #playsound('Dice snake.mp3')
        #playsound('Dice roll.mp3')
        while dices < 1:
            rolls = random.randint(1, 6)
            print(rolls)
            dices +=1

    elif chosen_dices == 2:
        #playsound('Dice snake.mp3')
        #playsound('Dice roll.mp3')
        while dices < 2:
            rolls = random.randint(1, 6)
            print(rolls)
            dices +=1

    elif chosen_dices == 3:
        #playsound('Dice snake.mp3')
        #playsound('Dice roll.mp3')
        while dices < 3:
            rolls = random.randint(1, 6)
            print(rolls)
            dices +=1

    elif chosen_dices == 4:
        #playsound('Dice snake.mp3')
        #playsound('Dice roll.mp3')
        while dices < 4:
            rolls = random.randint(1, 6)
            print(rolls)
            dices +=1

    elif chosen_dices == 5:
        #playsound('Dice snake.mp3')
        #playsound('Dice roll.mp3')
        while dices < 5:
            rolls = random.randint(1, 6)
            print(rolls)
            dices += 1

    print("Do you want to roll again?")
    while roll_again != "Yes" or roll_again != "No":
        roll_again = input("Yes | No: ").lower().capitalize()
        if roll_again == "Yes":
            again()
            break
        if roll_again == "No":
            print("GoodBye")
            break
again()