import pygame as py
import sys
import time
import random
# Classes
from Classes.GUIClasses.TextLabel import TextLabel
from Classes.GUIClasses.Image import Image
from Classes.GUIClasses.Textbox import Textbox
from Classes.GUIClasses.TextButton import TextButton

# Services / Modules
from Services.InputService import FireKeyPress, FireKeyRelease
import Display
from Classes.GUIClasses.Button import getButtonList


py.init()


# Backgrounds
BackgroundImage = Image(
    (0.5, 0.5),
    (1, 1),
    (200, 200, 0),
    0,
    "Assets\Background\SpaceMinesBGv3.png",
    zIndex=-1,
)

GlassFrame = Image(
    (0.5, 0.375),
    (0.5176, 0.4745),
    (200, 200, 0),
    1,
    r"Assets\Background\GlassFramev2.png",
    zIndex=0,
)

# Status = Image(
#     (0.5, 0.5), (1, 1), (200, 200, 0, 0), "Assets\MetalTexture.jpg", zIndex=1
# )

# NextTermButton = ImageButton(
#     (0.5, 0.5), (0.25, 0.25), (200, 200, 0, 0), r"Assets\NextTermB.png", zIndex=1
# )
HEADERTEXTCOLOR = (0, 0, 0)

REGULAR_TEXT_COLOR = (50, 50, 50)

# Text labels

# Headers
SOALabel = TextLabel(
    (0.4, 0.2), (0.15, 0.1), HEADERTEXTCOLOR, 1, (0, 0, 0), "SF Pro", 1, 2
)
SOALabel.Text = "State Of Affairs"
MarketsLabel = TextLabel(
    (0.485, 0.28), (0.1, 0.1), (0, 0, 0), 1, HEADERTEXTCOLOR, "SF Pro", 1, 2
)
MarketsLabel.Text = "Markets"
DecisionsLabel = TextLabel(
    (0.65, 0.2), (0.1, 0.1), (0, 0, 0), 1, HEADERTEXTCOLOR, "SF Pro", 1, 2
)
DecisionsLabel.Text = "Decisions"

# State Of Affairs
currentTermLabel = TextLabel(
    (0.33, 0.25), (0.15, 0.1), (0, 0, 0), 1, REGULAR_TEXT_COLOR
)
PopulationLabel = TextLabel((0.33, 0.3), (0.15, 0.1), (0, 0, 0), 1, REGULAR_TEXT_COLOR)
currentSatifactionLabel = TextLabel(
    (0.33, 0.5), (0.15, 0.1), (0, 0, 0), 1, REGULAR_TEXT_COLOR
)
NumberOfMinesLabel = TextLabel(
    (0.33, 0.35), (0.15, 0.1), (0, 0, 0), 1, REGULAR_TEXT_COLOR
)
OreProductionLabel = TextLabel(
    (0.33, 0.4), (0.15, 0.1), (0, 0, 0), 1, REGULAR_TEXT_COLOR
)
OreInStorageLabel = TextLabel(
    (0.33, 0.45), (0.15, 0.1), (0, 0, 0), 1, REGULAR_TEXT_COLOR
)

currentTermLabel.Text = "Current Term: 10"
PopulationLabel.Text = "Population:2,175"
currentSatifactionLabel.Text = "Population Satifaction: 1"
NumberOfMinesLabel.Text = "Mines Owned:100"
OreProductionLabel.Text = "Ore Production Rate:34"
OreInStorageLabel.Text = "Ore In Storage:8789(tons)"

# Pricing
FoodPriceLabel = TextLabel((0.485, 0.35), (0.15, 0.1), (0, 0, 0), 1, REGULAR_TEXT_COLOR)
OrePriceLabel = TextLabel((0.485, 0.4), (0.15, 0.1), (0, 0, 0), 1, REGULAR_TEXT_COLOR)
MinesPriceLabel = TextLabel(
    (0.485, 0.45), (0.15, 0.1), (0, 0, 0), 1, REGULAR_TEXT_COLOR, "monospace", 1, 2
)

FoodPriceLabel.Text = "Food Price:100$"
OrePriceLabel.Text = "Ore Price:50$"
MinesPriceLabel.Text = "Mine Price:250$"


# Purchasing Labels
CurrentBalLabel = TextLabel(
    (0.65, 0.25), (0.2, 0.2), (0, 0, 0), 1, REGULAR_TEXT_COLOR, "monospace", 1, 2
)
RemainingBalLabel = TextLabel(
    (0.65, 0.5), (0.2, 0.2), (0, 0, 0), 1, REGULAR_TEXT_COLOR, "monospace", 1, 2
)
CurrentBalLabel.Text = "Current Balance: 1000$"
RemainingBalLabel.Text = "Remaining Balance: 0$"

ErrorLabel = TextLabel((0.5, 0.7), (0.1, 0.1), (0,0,0), 0, (255, 0, 0), "monospace")

while True:
    BuyMinesLabel = TextLabel(
        (0.65, 0.3), (0.1, 0.1), (0, 0, 0), 1, REGULAR_TEXT_COLOR, "monospace", 1, 2
    )
    SellMinesLabel = TextLabel(
        (0.65, 0.35), (0.1, 0.1), (0, 0, 0), 1, REGULAR_TEXT_COLOR, "monospace", 1, 2
    )
    SellOreLabel = TextLabel(
        (0.65, 0.4), (0.1, 0.1), (0, 0, 0), 1, REGULAR_TEXT_COLOR, "monospace", 1, 2
    )
    BuyFoodLabel = TextLabel(
        (0.65, 0.45), (0.1, 0.1), (0, 0, 0), 1, REGULAR_TEXT_COLOR, "monospace", 1, 2
    )
    SellOreLabel.Text = "Sell Ore:"
    SellMinesLabel.Text = "Sell Mines:"
    BuyMinesLabel.Text = "Buy Mines:"
    BuyFoodLabel.Text = "Buy Food:"

    break

NextTermB = TextButton((0.5, 0.57), (0.15, 0.05), (50, 50, 50), 0, (0, 0, 0))
NextTermB.Text = "Next Term!"

#Variables
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
    currentTermLabel.Text = "Current Term:"+str(currentYear+1)
    PopulationLabel.Text = "Population:"+str(Population)
    NumberOfMinesLabel.Text = "Mines owned:"+str(NumberOfMines)
    OreProductionLabel.Text = "Each Mine Produces:"+str(OreProducion)+" tons of ore"
    OreInStorageLabel.Text = "Ore In Storage:"+str(oreInStorage)
    CurrentBalLabel.Text = "Current Balance:"+str(Money)

    MinesPriceLabel.Text = "Mine Selling Price:"+str(MinePrice)+"$"
    OrePriceLabel.Text = "Ore Selling Price:"+str(OrePrice)+"$"
    FoodPriceLabel.Text = "Food Price:"+str(FoodPrice)+"$"
    # print(f"Current year:{currentYear + 1}")
    # print(f"You have {[Population]} people in your colony")
    # print(f"You have {NumberOfMines} mines in your colony")
    # print(f"Your mines produced {OreProducion * NumberOfMines} tons of ore")
    # print(f"You now have {oreInStorage + OreProducion * NumberOfMines} tons of ore")
    # print(f"Current Balance {Money}")
    # print("Selling Prices;")
    # print(f"Each mining is currently selling/buying for {MinePrice}")
    # print(f"Each ton of ore is currently selling for {OrePrice}")
def UpdateTransactionBalance():
    pass

def ProcessTranactions():
    return False

def GoToNextTerm():
    if not ProcessTranactions():
        return
    
    global currentYear
    global OrePrice
    global MinePrice
    global oreInStorage
    #Ensure all values
    currentYear += 1
    # Randomise Ore & Mine price
    OrePrice = random.randint(1, 12) + 7
    MinePrice = random.randint(1, 2000) + 2000

    # Add ore produced
    oreInStorage += OreProducion * NumberOfMines

    DisplayStateOfAffairs()

    # Ways to lose (implement later)
    # if currentSafication < 0.6:
    #     print("Your people revolted")
    #     break
    # elif Population / NumberOfMines < 10:
    #     print(
    #         "Your've overworked your population you require ten people per each of your mines"
    #     )
    #     break
    # elif Population < 30:
    #     print("You don't have enough people left")
    #     break

    # if currentYear == yearsToSurive:
    #     print(f"Your've surived your {yearsToSurive} terms in office")
    #     break


NextTermB.MouseUp.Connect(GoToNextTerm)


# 0.875

StartTime = time.time()
LastFrameTime = time.time()

ElapedTime = 0

running = True

while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()
            running = False

        if event.type == py.KEYDOWN:
            FireKeyPress(event.key)
            # print("Key pressed:", event.key)
        if event.type == py.KEYUP:
            FireKeyRelease(event.key)
            # print("Key released:", event.key)
        bList = getButtonList()

        if event.type == py.MOUSEBUTTONDOWN:
            for clickCB in bList["MouseDown"]:
                clickCB(Display.screen, event.pos)
        elif event.type == py.MOUSEBUTTONUP:
            for clickCB in bList["MouseUp"]:
                clickCB(Display.screen, event.pos)

        if event.type == py.VIDEORESIZE:
            new_width = event.w
            new_height = int(new_width / Display.ASPECT_RATIO)

            # If height is too large for what user dragged,
            # base it on height instead
            if new_height > event.h:
                new_height = event.h
                new_width = int(new_height * Display.ASPECT_RATIO)

            screen = py.display.set_mode((new_width, new_height), py.RESIZABLE)

    currentTime = time.time()
    dt = currentTime - LastFrameTime
    ElapedTime += dt
    Display.TickDisplay(dt)
    # print(dt, ElapedTime)
    LastFrameTime = currentTime
