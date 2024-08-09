# The Long Road

# Libraries
from random import randint

# VIBECHECK

road = ["forest","woods","path","trail","lane","avenue","road","highway"]
roadflavor = ["The forest around you is rather difficult to traverse, you are truely in the wild now"
              " a simple path snakes its way between the trees and brambles, who knows what could be in these woods...",
              "The woods are pleasent to travel through though the lack of any real road makes things difficult at times"
              " you are alone except for the birds, however, you can't help but fear the possibility of bandits or wolves...",
              "The path stretches out before you, travel is not to difficult but the road is anything but maintained"
              " the land is plain for the most part, nuture prevails over any human influence, but the occational farm is seen",
              "A main trail, well used by traders like you, but rather distant from civilization, you see people,"
              " and pass them on your way, while the route is civilized the land around it is not",
              "The wagon track before you is well used, but not well maintained, you pass farmers and pilgrams but they simply"
              " grunt a greeting and move on, you see farms occationally, but wild animals just as often",
              "This maintained road is fairly basic, but there are not many potholes to be found, even the trees along the"
              " road are maintained in places, cut for wattle or grown for shade.",
              "This road is well used and even paved, people from many places travel on this road as it surely leads somewhere,"
              " it is patroled to keep bandits and beasts from causing issues, though usually by curruptable mercenary guards",
              "This is a main streach of royal road, it is multiple lanes wide to facilitate the common comings and goings along it,"
              " mercinary guards are fairly common among those seen on the road, these roads are kept safe and crime free, but taxes are common"]

post = ["tradepost","hamlet","village","fort","town","castle","city","metropolis"]
postflavor = ["A trade post in the wilderness, only traders and wanderers can be found here, a good place to pick up fur and wood",
              "A tiny hamlet in the wilderness, farmers go about their days, children come up to you eager to hear about distant lands",
              "A quaint village: crafts people and farmers looking to sell you their wares and wheat in return for your wonderous goods",
              "A small walled structure in the wilderness: soldiers, explorers, and traders keep this place and the surrounding land secure",
              "A town: a few streets bustling with activity surrounded by farms, some rich folks live here too, a good place to set up shop for a bit",
              "A castle: this strong fortified structure and its many men hold claim to these lands, it doesnt produce much but safety, always looking for supplies",
              "A city: this bustling place is full of trade, high and low people looking to buy and sell, soldiers to keep order, and beggars grasping for coin",
              "A bustling metropolis: surely anything the heart desires could be found in such a place, hordes from all over find their way here to trade"]

vibeflavor = ["This is a place of peace",
              "The sun shines and the birds sing",
              "Nothing seems out of the ordinary",
              "Something is off... you feel like you are being watched",
              "This is an awful place, evil lurks all around..."]

arcaneflavor = ["Things are quite mundane",
                "The breeze whistles crisply",
                "The sky is truely beautiful",
                "The hair stands on the back of your neck,",
                "The air hums with magic"]


civ = 2
vibe = 2    
arcane = 2
    


def check(old,x,little,big):
    new = old+randint(little,big)
    if new > x:
        new = x
    if new < 0:
        new = 0
    return(new)



# Caravan #

class unit:
  def __init__(self, name, price, weight, cap, strength, speed, pay, rations, grain, edible):
    self.name = name
    self.price = price
    self.weight = weight
    self.cap = cap
    self.pay = pay
    self.rations = rations
    self.speed = speed
    self.strength = strength
    self.grain = grain
    self.edible = edible

# Employees
porter = unit("Porter", 1, 1, 3, 0, 5, 1, 1, 0, False)
merc = unit("Mercenary Guard", 10, 1, 0, 0, 5, 3, 1, 0, False)
adventurer = unit("Adventurer", 50, 1, 0, 0, 5, 10, 1, 0, False)

# Fighting Beasts
ratdog = unit("Rat Dog", 1, 1, 0, 0, 6, 0, 1, 0, True)
wolfdog = unit("Wolf Dog", 10, 3, 0, 1, 10, 0, 2, 0, True)
beardog = unit("Bear Dog", 25, 5, 1, 2, 10, 0, 3, 0, True)

# Ordinary Beasts
goat = unit("Goat", 2, 2, 0, 1, 6, 0, 0, 0, True)
donkey = unit("Donkey", 5, 5, 5, 5, 7, 0, 0, 1, True)
horse = unit("Horse", 25, 10, 10, 15, 10, 0, 0, 2, True)
mule = unit("Mule", 25, 10, 25, 10, 7, 0, 0, 2, True)
ox = unit("Ox", 30, 15, 30, 20, 6, 0, 0, 3, True)

# Exotic Beasts
ostrich = unit("Ostrich", 10, 5, 1, 5, 10, 0, 0, 1, True)
camel = unit("Camel", 30, 15, 50, 10, 6, 0, 0, 1, True)
elephant = unit("Elephant", 100, 50, 50, 50, 5, 0, 0, 10, True)


# Arcane Creatures
goblin = unit("Suitcase Goblin", 10, 1, 1, 0, 5, 0, 0, 0, False)
skeletonhorse = unit("Skeleton Horse", 100, 10, 10, 15, 10, 0, 0, 0, False)
grub = unit("Milk Grub", 10, 1, 0, 0, 4, 0, 1, 1, True)
bloatedgrub = unit("Bloated Milk Grub", 100, 2, 0, 0, 3, 0, -10, 1, True)
shambler = unit("Shambler", 100, 5, 0, 10, 7, 0, 0, -1, False)
bogboar = unit("Bog Boar", 10, 25, 5, 5, 5, 0, 5, 0, True)

# Mega Beasts
snail = unit("Giant Snail", 1500, 250, 1000, 0, 1, 0, 0, 5, True)
walkinghut = unit("Walking Hut", 2500, 250, 100, 0, 15, 0, 0, 0, False)


# Vehicles #

class vehicle:
  def __init__(self, name, price, weight, cap):
    self.name = name
    self.price = price
    self.weight = weight
    self.cap = cap


travois = vehicle("Travois", 5, 1, 1)
cart = vehicle("Cart", 50, 5, 10)
wagon = vehicle("Wagon", 150, 10, 25)
heavywagon = vehicle("Heavy Wagon", 250, 20, 50)
ballista = vehicle("Ballista Wagon", 500, 10, 0)
carrage = vehicle("Carrage", 250, 10, 10)


# Goods #

class good:
    def __init__(self, name, value, stability, spoilage):
        self.name = name
        self.value = value
        self.spoilage = spoilage


# Food #

fruit = good("Fruit", 3, 50, 50)
meat = good("Meat", 5, 50, 25)
grain = good("Grain", 1, 25, 10)
herbs = good("Herbs", 10, 50, 25)
spices = good("Spices", 100, 75, 5)

# Wilderness #

wood = good("Wood", 2, 100, 5)
fur = good("Fur", 25, 50, 5)
ore = good("Ore", 1, 100, 0)
silver = good("Silver", 100, 10, 0)
copper = good("Copper", 10, 10, 0)

# Civilized #

weapons = good("Weapons", 10, 50, 0)
tools = good("Tools", 5, 50, 0)


# Ominous #

# auspicuous #

# Magical #

Tome = good("Arcane Tome", 100, 100, 1)




# Initialize #
Gold = 10
Rations = 10

Caravan = {}

Inventory = {}

# Main Loop #

while True:
    
    # Road #########################################################################################
    
    civ = check(civ,7,-2,2)
    print(roadflavor[civ])
    vibe = check(vibe,4,-1,1)
    print(vibeflavor[vibe])
    arcane = check(arcane,4,-1,1)
    print(arcaneflavor[arcane])
    print(arcane)
    input("what do you do? ")













    

    # Post ###########################################################################################
    
    civ = check(civ,7,-2,2)
    print(postflavor[civ])
    vibe = check(vibe,4,-1,1)
    print(vibeflavor[vibe])
    vibe = check(arcane,4,-1,1)
    print(arcaneflavor[arcane])
    print(arcane)
    input("what do you do? ")




