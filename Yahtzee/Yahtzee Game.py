import random

diceKept = []
keepDice = 0
diceRolls = [0, 0, 0, 0, 0]
keepAll = 0
TotalScore = 0


def getDiceRolls():
    global diceKept
    for x in range(len(diceRolls)):
        if x not in diceKept:
            diceRolls[x] = (random.randint(1,6))
        else:
            diceRolls[x] = diceRolls[x]


def reRoll():
    global diceKept
    quit = " "
    print("Enter the position of dice to keep or 'q' to quit.")
    while quit != "q":
        quit = input("> ")
        if quit == "q":
            break
        elif '0' < quit < '6':
            keepDice = (int(quit) - 1)
            diceKept.append(keepDice)
        else:
            print("Invalid Input")



def isFiveKind():
    global TotalScore
    score = 0
    if diceRolls.count(0) == 5:
        return True
        score = 50
    else:
        return False


def isFourKind():
    global TotalScore
    score = 0
    for i in range(1, 7):
        if diceRolls.count(i) == 4:
            score = sum(diceRolls)
            return True
            break

        elif i == 6:
            return False


def isThreeKind():
    global TotalScore
    score = 0
    for i in range(1, 7):
        if diceRolls.count(i) == 3:
            score = sum(diceRolls)
            return True
        elif i == 6:
            return False


def isStraight():
    global TotalScore
    score = 0
    minRange = min(diceRolls)
    maxRange = max(diceRolls)+1
    for i in range(minRange, maxRange):
        if i not in diceRolls:
            return False
            break
        elif i == max(diceRolls):
            score = 40
            return True


def isShortStraight():
    global TotalScore
    score = 0
    shortStraight = set(diceRolls)
    if len(shortStraight) < 4:
        return False
    minRange = min(diceRolls)
    maxRange = max(diceRolls) + 1
    for i in range(minRange, maxRange):
        if i not in diceRolls:
            return False
            break
        elif i == max(diceRolls):
            score = 40
            return True


def isFullHouse():
    twoOfaKind = 0
    threeOfaKind = 0
    global TotalScore
    score = 0
    for i in range(1, 7):
        if diceRolls.count(i) == 3:
            threeOfaKind = 1
        elif diceRolls.count(i) == 2:
            twoOfaKind = 1
    if threeOfaKind == 1 and twoOfaKind == 1:
        score = 25
        return True
    else:
        return False


def isOne():
    global TotalScore
    score = diceRolls.count(1)*1


def isTwo():
    global TotalScore
    score = diceRolls.count(2)*2


def isThree():
    global TotalScore
    score = diceRolls.count(3)*3


def isFour():
    global TotalScore
    score = diceRolls.count(4)*4


def isFive():
    global TotalScore
    score = diceRolls.count(5)*5


def isSix():
    global TotalScore
    score = diceRolls.count(6)*6

def chance():
    global TotalScore
    score = sum(diceRolls)


alreadySelected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

scoreSelection = ["Zero", "Ones", "Twos", "Threes", "Fours", "Fives",
                  "Sixes", "Three of a kind", "Four of a kind",
                  "Full House", "Short Straight","Long Straight",
                  "Five of a kind", "Chance"]

selectionFunctions = [0, isOne, isTwo, isThree, isFour, isFive, isSix, isThreeKind, isFourKind, isFullHouse, isShortStraight, isStraight, isFiveKind, chance]

keepScore = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0,
    10: 0,
    11: 0,
    12: 0,
    13: 0
}


def makeScoreSelection():
    for x in alreadySelected:
        print(str(x) + " : " + scoreSelection[x], end="\n")
    toRemove = input("Enter number to assign roll to \n > ")
    alreadySelected.remove(int(toRemove))
    reeemove = int(toRemove)
    selectionFunctions[reeemove]()
    keepScore.update({int(toRemove):TotalScore})


def printScoreSelection():
    print("Score")
    for x, y in keepScore.items():
        print(scoreSelection[x], ":", keepScore[x], end="\n")
    totalScore = sum(keepScore.values())
    print("Total Score : " + str(totalScore)+ "\n")


def turn():
    global diceKept
    reRollNumber = 0
    diceKept = []
    while True:
        if reRollNumber == 2:
            getDiceRolls()
            break
        elif len(diceKept) == 5:
            break
        else:
            getDiceRolls()
            print("Your set of dice are " + str(diceRolls)+ "\n")
            diceKept = []
            reRoll()
            reRollNumber += 1
    print("Your final set of dice are " + str(diceRolls) + "\n")
    makeScoreSelection()
    printScoreSelection()


for i in range(1,14):
    turn()

totalaaScore = 0
finalScore = 0
for i in range(6):
    totalaaScore += keepScore.values(i)

if totalaaScore > 63:
    finalScore = 35+sum(keepScore.values())

print("Final Score: "+finalScore)
