scoreCard = {
    "Ones": 4,
    "Twos": 0,
    "Threes": 9,
    "Chance": 24
}


def printScoreCard():
    for (key, value) in scoreCard.items():
        print(key, ":", value)
printScoreCard()
# calculate the total of all five dice rolls
# e.g. calculateDiceTotal([2,3,5,2,1]) returns 13
def calculateDiceTotal(diceRolls):
    return sum(diceRolls)
print(calculateDiceTotal([2,3,5,2,1]))
# calculate the total for a particular number
# e.g. calculateTotalOfRoll(2, [2, 4,5, 2, 2]) returns 6
def calculateTotalOfRoll(number, diceRolls):
    return diceRolls.count(number)*number

print(calculateTotalOfRoll(2, [2, 4,5, 2, 2]))
