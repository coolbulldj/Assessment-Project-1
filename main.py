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


# Variables are set to zero because they get initizlized later down the line in different functions
NumberOfMines = 0
Population = 0
Money = 0
FoodPrice = 0
OreProducion = 0



HARD_MODE_YEARS_TO_SURVIVE = 20
NORMAL_MODE_YEARS_TO_SURVIVE = 10
EASY_MODE_YEARS_TO_SURVIVE = 5

yearsToSurvive = NORMAL_MODE_YEARS_TO_SURVIVE



DEFAULT_SCREEN = r"Assets\Background\SpaceMinesBGv3.png"

#Loss Screens
OVERWORK_LOSS_SCREEN = r"Assets\Background\LoseScreens\OverworkedPopulationSpaceColony.png"
REVOLT_LOSS_SCREEN = r"Assets\Background\LoseScreens\SpaceColonyRevolt.png"
NOT_ENOUGH_PEOPLE_SCREEN = r"Assets\Background\LoseScreens\NotEnoughPeopleSpaceColony.png"

currentYear = 0
oreInStorage = 0
currentSatfication = 1

OrePrice = 0
MinePrice = 0

running = True


def DisplayStateOfAffairs():
    UIService.currentTermLabel.Text = "Current Term:" + str(currentYear)
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
    global currentSatfication

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
            "currentSatfication": currentSatfication,
            "OrePrice": OrePrice,
            "MinePrice": MinePrice,
        }
    )

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


def ProcessTranactions(): #Takes the content from the textboxes and converts them to numbers then adds them to connected variable
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
    global currentSatfication

    NumberOfMines -= CheckItem(UIService.SellMinesTB, MinePrice, False, NumberOfMines)
    oreInStorage -= CheckItem(UIService.SellOreTB, OrePrice, False, oreInStorage)
    NumberOfMines += CheckItem(
        UIService.BuyMinesTB, MinePrice, True, math.floor(RemainingBal / MinePrice)
    )
    foodPurchased = CheckItem(
            UIService.BuyFoodTB, FoodPrice, True, math.floor(RemainingBal / FoodPrice)
        )
    #print(foodPurchased, "food purchased")
    currentSatfication += (
        foodPurchased
        / Population
        - 1
    )

    Money = RemainingBal

def UpdateVariables(): #updates variables used after each term
    global currentYear, OrePrice, MinePrice, oreInStorage, OreProducion, Population

    # Ensure all values
    currentYear += 1
    # Randomise Ore & Mine price
    OrePrice = random.randint(1, 12) + 7
    MinePrice = random.randint(1, 2000) + 2000

    # Add ore produced
    oreInStorage += OreProducion * NumberOfMines

    if currentSatfication > 1.1:
        OreProducion += random.randint(1, 20) + 1
        Population += min(Population * (currentSatfication - 1), 15) #ensure population growth can't exceed 15 people
    elif currentSatfication < 0.9:
        OreProducion -= random.randint(1, 20) + 1
        Population -= min(Population * (1 - currentSatfication), 15) #ensure population growth can't exceed 15 people

    OreProducion = max(65, OreProducion) #Ensure ore production per mine doesn't drop below 60


def Events():
    #Events famine, radioactive leak, immgration boom, ore glut, gold rush
    EventRan = random.random()

    eventOccured = False

    if ((OreProducion * NumberOfMines) > 2500 or oreInStorage > 10000) and EventRan <= 0.5: #ore glut 50 percent probality ore glut will occur when production exceed 2500 ore, or ore in storage exceeds 10k
        UIService.ErrorLabel.Text = "Ore Glut price will drop; There is too much ore in circulation consider selling some of your ore or decreasing ore production"
        UIService.ErrorLabel.TextColor = (16, 148, 230) #Blue
        eventOccured = True
    elif EventRan <= 0.55: #5 percent probality, radioactive leak
        UIService.ErrorLabel.Text = "A Radioactive Leak Occurs many will die..."
        UIService.ErrorLabel.TextColor = (6, 209, 60) #green
        eventOccured = True
    elif EventRan <= 0.65: #10 percent probality, immgration boom
        UIService.ErrorLabel.Text = "A Immgration boom occurs population will grow"
        UIService.ErrorLabel.TextColor = (16, 148, 230) #Blue
        eventOccured = True
    elif EventRan <= 0.7: #5 percent probality
        UIService.ErrorLabel.Text = "A gold run occurs population & ore prices skyrockets"
        UIService.ErrorLabel.TextColor = (230, 173, 16) #gold / yellow
        eventOccured = True
    elif EventRan <= 0.75: #5 percent probality
        UIService.ErrorLabel.Text = "A famine occurs population decreases & food prices increase"
        UIService.ErrorLabel.TextColor = (100, 125, 140) #bluey gray
        eventOccured = True


    if eventOccured:
        UIService.ErrorLabel.Visible = True
        time.sleep(3)
        UIService.ErrorLabel.Visible = False
        DisplayStateOfAffairs()

def ToggleAllUIVisiblity(Toggle:bool):
    # Background stays visible
    UIService.BackgroundImage.Visible = Toggle
    #print(UIService.BackgroundImage.Visible)
    UIService.QuitB.Visible = Toggle
    UIService.NewGameB.Visible = Toggle
    UIService.ContinueB.Visible = Toggle
    UIService.ErrorLabel.Visible = Toggle

    # Hide everything else
    UIService.GlassFrame.Visible = Toggle

    UIService.SOALabel.Visible = Toggle
    UIService.MarketsLabel.Visible = Toggle
    UIService.DecisionsLabel.Visible = Toggle

    UIService.currentTermLabel.Visible = Toggle
    UIService.PopulationLabel.Visible = Toggle
    UIService.NumberOfMinesLabel.Visible = Toggle
    UIService.OreProductionLabel.Visible = Toggle
    UIService.OreInStorageLabel.Visible = Toggle
    UIService.currentSatifactionLabel.Visible = Toggle

    UIService.FoodPriceLabel.Visible = Toggle
    UIService.OrePriceLabel.Visible = Toggle
    UIService.MinesPriceLabel.Visible = Toggle

    UIService.CurrentBalLabel.Visible = Toggle
    UIService.RemainingBalLabel.Visible = Toggle

    UIService.SellMinesLabel.Visible = Toggle
    UIService.SellOreLabel.Visible = Toggle
    UIService.BuyMinesLabel.Visible = Toggle
    UIService.BuyFoodLabel.Visible = Toggle

    UIService.SellMinesTB.Visible = Toggle
    UIService.SellOreTB.Visible = Toggle
    UIService.BuyMinesTB.Visible = Toggle
    UIService.BuyFoodTB.Visible = Toggle

    UIService.NextTermB.Visible = Toggle

    UIService.QuitB.Visible = Toggle
    UIService.NewGameB.Visible = Toggle
    UIService.ContinueB.Visible = Toggle

    UIService.HardModeB.Visible = Toggle
    UIService.NormalModeB.Visible = Toggle
    UIService.EasyModeB.Visible = Toggle
    UIService.StartGameB.Visible = Toggle

def StartMenuOptions():
    pass

def HideMenuOptions():
    UIService.QuitB.Visible = False
    UIService.NewGameB.Visible = False
    UIService.ContinueB.Visible = False
    UIService.ErrorLabel.Visible = False

    UIService.EasyModeB.Visible = False
    UIService.NormalModeB.Visible = False
    UIService.HardModeB.Visible = False

    UIService.StartGameB.Visible = False

def DisplayMenuOptions():
    ToggleAllUIVisiblity(False)

    # Background stays visible
    UIService.BackgroundImage.Visible = True
    #print(UIService.BackgroundImage.Visible)
    UIService.QuitB.Visible = True
    UIService.NewGameB.Visible = True
    UIService.ContinueB.Visible = True

def DisplayLossOptions():
    DisplayMenuOptions()
    UIService.ErrorLabel.Visible = True
    UIService.ContinueB.Visible = False

def GoToNextTerm():
    ProcessTranactions()

    global running
    
    UpdateVariables()
    Events()
    DisplayStateOfAffairs()
    
    # Ways to lose (implement later)
    print(Population, "Population")
    print(currentSatfication, "current satfication")
    if currentSatfication < 0.6:
        UIService.ErrorLabel.Text = "Your people revolted! Aim to buy 1 unit of food per person"
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

    if currentYear == (yearsToSurvive+1): #Add one as current year starts a 1 therefore all terms are completed by the year surivived plus 1
        UIService.ErrorLabel.Text = (
            f"Your've surived your {yearsToSurvive} terms in office"
        )
        UIService.ErrorLabel.Text = ()


def QuitGame():
    global running
    running = False

def CreateNewGame():
    ToggleAllUIVisiblity(False)

    UIService.EasyModeB.Visible = True
    UIService.NormalModeB.Visible = True
    UIService.HardModeB.Visible = True

    UIService.StartGameB.Visible = True

def StartNewGame():
    global NumberOfMines, Population, Money, FoodPrice, OreProducion

    ToggleAllUIVisiblity(True)
    HideMenuOptions()

    #Determine Starting variables
    NumberOfMines = random.randint(1, 3) + 5
    Population = random.randint(1, 60) + NumberOfMines * 10
    Money = (random.randint(1, 50) + 10) * Population
    FoodPrice = random.randint(1, 20) + 20
    OreProducion = random.randint(1, 40) + 80

    UpdateVariables()
    DisplayStateOfAffairs()

def LoadPreviousGame():
    global NumberOfMines, Population, Money, FoodPrice, OreProducion, currentYear, oreInStorage, currentSatfication, OrePrice, MinePrice
    data = DataService.readData()

    NumberOfMines = data["NumberOfMines"]
    Population = data["Population"]
    Money = data["Money"]
    FoodPrice = data["FoodPrice"]
    OreProducion = OreProducion["OreProduction"]
    currentYear = data["currentYear"]
    oreInStorage = data["OreInStorage"]
    currentSatfication = data["currentSatfication"]
    OrePrice = data["OrePrice"]
    MinePrice = data["MinePrice"]



#Note these button functions here provide a Callback for button callback list,
#they are then called from the ClickCB in the main loop
UIService.NextTermB.MouseUp.Connect(GoToNextTerm)
UIService.QuitB.MouseUp.Connect(QuitGame)
UIService.NewGameB.MouseUp.Connect(CreateNewGame)
UIService.ContinueB.MouseUp.Connect(LoadPreviousGame)

def EasyMode():
    global yearsToSurvive
    yearsToSurvive = EASY_MODE_YEARS_TO_SURVIVE

def NormalMode():
    global yearsToSurvive
    yearsToSurvive = NORMAL_MODE_YEARS_TO_SURVIVE

def HardMode():
    global yearsToSurvive
    yearsToSurvive = HARD_MODE_YEARS_TO_SURVIVE

UIService.EasyModeB.MouseUp.Connect(EasyMode)
UIService.NormalModeB.MouseUp.Connect(NormalMode)
UIService.HardModeB.MouseUp.Connect(HardMode)

UIService.StartGameB.MouseUp.Connect(StartNewGame)



def main():
    DisplayMenuOptions()
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