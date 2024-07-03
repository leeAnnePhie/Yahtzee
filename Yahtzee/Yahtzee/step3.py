scoringOptions = [
    "Ones",
    "Twos",
    "Threes",
    "Chance"
]


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


for i in range(4):
    makeScoreSelection()

