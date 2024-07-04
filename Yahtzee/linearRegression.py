#import matplotlib.pyplot as plt
#import numpy as np
#import csv
#from scipy import stats
import checkChecks
from tkinter import *
from tkinter import messagebox

placeHolder = []
roundOneDiceHeld = []
roundTwoDiceHeld = []
indexList = []
trackofRolls = 3
finalRoundDiceHeld = []

def appending():
  global placeHolder
  global roundOneDiceHeld 
  global roundTwoDiceHeld
  global finalRoundDiceHeld
  global trackofRolls
  if trackofRolls == 3:
    roundOneDiceHeld.extend(placeHolder)
    placeHolder = []
  elif trackofRolls == 2:
    for i in indexList:
      roundOneDiceHeld.pop(i)
    roundTwoDiceHeld = placeHolder[:]
    placeHolder = []
  elif trackofRolls == 1:
    for i in indexList:
      roundTwoDiceHeld.pop(i)
    placeHolder = []
  elif trackofRolls == 0:
    finalRoundDiceHeld.extend(roundOneDiceHeld)
    finalRoundDiceHeld.extend(roundTwoDiceHeld)


diceHeld = [] #independent
roundScore = [] #independent 

def updateLists():
  global finalRoundDiceHeld
  global placeHolder
  global roundOneDiceHeld 
  global roundTwoDiceHeld
  global trackofRolls
  global diceHeld
  for i in finalRoundDiceHeld:
    roundScore.append(checkChecks.TotalScore)
    diceHeld.append(i)
  finalRoundDiceHeld = []
  placeHolder = []
  roundOneDiceHeld = []
  roundTwoDiceHeld = []
  trackofRolls = 3

def visualize(theta, diceHeld, roundScore):
  plt.scatter(diceHeld, roundScore, color = 'g',s = 40)
  plt.xlabel('Value of Dice Held')
  plt.ylabel('Score of Round')
  plt.title('Value of Dice Held vs Score of Round', fontsize = 20)
  diceArray = np.append(diceHeld, [0, max(diceHeld)+10])
  scoreArray = theta[0] + theta[1] * diceArray
  plt.plot(diceHeld, scoreArray)
  plt.axis((0, max(diceArray), -2, max(roundDice)))
  plt.show()

def predict(theta, x):
  hey = theta[0] + theta[1] * x
  return hey

def fit(x, y, theta, alpha, iter):
  theta = np.zeros(2)
  x = np.array(x)
  y = np.array(y)
  n = len(y+x)
  for i in range(iter):
    m_gradient = 0
    b_gradient = 0
    for i in range(n):
      m_gradient += -(2/n) * x[i] * (y[i] - predict(theta, x[i]))
      b_gradient += -(2/n) * (y[i] - predict(theta, x[i]))

    theta[1] = theta[1] - alpha * m_gradient
    theta[0] = theta[0] - alpha * b_gradient
  return theta

def showStats():
  messagebox.askokcancel(message="Your Dice Held is: "+str(diceHeld)+"\n and your individual scores are "+str(roundScore))