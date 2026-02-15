import pygame as py
import sys
import time

# Classes
from Classes.GUIClasses.TextLabel import TextLabel
from Classes.GUIClasses.Image import Image
from Classes.GUIClasses.Textbox import Textbox
from Classes.GUIClasses.ImageButton import ImageButton

# Services / Modules
from Services.InputService import FireKeyPress, FireKeyRelease
from Display import TickDisplay


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

# Text labels

# Headers
SOALabel = TextLabel((0.4, 0.2), (0.15, 0.1), (0, 0, 0), 1, (0, 0, 0), "SF Pro", 1, 2)
SOALabel.Text = "State Of Affairs"
# MarketsLabel = TextLabel(
#     (0.5, 0.2), (0.1, 0.1), (0, 0, 0), 1, (0, 0, 0), "SF Pro", 1, 2
# )
# MarketsLabel.Text = "Markets"
DecisionsLabel = TextLabel(
    (0.65, 0.2), (0.1, 0.1), (0, 0, 0), 1, (0, 0, 0), "SF Pro", 1, 2
)
DecisionsLabel.Text = "Decisions"

#State Of Affairs
currentTermLabel = TextLabel((0.35, 0.5), (0.1, 0.1), (0, 0, 0), 1, (255, 255, 255))
PopulationLabel = TextLabel((0.35, 0.5), (0.1, 0.1), (0, 0, 0), 1, (255, 255, 255))
currentSatifactionLabel = TextLabel(
    (0.35, 0.5), (0.1, 0.1), (0, 0, 0), 1, (255, 255, 255)
)
NumberOfMinesLabel = TextLabel((0.35, 0.5), (0.1, 0.1), (0, 0, 0), 1, (255, 255, 255))
OreProductionLabel = TextLabel((0.5, 0.5), (0.1, 0.1), (0, 0, 0), 1, (255, 255, 255))
OreInStorageLabel = TextLabel((0.5, 0.5), (0.1, 0.1), (0, 0, 0), 1, (255, 255, 255))

currentTermLabel.Text = "Current Term: 10"
PopulationLabel.Text = "Population:2,175"
currentSatifactionLabel.Text = "Population Satifaction: 1"
NumberOfMinesLabel.Text = "Mines Owned:100"
OreProductionLabel.Text = "Ore Production Rate:34"
OreInStorageLabel.Text = "Ore In Storage:8789(tons)"

# Pricing
# FoodPriceLabel = TextLabel((0.5, 0.3), (0.15, 0.1), (0, 0, 0), 1, (255, 255, 255))
# OrePriceLabel = TextLabel((0.5, 0.4), (0.15, 0.1), (0, 0, 0), 1, (255, 255, 255))
# MinesPriceLabel = TextLabel(
#     (0.5, 0.5), (0.15, 0.1), (0, 0, 0), 1, (0, 0, 0), "monospace", 1, 2
# )

# FoodPriceLabel.Text = "Food Price:100$"
# OrePriceLabel.Text = "Ore Price:50$"
# MinesPriceLabel.Text = "Mine Price:250$"


# Purchasing Labels
CurrentBalLabel  = TextLabel(
        (0.65, 0.25), (0.2, 0.2), (0, 0, 0), 1, (0, 0, 0), "monospace", 1, 2
    )
RemainingBalLabel  = TextLabel(
        (0.65, 0.5), (0.2, 0.2), (0, 0, 0), 1, (0, 0, 0), "monospace", 1, 2
    )
CurrentBalLabel.Text = "Current Balance: 1000$"
RemainingBalLabel.Text = "Remaining Balance: 0$"
while True:
    BuyMinesLabel = TextLabel(
        (0.65, 0.3), (0.1, 0.1), (0, 0, 0), 1, (0, 0, 0), "monospace", 1, 2
    )
    SellMinesLabel = TextLabel(
        (0.65, 0.35), (0.1, 0.1), (0, 0, 0), 1, (0, 0, 0), "monospace", 1, 2
    )
    SellOreLabel = TextLabel(
        (0.65, 0.4), (0.1, 0.1), (0, 0, 0), 1, (0, 0, 0), "monospace", 1, 2
    )
    BuyFoodLabel = TextLabel(
        (0.65, 0.45), (0.1, 0.1), (0, 0, 0), 1, (0, 0, 0), "monospace", 1, 2
    )
    SellOreLabel.Text = "Sell Ore:"
    SellMinesLabel.Text = "Sell Mines:"
    BuyMinesLabel.Text = "Buy Mines:"
    BuyFoodLabel.Text = "Buy Food:"

    break


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

    currentTime = time.time()
    dt = currentTime - LastFrameTime
    ElapedTime += dt
    TickDisplay(dt)
    # print(dt, ElapedTime)
    LastFrameTime = currentTime
