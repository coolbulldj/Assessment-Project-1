import random
import math

# SETTINGS
yearsToSurive = 10

# Randomize starting variables
NumberOfMines = random.randint(1, 3) + 5
Population = random.randint(1, 60) + 40
Money = (random.randint(1, 50) + 10) * Population
FoodPrice = random.randint(1, 40) + 80
OreProducion = random.randint(1, 40) + 80

currentYear = 0
oreInStorage = 0
currentSafication = 1

OrePrice = 0
MinePrice = 0


def DisplayStateOfAffairs():
    print(f"Current year:{currentYear + 1}")
    print(f"You have {[Population]} people in your colony")
    print(f"You have {NumberOfMines} mines in your colony")
    print(f"Your mines produced {OreProducion * NumberOfMines} tons of ore")
    print(f"You now have {oreInStorage + OreProducion * NumberOfMines} tons of ore")
    print(f"Current Balance {Money}")
    print("Selling Prices;")
    print(f"Each mining is currently selling/buying for {MinePrice}")
    print(f"Each ton of ore is currently selling for {OrePrice}")


def GetInt(DisplayString):
    a = input(DisplayString)

    try:
        a = int(a)
    except Exception:
        print("Please enter valid interger")
        return None

    return a


def SellItems():
    global oreInStorage
    global NumberOfMines
    global Money

    OreToSell = 10000

    while True:
        OreToSell = GetInt("How much ore do you want to sell? ")
        if OreToSell is None:
            continue

        if OreToSell <= oreInStorage:
            break
        print("You do not have that much ore to sell")

    oreInStorage -= OreToSell
    Money += OreToSell * OrePrice

    MinesToSell = 10000
    while True:
        MinesToSell = GetInt(
            "How many mines do you want to sell? "
        )  # "How many mines do you want to sell? "

        if MinesToSell is None:
            continue

        if MinesToSell <= NumberOfMines:
            break
        # print(MinesToSell, NumberOfMines)
        print("You do not have that many mines to sell")

    NumberOfMines -= MinesToSell
    Money += MinesToSell * MinePrice


def BuyItems():
    global currentSafication
    global NumberOfMines
    global Money

    FoodToBuy = 10000

    while True:
        FoodToBuy = GetInt("How much food do you want to buy? ((Appox. 100$ EA.)")
        if not FoodToBuy:
            continue

        if FoodToBuy <= Money:
            break
        print("You do not have enough money to buy that much food!")

    Money -= FoodToBuy

    currentSafication += (FoodToBuy / Population) - 1

    MinesToBuy = 10000
    while True:
        MinesToBuy = GetInt(
            "How many mines do you want to buy? "
        )  # "How many mines do you want to sell? "

        if not MinesToBuy:
            continue

        if MinesToBuy * MinePrice <= Money:
            break
        print("You do not have enough money to buy that many mines!")

    NumberOfMines += MinesToBuy
    Money -= MinesToBuy * MinePrice


while True:
    currentYear += 1
    # Randomise Ore & Mine price
    OrePrice = random.randint(1, 12) + 7
    MinePrice = random.randint(1, 2000) + 2000

    DisplayStateOfAffairs()
    # Add ore produced
    oreInStorage += OreProducion * NumberOfMines
    SellItems()
    print(f"Current Balance {Money}")
    BuyItems()
    # Apply effects of satifaction value
    if currentSafication > 1.1:
        OreProducion += random.randint(1, 20) + 1
    elif currentSafication < 0.9:
        OreProducion -= random.randint(1, 20) + 1

    # Events
    if random.random() < 0.05:
        print("Radioactive leak .... many die")
        Population /= 2
        Population = math.floor(Population)
    if OreProducion > 150:
        print("Market Glut - Ore price drops")
        OrePrice /= 2
        OrePrice = math.floor(OrePrice)

    # Ways to lose
    if currentSafication < 0.6:
        print("Your people revolted")
        break
    elif Population / NumberOfMines < 10:
        print(
            "Your've overworked your population you require ten people per each of your mines"
        )
        break
    elif Population < 30:
        print("You don't have enough people left")
        break

    if currentYear == yearsToSurive:
        print(f"Your've surived your {yearsToSurive} terms in office")
        break
