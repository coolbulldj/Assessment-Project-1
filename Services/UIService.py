# Classes
from Classes.GUIClasses.TextLabel import TextLabel
from Classes.GUIClasses.Image import Image
from Classes.GUIClasses.TextButton import TextButton
from Classes.GUIClasses.Textbox import Textbox



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

MarketsLabel = TextLabel(
    (0.485, 0.28), (0.1, 0.1), (0, 0, 0), 1, HEADERTEXTCOLOR, "SF Pro", 1, 2
)

DecisionsLabel = TextLabel(
    (0.65, 0.2), (0.1, 0.1), (0, 0, 0), 1, HEADERTEXTCOLOR, "SF Pro", 1, 2
)


# SOALabel.Text = "State Of Affairs"
# MarketsLabel.Text = "Markets"
# DecisionsLabel.Text = "Decisions"

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

# currentTermLabel.Text = "Current Term: 10"
# PopulationLabel.Text = "Population:2,175"
# currentSatifactionLabel.Text = "Population Satifaction: 1"
# NumberOfMinesLabel.Text = "Mines Owned:100"
# OreProductionLabel.Text = "Ore Production Rate:34"
# OreInStorageLabel.Text = "Ore In Storage:8789(tons)"

# Pricing
FoodPriceLabel = TextLabel((0.485, 0.35), (0.15, 0.1), (0, 0, 0), 1, REGULAR_TEXT_COLOR)
OrePriceLabel = TextLabel((0.485, 0.4), (0.15, 0.1), (0, 0, 0), 1, REGULAR_TEXT_COLOR)
MinesPriceLabel = TextLabel(
    (0.485, 0.45), (0.15, 0.1), (0, 0, 0), 1, REGULAR_TEXT_COLOR, "monospace", 1, 2
)

# FoodPriceLabel.Text = "Food Price:100$"
# OrePriceLabel.Text = "Ore Price:50$"
# MinesPriceLabel.Text = "Mine Price:250$"


# Purchasing Labels
CurrentBalLabel = TextLabel(
    (0.65, 0.25), (0.2, 0.2), (0, 0, 0), 1, REGULAR_TEXT_COLOR, "monospace", 1, 2
)
RemainingBalLabel = TextLabel(
    (0.65, 0.5), (0.2, 0.2), (0, 0, 0), 1, REGULAR_TEXT_COLOR, "monospace", 1, 2
)
# CurrentBalLabel.Text = "Current Balance: 1000$"
# RemainingBalLabel.Text = "Remaining Balance: 0$"

ErrorLabel = TextLabel((0.5, 0.7), (0.1, 0.1), (0,0,0), 0, (255, 0, 0), "monospace")

SellMinesLabel = TextLabel(
        (0.65, 0.3), (0.1, 0.1), (0, 0, 0), 1, REGULAR_TEXT_COLOR, "monospace", 1, 2
    )
SellOreLabel = TextLabel(
        (0.65, 0.35), (0.1, 0.1), (0, 0, 0), 1, REGULAR_TEXT_COLOR, "monospace", 1, 2
    )
BuyMinesLabel = TextLabel(
        (0.65, 0.4), (0.1, 0.1), (0, 0, 0), 1, REGULAR_TEXT_COLOR, "monospace", 1, 2
    )
BuyFoodLabel = TextLabel(
        (0.65, 0.45), (0.1, 0.1), (0, 0, 0), 1, REGULAR_TEXT_COLOR, "monospace", 1, 2
    )

SellOreLabel.Text = "Sell Ore:"
SellMinesLabel.Text = "Sell Mines:"
BuyMinesLabel.Text = "Buy Mines:"
BuyFoodLabel.Text = "Buy Food:"

TB_STANDARD_SIZE = (0.04, 0.03)

SellMinesTB = Textbox((0.72, 0.3), TB_STANDARD_SIZE, (255, 255, 0), 0, (0,0,0), "monospace")
SellOreTB = Textbox((0.72, 0.35), TB_STANDARD_SIZE, (255, 255, 0), 0, (0,0,0), "monospace")
BuyMinesTB = Textbox((0.72, 0.4), TB_STANDARD_SIZE, (255, 255, 0), 0, (0,0,0), "monospace")
BuyFoodTB = Textbox((0.72, 0.45), TB_STANDARD_SIZE, (255, 255, 0), 0, (0,0,0), "monospace")

SellMinesTB.Name = "SellMinesTB"
SellOreTB.Name = "SellOreTB"
BuyMinesTB.Name = "BuyMinesTB"
BuyFoodTB.Name = "BuyFoodTB"

NextTermB = TextButton((0.5, 0.57), (0.15, 0.05), (50, 50, 50), 0, (0, 0, 0))
NextTermB.Text = "Next Term!"