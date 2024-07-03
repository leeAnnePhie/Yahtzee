from tkinter import *
import random
import checkChecks
import PIL.Image
from PIL import Image, ImageTk
from functools import partial
from tkinter import messagebox

from PIL.ImageTk import PhotoImage

rerollCounter = 3
finalScore = 0
rounds = 0

root = Tk()
root.geometry("480x680")

mainSlotOneVar = IntVar()
mainSlotTwoVar = IntVar()
mainSlotThreeVar = IntVar()
mainSlotFiveVar = IntVar()
mainSlotSixVar = IntVar()

# <editor-fold desc="Dice Images">
Unknown = (Image.open("questionmark.png"))
resizedUnknown = Unknown.resize((70, 70))
mainDiceImageUnknown = ImageTk.PhotoImage(resizedUnknown)
resizedUnknownSmall = Unknown.resize((20, 20))
mainUnknownsmall = ImageTk.PhotoImage(resizedUnknownSmall)

diceRollOne = (Image.open("dice-six-faces-one.png"))
resizedOne = diceRollOne.resize((70, 70))
mainDiceImageOne = ImageTk.PhotoImage(resizedOne)
resizedOneSmall = diceRollOne.resize((25, 25))
mainDiceOnesmall = ImageTk.PhotoImage(resizedOneSmall)

diceRollTwo = (Image.open("dice-six-faces-two.png"))
resizedTwo = diceRollTwo.resize((70, 70))
mainDiceImageTwo = ImageTk.PhotoImage(resizedTwo)
resizedTwoSmall = diceRollTwo.resize((25, 25))
mainDiceTwosmall = ImageTk.PhotoImage(resizedTwoSmall)

diceRollThree = (Image.open("dice-six-faces-three.png"))
resizedThree = diceRollThree.resize((70, 70))
mainDiceImageThree = ImageTk.PhotoImage(resizedThree)
resizedThreeSmall = diceRollThree.resize((25, 25))
mainDiceThreesmall = ImageTk.PhotoImage(resizedThreeSmall)

diceRollFour = (Image.open("dice-six-faces-four.png"))
resizedFour = diceRollFour.resize((70, 70))
mainDiceImageFour = ImageTk.PhotoImage(resizedFour)
resizedFourSmall = diceRollFour.resize((25, 25))
mainDiceFoursmall = ImageTk.PhotoImage(resizedFourSmall)

diceRollFive = (Image.open("dice-six-faces-five.png"))
resizedFive = diceRollFive.resize((70, 70))
mainDiceImageFive: PhotoImage = ImageTk.PhotoImage(resizedFive)
resizedFiveSmall = diceRollFive.resize((25, 25))
mainDiceFivesmall = ImageTk.PhotoImage(resizedFiveSmall)

diceRollSix = (Image.open("dice-six-faces-six.png"))
resizedSix = diceRollSix.resize((70, 70))
mainDiceImageSix = ImageTk.PhotoImage(resizedSix)
resizedSixSmall = diceRollSix.resize((25, 25))
mainDiceSixsmall = ImageTk.PhotoImage(resizedSixSmall)
# </editor-fold>

# <editor-fold desc="Frames">
top_frame = Frame(root, height="550", width="480")
top_frame.grid(row=0, column=0)

bottom_frame = Frame(root)
bottom_frame.grid(row=1, column=0)

diceRolls_frame = Frame(bottom_frame, height="100", width="480")
diceRolls_frame.grid(row=0, column=0)

button_frame = Frame(bottom_frame, height="50", width="480")
button_frame.grid(row=1, column=0)


# </editor-fold>

def reRollCmd():
    global rerollCounter
    keptDice = []
    global smallDiceList
    for i, x in listOfDicePosition:
        if x.get() == 0:
            keptDice.append(i)
    for i, x in listOfDicePosition:
        if i in keptDice:
            number = listOfDicePosition.index((i, x))
            rndChoice = random.randint(1, 6)
            newDice = blahblah[rndChoice - 1][0]
            i.configure(image=newDice)
            checkChecks.mainScoreList[number] = rndChoice
            smallDiceList[number] = (blahblah[rndChoice - 1][1])
    rerollCounter = rerollCounter - 1
    rerollButton.configure(text="Rerolls Left: " + str(rerollCounter))
    if rerollCounter == 0:
        rerollButton.configure(state=DISABLED)
    confirmButton.configure(state=ACTIVE)
    for x, y in listOfDicePosition:
        x.configure(state=NORMAL)


def confirmButtonCmd():
    global rerollCounter
    global smallDiceList
    global finalScore
    global rounds
    checkSelectionVar = selectionCheck.get()
    if checkSelectionVar == 0:
        messagebox.showwarning(message="Invalid. Select a checkbox.")
    else:
        for i, (x, y) in checkButtonList.items():
            if checkSelectionVar == x:
                y.configure(state=DISABLED)
                real = selectionList[i]
                column = 0
                for h in range(1, 6):
                    i = Canvas(real, width=25, height=25, bg="lightgrey")
                    i.grid(row=0, column=column, padx=3, pady=0)
                    i.create_image(14, 14, image=smallDiceList[h - 1])
                    column += 1
        rerollCounter = 3
        rerollButton.configure(state=ACTIVE, text="Roll")
        for x, y in listOfDicePosition:
            x.configure(image=mainDiceImageUnknown, state=DISABLED)
            y.set(FALSE)
        checkChecks.selectionFunctions[checkSelectionVar]()
        finalScore = finalScore + checkChecks.TotalScore
        selectionCheck.set(0)
        confirmButton.configure(state=DISABLED)
        totalScore.configure(text="Total Score: "+str(finalScore))
        smallDiceList = [mainUnknownsmall, mainUnknownsmall, mainUnknownsmall, mainUnknownsmall, mainUnknownsmall]
        checkChecks.mainScoreList = [0, 0, 0, 0, 0]
        rounds += 1
        if rounds == 13:
            messagebox.askokcancel(message="You're final score is: "+str(finalScore))
            playAgain = messagebox.askyesno(message="Want to play again?")
            if playAgain == TRUE:
                rounds = 0
                reset()
            else:
                quit()


def reset():
    global finalScore
    finalScore = 0
    selectionCheck.set(1)
    for i, (x, y) in checkButtonList.items():
            y.configure(state=NORMAL)
            real = selectionList[i]
            column = 0
            for h in range(1, 6):
                i = Canvas(real, width=25, height=25, bg="lightgrey")
                i.grid(row=0, column=column, padx=3, pady=0)
                i.create_image(14, 14, image=smallDiceList[h - 1])
                column += 1
    for x, y in listOfDicePosition:
        x.configure(image=mainDiceImageUnknown, state=DISABLED)
        y.set(FALSE)
    totalScore.configure(text="Total Score: "+str(finalScore))
    selectionCheck.set(0)
    confirmButton.configure(state=DISABLED)


# <editor-fold desc="make big dice">
mainDiceSlotOne = Checkbutton(diceRolls_frame, image=mainDiceImageUnknown, variable=mainSlotOneVar, indicatoron=FALSE,
                              activebackground='white',
                              background="grey", width=80, height=80, bg="lightgrey")
mainDiceSlotOne.grid(row=0, column=0)

mainDiceSlotTwo = Checkbutton(diceRolls_frame, image=mainDiceImageUnknown, variable=mainSlotTwoVar, indicatoron=FALSE,
                              activebackground='white',
                              background="grey", width=80, height=80, bg="lightgrey")
mainDiceSlotTwo.grid(row=0, column=1)

mainDiceSlotThree = Checkbutton(diceRolls_frame, image=mainDiceImageUnknown, variable=mainSlotThreeVar, indicatoron=FALSE,
                                activebackground='white',
                                background="grey", width=80, height=80, bg="lightgrey")
mainDiceSlotThree.grid(row=0, column=2)

mainDiceSlotFour = Checkbutton(diceRolls_frame, image=mainDiceImageUnknown, variable=mainSlotFiveVar, indicatoron=FALSE,
                               activebackground='white',
                               background="grey", width=80, height=80, bg="lightgrey")
mainDiceSlotFour.grid(row=0, column=3)

mainDiceSlotFive = Checkbutton(diceRolls_frame, image=mainDiceImageUnknown, variable=mainSlotSixVar, indicatoron=FALSE,
                               activebackground='white',
                               background="grey", width=80, height=80, bg="lightgrey")
mainDiceSlotFive.grid(row=0, column=4)
# </editor-fold>

listOfDice = [
    mainDiceImageOne, mainDiceImageTwo, mainDiceImageThree, mainDiceImageFour, mainDiceImageFive, mainDiceImageSix]
smallDiceList = [mainUnknownsmall, mainUnknownsmall, mainUnknownsmall, mainUnknownsmall, mainUnknownsmall]

blahblah = [(mainDiceImageOne, mainDiceOnesmall), (mainDiceImageTwo, mainDiceTwosmall),
            (mainDiceImageThree, mainDiceThreesmall), (mainDiceImageFour, mainDiceFoursmall),
            (mainDiceImageFive, mainDiceFivesmall), (mainDiceImageSix, mainDiceSixsmall)]

listOfDicePosition = [(mainDiceSlotOne, mainSlotOneVar), (mainDiceSlotTwo, mainSlotTwoVar), (mainDiceSlotThree,
    mainSlotThreeVar), (mainDiceSlotFour, mainSlotFiveVar), (mainDiceSlotFive, mainSlotSixVar)]

labelSelectionList = ["Ones", "Twos", "Threes", "Fours", "Fives", "Sixes", "Three of a Kind", "Four of a Kind",
                      "Fullhouse", "Short Straight", "Long Straight", "Yahtzee", "Chance"]

# <editor-fold desc="radio buttons">
selectionCheck = IntVar()
onesButtonVar = IntVar()
onesButton = Checkbutton(top_frame, variable=selectionCheck, onvalue=1, offvalue=0)
onesButton.grid(row=0, column=2, padx=10, pady=7)

twosButtonVar = BooleanVar()
twosButton = Checkbutton(top_frame, variable=selectionCheck, onvalue=2, offvalue=0)
twosButton.grid(row=1, column=2, padx=10, pady=7)

threesButtonVa = BooleanVar
threesButton = Checkbutton(top_frame, variable=selectionCheck, onvalue=3, offvalue=0)
threesButton.grid(row=2, column=2, padx=10, pady=7)

foursButtonVa = BooleanVar
foursButton = Checkbutton(top_frame, variable=selectionCheck, onvalue=4, offvalue=0)
foursButton.grid(row=3, column=2, padx=10, pady=7)

fivesButtonVa = BooleanVar
fivesButton = Checkbutton(top_frame, variable=selectionCheck, onvalue=5, offvalue=0)
fivesButton.grid(row=4, column=2, padx=10, pady=7)

sixesButtonVa = BooleanVar
sixesButton = Checkbutton(top_frame, variable=selectionCheck, onvalue=6, offvalue=0)
sixesButton.grid(row=5, column=2, padx=10, pady=7)

threeofkindButtonVa = BooleanVar
tokButton = Checkbutton(top_frame, variable=selectionCheck, onvalue=7, offvalue=0)
tokButton.grid(row=6, column=2, padx=10, pady=7)

fourofkindButtonVa = BooleanVar
fokButton = Checkbutton(top_frame, variable=selectionCheck, onvalue=8, offvalue=0)
fokButton.grid(row=7, column=2, padx=10, pady=7)

fullhouseButtonVa = BooleanVar
fullButton = Checkbutton(top_frame, variable=selectionCheck, onvalue=9, offvalue=0)
fullButton.grid(row=8, column=2, padx=10, pady=7)

shortButtonVa = BooleanVar
shortButton = Checkbutton(top_frame, variable=selectionCheck, onvalue=10, offvalue=0)
shortButton.grid(row=9, column=2, padx=10, pady=7)

longButtonVa = BooleanVar
longButton = Checkbutton(top_frame, variable=selectionCheck, onvalue=11, offvalue=0)
longButton.grid(row=10, column=2, padx=10, pady=7)

fiveofkindButtonVa = BooleanVar
fiokButton = Checkbutton(top_frame, variable=selectionCheck, onvalue=12, offvalue=0)
fiokButton.grid(row=11, column=2, padx=10, pady=7)

chanceButtonVa = BooleanVar
chanceButton = Checkbutton(top_frame, variable=selectionCheck, onvalue=13, offvalue=0)
chanceButton.grid(row=12, column=2, padx=10, pady=7)


checkButtonList = {
    "ones": (1, onesButton), "twos": (2, twosButton), "threes": (3, threesButton),
    "fours": (4, foursButton),
    "fives": (5, fivesButton), "sixes": (6, sixesButton),
    "threeofkind": (7, tokButton),
    "fourofkind": (8, fokButton), "fullhouse": (9, fullButton),
    "short": (10, shortButton), "long": (11, longButton),
    "fiveofkind": (12, fiokButton), "chance": (13, chanceButton)
}

# </editor-fold>

# <editor-fold desc="Selection Row">
rowCounter = 0
for items in labelSelectionList:
    selectionLabel_frame = Label(top_frame, text=items)
    selectionLabel_frame.grid(row=rowCounter, column=0, padx=35, pady=5)
    rowCounter += 1

oneSelectionFrame = Frame(top_frame)
oneSelectionFrame.grid(row=0, column=1, padx=20, pady=5)

twoSelectionFrame = Frame(top_frame)
twoSelectionFrame.grid(row=1, column=1, padx=20, pady=5)

threeSelectionFrame = Frame(top_frame)
threeSelectionFrame.grid(row=2, column=1, padx=20, pady=5)

fourSelectionFrame = Frame(top_frame)
fourSelectionFrame.grid(row=3, column=1, padx=20, pady=5)

fiveSelectionFrame = Frame(top_frame)
fiveSelectionFrame.grid(row=4, column=1, padx=20, pady=5)

sixSelectionFrame = Frame(top_frame)
sixSelectionFrame.grid(row=5, column=1, padx=20, pady=5)

threofSelectionFrame = Frame(top_frame)
threofSelectionFrame.grid(row=6, column=1, padx=20, pady=5)

fouofSelectionFrame = Frame(top_frame)
fouofSelectionFrame.grid(row=7, column=1, padx=20, pady=5)

fullSelectionFrame = Frame(top_frame)
fullSelectionFrame.grid(row=8, column=1, padx=20, pady=5)

shortSelectionFrame = Frame(top_frame)
shortSelectionFrame.grid(row=9, column=1, padx=20, pady=5)

longSelectionFrame = Frame(top_frame)
longSelectionFrame.grid(row=10, column=1, padx=20, pady=5)

fivofSelectionFrame = Frame(top_frame)
fivofSelectionFrame.grid(row=11, column=1, padx=20, pady=5)

chanceSelectionFrame = Frame(top_frame)
chanceSelectionFrame.grid(row=12, column=1, padx=20, pady=5)
# </editor-fold>
for x, y in listOfDicePosition:
    x.configure(state=DISABLED)

selectionList = {"ones": oneSelectionFrame,
                 "twos": twoSelectionFrame,
                 "threes": threeSelectionFrame,
                 "fours": fourSelectionFrame,
                 "fives": fiveSelectionFrame,
                 "sixes": sixSelectionFrame,
                 "threeofkind": threofSelectionFrame,
                 "fourofkind": fouofSelectionFrame,
                 "fullhouse": fullSelectionFrame,
                 "short": shortSelectionFrame,
                 "long": longSelectionFrame,
                 "fiveofkind": fivofSelectionFrame,
                 "chance": chanceSelectionFrame}

for x, y in selectionList.items():
    column = 0
    for i in range(1, 6):
        i = Canvas(y, width=25, height=25, bg="lightgrey")
        i.grid(row=0, column=column, padx=3, pady=0)
        i.create_image(14, 14, image=mainUnknownsmall)
        column += 1

rerollButton = Button(button_frame, text="Roll", width=10, command=reRollCmd)
rerollButton.grid(row=0, column=0, padx=20, pady=12)

totalScore = Label(button_frame, text="Total Score: "+str(finalScore))
totalScore.grid(row=0, column=1, padx=20, pady=6)

confirmButton = Button(button_frame, text="Confirm Selection", width=10, command=confirmButtonCmd)
confirmButton.grid(row=0, column=2, padx=20, pady=12)
confirmButton.configure(state=DISABLED)


button_frame.grid_propagate(0)
top_frame.grid_propagate(0)
root.mainloop()
