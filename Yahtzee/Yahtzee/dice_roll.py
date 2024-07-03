import random


def getDiceRolls():
    diceRolls = []
    for i in range(5):
        diceRolls.append(random.randint(1, 6))
    print("Your initial dice rolls are...")
    print(diceRolls)

    for i in range(2):
        reroll_list = []
        print("Enter the position of the dice roll or q to quit")
        while True:
            response = input("> ")
            if response == "q":
                break
            else:
                reroll_list.append(int(response))

        for i in reroll_list:
            diceRolls[i-1] = random.randint(1, 6)

        print("New dice rolls are...", diceRolls)
    return diceRolls

print(getDiceRolls())
