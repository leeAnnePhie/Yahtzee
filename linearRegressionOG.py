import matplotlib.pyplot as plt
import numpy
import numpy as np
from tkinter import messagebox

placeHolder = [0, 0, 0, 0, 0]
roundOneDiceHeld = []
roundTwoDiceHeld = []
indexList = []
trackofRolls = 3
finalRoundDiceHeld = []
theta = np.zeros(2)

diceHeld = []
roundScore = []

def appending():
    global placeHolder
    global roundOneDiceHeld
    global roundTwoDiceHeld
    global finalRoundDiceHeld
    global trackofRolls
    global indexList
    placeholder2 = []
    if trackofRolls == 3:
        roundOneDiceHeld.extend(placeHolder)
    elif trackofRolls == 2:
        for i in indexList:
            x = roundOneDiceHeld[i]
            placeholder2.append(x)
        for i in placeholder2:
            roundOneDiceHeld.remove(i)
        roundTwoDiceHeld.extend(placeHolder)
        placeholder2 = []
    elif trackofRolls == 1:
        for i in indexList:
            x = roundTwoDiceHeld[i]
            placeholder2.append(x)
        for i in placeholder2:
            roundTwoDiceHeld.remove(i)
        placeholder2 = []
    elif trackofRolls == 0:
        finalRoundDiceHeld.extend(roundOneDiceHeld)
        finalRoundDiceHeld.extend(roundTwoDiceHeld)
        trackofRolls = 3
    indexList = []


def updateLists():
    global finalRoundDiceHeld
    global placeHolder
    global roundOneDiceHeld
    global roundTwoDiceHeld
    global trackofRolls
    global diceHeld
    for i in finalRoundDiceHeld:
        #roundScore.append(checkChecks.TotalScore)
        diceHeld.append(i)
    finalRoundDiceHeld = []
    placeHolder = [0, 0, 0, 0, 0]
    roundOneDiceHeld = []
    roundTwoDiceHeld = []
    trackofRolls = 3


def predict(theta, roundScore):
    hey = theta[0] + theta[1] * roundScore
    return hey


def visualize(theta, roundScore, diceHeld):
    plt.scatter(roundScore, diceHeld, alpha=0.2, s=10)
    plt.xlabel('Score of Round')
    plt.ylabel('Dice Held')
    plt.title('Value of Dice Held vs Score of Round', fontsize=20)
    xp = np.array(roundScore)
    yp = theta[0] + theta[1] * xp
    plt.plot(roundScore, yp)
    plt.axis((min(roundScore) - 2, max(roundScore)+10, 0, max(diceHeld)))
    plt.show()


def fit(roundScore, diceHeld, theta, alpha, iter):
    theta = np.zeros(2)
    roundScore = np.array(roundScore)
    diceHeld = np.array(diceHeld)
    n = len(roundScore + diceHeld)
    for f in range(iter):
        m_gradient = 0
        b_gradient = 0
        m_gradient = np.float16(m_gradient)
        b_gradient = np.float16(b_gradient)
        for i in range(n):
            m_gradient += -(2 / n) * roundScore[i] * (diceHeld[i] - predict(theta, roundScore[i]))
            b_gradient += -(2 / n) * (diceHeld[i] - predict(theta, roundScore[i]))
        theta[1] = theta[1] - alpha * m_gradient
        theta[0] = theta[0] - alpha * b_gradient
    return theta


def showStats():
    messagebox.askokcancel(
        message="Your Dice Held is: " + str(diceHeld) + "\n and your individual scores are " + str(roundScore))


def showfinalstats():
    visualize(fit(roundScore, diceHeld, theta, 0.0001, 100), roundScore, diceHeld)

