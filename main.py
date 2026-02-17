import pygame as py
import sys
import time
import random
# Classes
from Classes.GUIClasses.TextLabel import TextLabel
from Classes.GUIClasses.Image import Image
from Classes.GUIClasses.TextButton import TextButton

# Services / Modules
from Services.InputService import FireKeyPress, FireKeyRelease
import Display
from Classes.GUIClasses.Button import getButtonList
import Services.UIService as UIService

UIService.SOALabel.Text = "State Of Affairs"
UIService.MarketsLabel.Text = "Markets"
UIService.DecisionsLabel.Text = "Decisions"

UIService.currentTermLabel.Text = "Current Term: 10"
UIService.PopulationLabel.Text = "Population:2,175"
UIService.currentSatifactionLabel.Text = "Population Satifaction: 1"
UIService.NumberOfMinesLabel.Text = "Mines Owned:100"
UIService.OreProductionLabel.Text = "Ore Production Rate:34"
UIService.OreInStorageLabel.Text = "Ore In Storage:8789(tons)"

UIService.FoodPriceLabel.Text = "Food Price:100$"
UIService.OrePriceLabel.Text = "Ore Price:50$"
UIService.MinesPriceLabel.Text = "Mine Price:250$"

UIService.CurrentBalLabel.Text = "Current Balance: 1000$"
UIService.RemainingBalLabel.Text = "Remaining Balance: 0$"


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
    print("Next Term")
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


UIService.NextTermB.MouseUp.Connect(GoToNextTerm)


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
