#Levi Peachey-Stoner
#ItemAdventure

import random
import time


print("You got lost in a storm far from town last night.")
time.sleep(2)
print("By the time you saw a light in the blizzard it was almost too late.")
time.sleep(2)
print("you stumbled into the cabin and crawled over to the fire place.")
time.sleep(2)
print("you were too delerious to tell if anyone was home.")
time.sleep(2)
print("before long you were asleep.")
time.sleep(2)
print()
time.sleep(2)
print("you wake up shivering, the fire is out.")


def look(things):
    if "fire" in things:
        print("You are in a warm cabin.")
    else:
        print("You are in a cold cabin.")
    print()
    print("You see the following things:")
    for i in things:
        print(i)
    print()

def search(thing):
    print("You search the",thing+".")
    
    if thing=="exit":
        print("When opened a wall of snow and ice is revealed.")
        print("This will not be an escape for a long time.")
        print()
        
    if thing=="fireplace":
        if "fire" not in things:
            print("There is naught but ash and an icy draft from the chimney.")
            print("It would be nice to light the fire at some point.")
            if "chimney" not in things:
                print("You discovered the chimney")
                return("chimney")
            if "match" in inventory and "firewood" in inventory:
                x=input("Do you start a fire with your match and firewood? ")
                if x == "yes" or x=='y' or x == "Yes":
                    print("You started a fire in the fireplace.")
                    return("fire")
                else:
                    print("You remain cold and sad.")
            else:
                print("If you had a match and firewood you could start a fire.")
        else:
            print("A fire burns here warming the cabin.")
        print()

    if thing=="loft":
        print("You climb the ladder to the loft.")
        if "bed" not in things:
            print("You see a bed and a cedar chest, an injured man is sleeping in the bed.")
            print()
            return "bed"
        else:
            print("Nothing much has changed up here.")
        print()

    if thing=="trapdoor":
        print("This heavy trap door likey leads to some under ground space.")
        if "key" not in inventory:
            print("It is locked and will not budge without the key.")
        else:
            x=input("Do you use the key to open the trapdoor?")
            if x == "yes" or x=='y' or x == "Yes":
                print("You open the trap door, it leads down some steps to a cellar.")
                return("cellar")
            else:
                print("ok...")
        print()
    if thing=="chimney":
        if "fire" in things:
            print("But, the fire makes it too hot to look for more than a second.")
        else:
            print("There is nothing of use.")
        print()
        
    if thing=="fire":
        print("The fire burns merrily, warming the cabin")
        if "pot" in inventory:
            x=input("Would you like to use your pot to melt snow into water?")
            if x == "yes" or x=='y' or x == "Yes":
                y=random.randint(1,6)
                if y==1:
                    print("Ooops...")
                    y=random.randint(1,6)
                    if y==1:
                        print("Well, gosh-golly. How terribly unfortunate.")
                        print("You extingish the fire and gain nothing.")
                        return("wetfire")
                    else:
                        print("You extinguish the fire and gather the charcoal.")
                        print ()
                        return("charcoal")
                else:
                    print("You boil some water.")
                    print()
                    return("water")
        if "water" in inventory:
            x=input("Would you like to extinguish the fire with water to obtain charcoal?")
            if x == "yes" or x=='y' or x == "Yes":
                print("You extinguish the fire and gather the charcoal.")
                print ()
                return("charcoal")

    if thing=="bed":
        print("A warm bed comfortable bed.")
        if "floorboard" not in things:
            print("You notice a loose floorboard under the bed.")
            return("floorboard")
        else:
            print("There would be room for two... if you both survive...")

    if thing=="cedar chest":
        print("The box is sturdy and well made, but it is unlocked.")
        if "empty cedar chest" not in things:
            print("There are three peices of cloth and a few matches inside")
            print()
            return ("cedar chest")
        else:
            print("Contains nothing but a lovely smell.")
            print()

    if thing=="injured man":
        print("The man looks like he is usually quite strong and healthy.")
        print("However, he us currently unconcious and in grave peril.")
        print()
        print('You can use the "heal" action to help the poor soul')
        return("healing")
        
        


        print()
    if thing=="cellar":
        pass
    

        print()

def takeinventory(inventory):
    print("you have:")
    for i in inventory:
        print(i)

def heal(x):
    if injury>=7:
        print("The man is dead")
        print()
        return("dead")
    else:
        print("From most to least severe his ailments are:")
        print()
        for i in (injurys[::-1]):
            print(i)
        print()
        print("You must cure his ailments in order of severity")
        print()
        x=input("Do you want to treat him now?")
        if x == "yes" or x=='y' or x == "Yes":
            worst=str(injurys[-1:])[2:-2]
            if "infection"==worst:
                if "medicine" in inventory:
                    x=input("Do you want to treat his infection with medicine?")
                    if x == "yes" or x=='y' or x == "Yes":
                        return("infection")
                    else:
                        return("didnt")
                else:
                    print("You can not treat his infection without medicine.")
                    return("cant")
                    
            elif "animal bite"==worst:
                if "cloth" in inventory:
                    x=input("Do you want to treat his animal bite with a cloth bandage?")
                    if x == "yes" or x=='y' or x == "Yes":
                        return("animal bite")
                    else:
                        return("didnt")
                else:
                    print("You can not treat his animal bite without cloth")
                    return("cant")

            elif "shock"==worst:
                print("You can not treat his shock, it will reduce after a night of rest.")
                return("cant")

            elif "hypothermia"==worst:
                if "soup" in inventory:
                    x=input("Do you want to treat his hypothermia with soup?")
                    if x == "yes" or x=='y' or x == "Yes":
                        return("hypothermia")
                    else:
                        return("didnt")
                else:
                    print("You can not treat his illness without soup")
                    return("cant")
                
            elif "ill"==worst:
                if "charcoal" in inventory:
                    x=input("Do you want to treat his illness with charcoal?")
                    if x == "yes" or x=='y' or x == "Yes":
                        return("ill")
                    else:
                        return("didnt")
                else:
                    print("You can not treat his illness without charcoal")
                    return("cant")
                
            elif "cold"==worst:
                print('If you have the fire burning when you end the day he will automaticaly lose one "cold" injury.')
                if "cloth" in inventory:
                    x=input("Do you want to treat his illness with cloth?")
                    if x == "yes" or x=='y' or x == "Yes":
                        return("cold")
                    else:
                        return("didnt")
                else:
                    print("You can not treat his illness without cloth")
                    return("cant")

                


        else:
            return("no")

    print()

####################################################################################################

inventory=["match","firewood","pot"]
things=["exit","fireplace","loft","trapdoor"]

injury=random.randint(3,6)
injurys=[]
for pain in range(injury):
    x=random.randint(0,6)+pain
    if x<=3:
        if "cold" in injurys:
            injurys.append("ill")
        else:
            injurys.append("cold")
    elif 3<x<=6:
        if "cold" in injurys:
            injurys.append("frostbite")
        else:
            injurys.append("cold")
    elif 6<x<=7:
        injurys.append("shock")
    elif x>7:
        if "animal bite" in injurys:
            injurys.append("infection")
        else:
            injurys.append("animal bite")





alive=True
day=1

####################################################################################################

while alive==True:
    action=input("What do you do? ")
    print()
    if action=="?":
        print("You are currently able to take the following actions:")
        print()
        print("look: to check out your surroundings")
        print("search: to interact with something in your surroundings")
        print("inventory: To check your inventory")
        print()
    if action=="look":
        look(things)
    if action=="search":
        thing=(input("what would you like to search? "))
        print()
        if thing in things:
            discovered=search(thing)
            if discovered==None:
                continue
            elif discovered=="dead":
                alive=False
            elif discovered=="water":
                inventory.append("water")
            elif discovered=="charcoal":
                inventory.append("charcoal")
                inventory.remove("water")
                things.remove("fire")
            elif discovered=="wetfire":
                things.remove("fire")
            elif discovered=="bed":
                things.append("bed")
                things.append("cedar chest")
                things.append("injured man")
            elif discovered=="fire":
                things.append("fire")
                inventory.remove("match")
                inventory.remove("firewood")
            elif discovered=="cedar chest":
                for i in range(3):
                    inventory.append("cloth")
                for i in range(random.randint(2,5)):
                    inventory.append("match")
                    
            else:
                  things.append(discovered)
        else:
            print("There is no",thing,"to search")
            print()
    if action=="inventory":
        takeinventory(inventory)

if alive == False:
    if injury>6:
        print("The man died, without him you were soon to follow...")
        
    print("YOU DIED")
    print()
    print("You discovered the following:")
    for i in things:
        print(i)
    print()
    print("You gathered the following:")
    for i in inventory:
        print(i)
    




    
