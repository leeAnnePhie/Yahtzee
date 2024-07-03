def isFourOfKind(rolls):
    return any([rolls.count(x) >= 4 for x in range(1, 7)])


def isFiveOfKind(rolls):
    nodups = list(set(rolls))
    return len(nodups) == 1


def isThreeOfKind(rolls):
    return any([rolls.count(x) >= 3 for x in range(1, 7)])


def isStraight(rolls):
    nodups = list(set(rolls))
    return len(nodups) == 5 and max(nodups) - min(nodups) == 4


def isShortStraight(rolls):
    if isStraight(rolls):
        return True
    nodups = list(set(rolls))
    nodups.sort()
    if (len(nodups) == 4) and max(nodups) - min(nodups) == 3:
        return True
    if (len(nodups) == 5):
        return nodups[4] - nodups[1] == 3 or nodups[3] - nodups[0] == 3
    else:
        return False


def isFullhouse(rolls):
    if isFiveOfKind(rolls):
        return True
    rolls.sort()
    if len(set(rolls)) == 2 and rolls.count(rolls[0]) == 3 or rolls.count(rolls[0]) == 2:
        return True
    else:
        return False
