import pygame as py
import sys
import time
import random
import math


# Services / Modules
from Services.InputService import FireKeyPress, FireKeyRelease
import Display
from Classes.GUIClasses.Button import getButtonList
from Classes.GUIClasses.Textbox import Textbox
import Services.UIService as UIService
import Services.DataService as DataService

UIService.SOALabel.Text = "State Of Affairs"
UIService.MarketsLabel.Text = "Markets"
UIService.DecisionsLabel.Text = "Decisions"

UIService.currentTermLabel.Text = "Current Term: 10"
UIService.PopulationLabel.Text = "Population, is ending world hunger"
UIService.currentSatifactionLabel.Text = "Population Satifaction: 1"
UIService.NumberOfMinesLabel.Text = "Mines Owned:100"
UIService.OreProductionLabel.Text = "Ore Production Rate:34"
UIService.OreInStorageLabel.Text = "Ore In Storage:8789(tons)"

UIService.FoodPriceLabel.Text = "Food Price:100$"
UIService.OrePriceLabel.Text = "Ore Price:50$"
UIService.MinesPriceLabel.Text = "Mine Price:250$"

UIService.CurrentBalLabel.Text = "Current Balance: 1000$"
UIService.RemainingBalLabel.Text = "Remaining Balance: 0$"


# Variables
NumberOfMines = random.randint(1, 3) + 5
Population = random.randint(1, 60) + 40
Money = (random.randint(1, 50) + 10) * Population
FoodPrice = random.randint(1, 40) + 80
OreProducion = random.randint(1, 40) + 80

YEARS_TO_SURIVE = 10

DEFAULT_SCREEN = "Assets\Background\SpaceMinesBGv3.png"

#Loss Screens
OVERWORK_LOSS_SCREEN = "Assets\Background\LoseScreens\OverworkedPopulationSpaceColony.png"
REVOLT_LOSS_SCREEN = "Assets\Background\LoseScreens\SpaceColonyRevolt.png"
NOT_ENOUGH_PEOPLE_SCREEN = r"Assets\Background\LoseScreens\NotEnoughPeopleSpaceColony.png"

currentYear = 0
oreInStorage = 0
currentSafication = 1

OrePrice = 0
MinePrice = 0

running = True


def DisplayStateOfAffairs():
    UIService.currentTermLabel.Text = "Current Term:" + str(currentYear + 1)
    UIService.PopulationLabel.Text = "Population:" + str(Population)
    UIService.NumberOfMinesLabel.Text = "Mines owned:" + str(NumberOfMines)
    UIService.OreProductionLabel.Text = (
        "Each Mine Produces:" + str(OreProducion) + " tons of ore"
    )
    UIService.OreInStorageLabel.Text = "Ore In Storage:" + str(oreInStorage)
    UIService.CurrentBalLabel.Text = "Current Balance:" + str(Money)

    UIService.MinesPriceLabel.Text = "Mine Selling Price:" + str(MinePrice) + "$"
    UIService.OrePriceLabel.Text = "Ore Selling Price:" + str(OrePrice) + "$"
    UIService.FoodPriceLabel.Text = "Food Price:" + str(FoodPrice) + "$"
    # print(f"Current year:{currentYear + 1}")
    # print(f"You have {[Population]} people in your colony")
    # print(f"You have {NumberOfMines} mines in your colony")
    # print(f"Your mines produced {OreProducion * NumberOfMines} tons of ore")
    # print(f"You now have {oreInStorage + OreProducion * NumberOfMines} tons of ore")
    # print(f"Current Balance {Money}")
    # print("Selling Prices;")
    # print(f"Each mining is currently selling/buying for {MinePrice}")
    # print(f"Each ton of ore is currently selling for {OrePrice}")


def AttemptToGetInt(IntString):
    a = -1
    try:
        a = int(IntString)
    except Exception:
        pass
    return a


def UpdateTransactionBalance(_):
    # Prevents recursion from TB.TextLabel.Text = ""
    # if str(UIService.)
    RemainingBal = Money

    def CheckItem(TB: Textbox, Price, Buying: bool, MaxItemsInTransaction):
        if TB.Textlabel.Text == "":  # The textlabel isn't real
            return 0
        nonlocal RemainingBal

        ItemsInTransaction = AttemptToGetInt(TB.Textlabel.Text)
        ItemCost = ItemsInTransaction * Price
        # print(((ItemCost) > RemainingBal), Buying)
        # print(((ItemCost) > RemainingBal) == Buying)
        if ItemsInTransaction < 0:
            # Error occurred
            TB.Textlabel.Text = ""
            return 0
        elif ItemsInTransaction > MaxItemsInTransaction:
            ItemsInTransaction = MaxItemsInTransaction
            ItemCost = ItemsInTransaction * Price
            TB.Textlabel.Text = f"{MaxItemsInTransaction}"
            # DEBUGGING
            # print(f"<<<{TB.Name}>>>")
            # print(ItemsInTransaction, "Items in transactions")
            # print(ItemCost, "max", MaxItemsInTransaction)
            # print("<<<END>>>")

        if Buying:
            RemainingBal -= ItemCost
        else:
            RemainingBal += ItemCost

        return ItemsInTransaction

    global NumberOfMines
    global oreInStorage
    global currentSafication

    # NumberOfMines -= CheckItem(UIService.SellMinesTB, MinePrice, False, NumberOfMines)
    # oreInStorage -= CheckItem(UIService.SellOreTB, OrePrice, False, oreInStorage)
    # NumberOfMines += CheckItem(UIService.BuyMinesTB, MinePrice, True, math.floor(RemainingBal / MinePrice))
    # currentSafication += CheckItem(UIService.SellMinesTB, FoodPrice, True, math.floor(RemainingBal / FoodPrice)) / Population - 1
    CheckItem(UIService.SellMinesTB, MinePrice, False, NumberOfMines)
    CheckItem(UIService.SellOreTB, OrePrice, False, oreInStorage)
    CheckItem(
        UIService.BuyMinesTB, MinePrice, True, math.floor(RemainingBal / MinePrice)
    )
    CheckItem(
        UIService.BuyFoodTB, FoodPrice, True, math.floor(RemainingBal / FoodPrice)
    )

    UIService.RemainingBalLabel.Text = f"Remaining Balance:{RemainingBal}"


def SaveData():
    DataService.writeData(
        {
            "NumberOfMines": NumberOfMines,
            "Population": Population,
            "Money": Money,
            "FoodPrice": FoodPrice,
            "OreProducion": OreProducion,
            "currentYear": currentYear,
            "oreInStorage": oreInStorage,
            "currentSafication": currentSafication,
            "OrePrice": OrePrice,
            "MinePrice": MinePrice,
        }
    )

def LoadData():
    data = DataService.readData()


UIService.SellMinesTB.Textlabel.GetPropertyChangedSignal("Text").Connect(
    UpdateTransactionBalance
)
UIService.SellOreTB.Textlabel.GetPropertyChangedSignal("Text").Connect(
    UpdateTransactionBalance
)
UIService.BuyMinesTB.Textlabel.GetPropertyChangedSignal("Text").Connect(
    UpdateTransactionBalance
)
UIService.BuyFoodTB.Textlabel.GetPropertyChangedSignal("Text").Connect(
    UpdateTransactionBalance
)


def ProcessTranactions():
    global Money
    RemainingBal = Money

    def CheckItem(TB: Textbox, Price, Buying: bool, MaxItemsInTransaction):
        if TB.Textlabel.Text == "":  # The textlabel isn't real
            return 0
        nonlocal RemainingBal

        ItemsInTransaction = AttemptToGetInt(TB.Textlabel.Text)
        ItemCost = ItemsInTransaction * Price
        # print(((ItemCost) > RemainingBal), Buying)
        # print(((ItemCost) > RemainingBal) == Buying)
        if ItemsInTransaction < 0:
            # Error occurred
            TB.Textlabel.Text = ""
            return 0
        elif ItemsInTransaction > MaxItemsInTransaction:
            ItemsInTransaction = MaxItemsInTransaction
            ItemCost = ItemsInTransaction * Price
            TB.Textlabel.Text = f"{MaxItemsInTransaction}"
            # DEBUGGING
            # print(f"<<<{TB.Name}>>>")
            # print(ItemsInTransaction, "Items in transactions")
            # print(ItemCost, "max", MaxItemsInTransaction)
            # print("<<<END>>>")

        if Buying:
            RemainingBal -= ItemCost
        else:
            RemainingBal += ItemCost

        return ItemsInTransaction

    global NumberOfMines
    global oreInStorage
    global currentSafication

    NumberOfMines -= CheckItem(UIService.SellMinesTB, MinePrice, False, NumberOfMines)
    oreInStorage -= CheckItem(UIService.SellOreTB, OrePrice, False, oreInStorage)
    NumberOfMines += CheckItem(
        UIService.BuyMinesTB, MinePrice, True, math.floor(RemainingBal / MinePrice)
    )
    currentSafication += (
        CheckItem(
            UIService.SellMinesTB, FoodPrice, True, math.floor(RemainingBal / FoodPrice)
        )
        / Population
        - 1
    )

    Money = RemainingBal

    return True

    



def DisplayMenuOptions():
    # Background stays visible
    UIService.BackgroundImage.Visible = True
    #print(UIService.BackgroundImage.Visible)
    UIService.QuitB.Visible = True
    UIService.NewGameB.Visible = True
    UIService.ContinueB.Visible = True
    UIService.ErrorLabel.Visible = True

    # Hide everything else
    UIService.GlassFrame.Visible = False

    UIService.SOALabel.Visible = False
    UIService.MarketsLabel.Visible = False
    UIService.DecisionsLabel.Visible = False

    UIService.currentTermLabel.Visible = False
    UIService.PopulationLabel.Visible = False
    UIService.NumberOfMinesLabel.Visible = False
    UIService.OreProductionLabel.Visible = False
    UIService.OreInStorageLabel.Visible = False
    UIService.currentSatifactionLabel.Visible = False

    UIService.FoodPriceLabel.Visible = False
    UIService.OrePriceLabel.Visible = False
    UIService.MinesPriceLabel.Visible = False

    UIService.CurrentBalLabel.Visible = False
    UIService.RemainingBalLabel.Visible = False

    UIService.SellMinesLabel.Visible = False
    UIService.SellOreLabel.Visible = False
    UIService.BuyMinesLabel.Visible = False
    UIService.BuyFoodLabel.Visible = False

    UIService.SellMinesTB.Visible = False
    UIService.SellOreTB.Visible = False
    UIService.BuyMinesTB.Visible = False
    UIService.BuyFoodTB.Visible = False

    UIService.NextTermB.Visible = False

def DisplayLossOptions():
    DisplayMenuOptions()
    UIService.ContinueB.Visible = True

def GoToNextTerm(StartingGame: bool = None):
    if not StartingGame and not ProcessTranactions():
        return

    global currentYear
    global OrePrice
    global MinePrice
    global oreInStorage
    global OreProducion
    global running

    # Ensure all values
    currentYear += 1
    # Randomise Ore & Mine price
    OrePrice = random.randint(1, 12) + 7
    MinePrice = random.randint(1, 2000) + 2000

    # Add ore produced
    oreInStorage += OreProducion * NumberOfMines

    DisplayStateOfAffairs()

    # Reset Textbox Values

    if currentSafication > 1.1:
        OreProducion += random.randint(1, 20) + 1
    elif currentSafication < 0.9:
        OreProducion -= random.randint(1, 20) + 1

    # Ways to lose (implement later)
    if currentSafication < 0.6:
        UIService.ErrorLabel.Text = "Your people revolted!"
        UIService.BackgroundImage.ImagePath = REVOLT_LOSS_SCREEN
        DisplayLossOptions()
    elif Population / NumberOfMines < 10:
        UIService.ErrorLabel.Text = "Your've overworked your population you require ten people per each of your mines"
        UIService.BackgroundImage.ImagePath = OVERWORK_LOSS_SCREEN
        DisplayLossOptions()
    elif Population < 30:
        UIService.ErrorLabel.Text = "You don't have enough people left"
        UIService.BackgroundImage.ImagePath = NOT_ENOUGH_PEOPLE_SCREEN
        DisplayLossOptions()

    if currentYear == YEARS_TO_SURIVE:
        UIService.ErrorLabel.Text = (
            f"Your've surived your {YEARS_TO_SURIVE} terms in office"
        )


UIService.NextTermB.MouseUp.Connect(GoToNextTerm)
GoToNextTerm(True)


# 0.875


def main():
    LastFrameTime = time.time()

    ElapedTime = 0

    FPS_CAP = 60

    global running, screen
    while running:
        # print("running")
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
        Display.TickDisplay()

        LastFrameTime = currentTime

        time.sleep(max(1 / FPS_CAP - dt, 0))

main()