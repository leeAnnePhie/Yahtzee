TotalScore = 0
mainScoreList = [0, 0, 0, 0, 0]

def isFiveKind():
    global TotalScore
    TotalScore = 0
    if mainScoreList.count(0) == 5:
        TotalScore = 50


def isFourKind():
    global TotalScore
    TotalScore = 0
    for i in range(1, 7):
        if mainScoreList.count(i) >= 4:
            TotalScore = sum(mainScoreList)
            break


def isThreeKind():
    global TotalScore
    TotalScore = 0
    for i in range(1, 7):
        if mainScoreList.count(i) >= 3:
            TotalScore = sum(mainScoreList)


def isStraight():
    global TotalScore
    TotalScore = 0
    minRange = min(mainScoreList)
    maxRange = max(mainScoreList) + 1
    for i in range(minRange, maxRange):
        if i not in mainScoreList:
            break
        elif i == max(mainScoreList):
            TotalScore = 40


def isShortStraight():
    global TotalScore
    TotalScore = 0
    shortStraight = set(mainScoreList)
    if len(shortStraight) < 4:
        return TotalScore
    minRange = min(mainScoreList)
    maxRange = max(mainScoreList) + 1
    for i in range(minRange, maxRange):
        if i not in mainScoreList:
            break
        elif i == max(mainScoreList):
            TotalScore = 40


def isFullHouse():
    twoOfaKind = 0
    threeOfaKind = 0
    global TotalScore
    TotalScore = 0
    for i in range(1, 7):
        if mainScoreList.count(i) == 3:
            threeOfaKind = 1
        elif mainScoreList.count(i) == 2:
            twoOfaKind = 1
    if threeOfaKind == 1 and twoOfaKind == 1:
        TotalScore = 25



def isOne():
    global TotalScore
    TotalScore = mainScoreList.count(1) * 1


def isTwo():
    global TotalScore
    TotalScore = mainScoreList.count(2) * 2



def isThree():
    global TotalScore
    TotalScore = mainScoreList.count(3) * 3



def isFour():
    global TotalScore
    TotalScore = mainScoreList.count(4) * 4



def isFive():
    global TotalScore
    TotalScore = mainScoreList.count(5) * 5



def isSix():
    global TotalScore
    TotalScore = mainScoreList.count(6) * 6


def chance():
    global TotalScore
    TotalScore = sum(mainScoreList)


selectionFunctions = [0, isOne, isTwo, isThree, isFour, isFive, isSix, isThreeKind, isFourKind, isFullHouse,
                          isShortStraight, isStraight, isFiveKind, chance]


