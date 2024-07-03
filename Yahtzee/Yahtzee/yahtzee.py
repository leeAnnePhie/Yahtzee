from checker import *
import random

scoringOptions = [
    "Ones",
    "Twos",
    "Threes",
    "Fours",
    "Fives",
    "Sixes",
    "Three of a kind",
    "Four of a kind",
    "Fullhouse",
    "Short Straight",
    "Long Straight",
    "Five of a kind",
    "Chance"
]

scoreCard = {
    "Ones": 0,
    "Twos": 0,
    "Threes": 0,
    "Fours": 0,
    "Fives": 0,
    "Sixes": 0,
    "Three of a kind": 0,
    "Four of a kind": 0,
    "Fullhouse": 0,
    "Short Straight": 0,
    "Long Straight": 0,
    "Five of a kind": 0,
    "Chance": 0
}


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
            diceRolls[i - 1] = random.randint(1, 6)

        print("New dice rolls are...", diceRolls)
    return diceRolls


def makeScoreSelection():
    global scoringOptions
    counter = 1
    print("Select one of the following available scoring options...")
    for option in scoringOptions:
        print(str(counter) + ":", option)
        # add 1 to the counter
        counter = counter + 1
    response = input("> ")
    selection = scoringOptions[int(response) - 1]
    scoringOptions.remove(selection)
    return selection


def printScoreCard():
    for (key, value) in scoreCard.items():
        print(key, ":", value)


def calculateDiceTotal(diceRolls):
    return sum(diceRolls)


def calculateTotalOfRoll(number, diceRolls):
    return diceRolls.count(number) * number


def calculateScore(scoringOption, diceRolls):
    global scoreCard
    score = 0
    # update the score by checking whether the scoring option is
    # valid

    # update the score card dictionary
    scoreCard[scoringOption] = score


diceRolls = getDiceRolls()
scoringOption = makeScoreSelection()
calculateScore(scoringOption, diceRolls)
printScoreCard()