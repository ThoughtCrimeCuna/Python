#Levi Peachey-Stoner
#archeologist game based on inventory concept
#started to practice with the use of dicitonaries


#Libraries

import random

#Inventory

inventory={"energy":0,"apple":10}
def takeinventory():
    print("\nYou have the following:\n")
    print("energy",inventory["energy"])
    for item in inventory:
        if item in food:
            print (item,inventory[item])
    for item in inventory:
        if item not in food and item !="energy":
            print (item,inventory[item])
    print()
def got(item,quant):
    try:
        inventory.update({item:inventory[item]+quant})
    except:
        inventory[item]=quant

def lose(item,quant):
    try:
        if inventory[item]>=quant:
            inventory.update({item:inventory[item]-quant})
            return True
        else:
            return False
    except:
        return False

def fullAccess():
    x=input("get or lose? ")
    if x == "get":
        got(input("What you got? "))
    elif x == "lose":
        lose(input("what did you lose? "))
    else:
        print(inventory)

#Actions
        
def dig(noun):
    if noun in sites:
        print("You dig on",noun,"and find ", end="")
        if sites[noun]==1:
            print("a firey pit")
        elif sites[noun]==2:
            y=random.randint(1,4)
            if y==1:
                got("bone",1)
                print("a disturbing reminder.\nYou got a bone.")
            elif y==2:
                z=random.randint(2,3)
                got("bone",z)
                print("some old bones.\nYou got",z,"bones.")
            elif y==3:
                z=random.randint(4,10)
                got("bone",z)
                print("an ancient skeleton.\nYou got",z,"bones.")
            elif y==4:
                z=random.randint(6,10)
                got("bone",z)
                print("a poor mans grave.\nYou got",z,"bones.")
        elif sites[noun]==3:
            y=random.randint(1,2)
            if y==1:
                got("bulb",1)
                print("a strange vegetable. A large fleshy bulb, with a tough husk.\nYou got 1 bulb.")
            elif y==2:
                z=random.randint(2,3)
                got("tuber",z)
                print("a some strange vegetables. A wierdly lobed tuber, with a sweet green shoot.\nYou got",z,"tubers.")
        elif sites[noun]==4:
            y=random.randint(1,2)
            if y==1:
                got("yam",1)
                print("a huge starchy yam.\nYou got a yam.")
            elif y==2:
                z=random.randint(3,7)
                got("onion",z)
                print("a patch of spicy, wild onions.\nYou got",z,"onions.")
        elif sites[noun]==5:
            y=random.randint(1,3)
            if y==1:
                got("ginger",1)
                print("a sweet clump of ginger root.\nYou got a ginger.")
            elif y==2:
                z=random.randint(3,6)
                got("potato",z)
                print("a wealth of dusty potatoes.\nYou got",z,"potatoes.")
            elif y==3:
                got("carrot",1)
                print("a crooked little carrot.\nYou got a carrot.")
        elif sites[noun]==6:
            print("nothing but shifting sand.")
        elif sites[noun]==7:
            y=random.randint(1,4)
            if y==1:
                got("scrap",1)
                print("a  from a time long past.\nYou got a scrap.")
            elif y==2:
                z=random.randint(2,3)
                got("scrap",z)
                print("some old peices of art.\nYou got",z,"scraps.")
            elif y==3:
                z=random.randint(2,6)
                got("scrap",z)
                print("a cache of old metal tools, and .\nYou got",z,"scraps.")
            elif y==4:
                z=random.randint(6,10)
                got("bone",z)
                w=random.randint(2,3)
                got("scrap",w)
                print("a rich mans tomb.\nYou got",z,"bones.\nYou got",w,"scraps.")
        elif sites[noun]==8:
            y=random.randint(1,4)
            if y==1:
                got("scrap",1)
                print("a from a time long past.\nYou got a scrap.")
            elif y==2:
                z=random.randint(2,3)
                got("scrap",z)
                print("some old peices of art.\nYou got",z,"scraps.")
            elif y==3:
                z=random.randint(2,6)
                got("scrap",z)
                print("a cache of old metal tools, and .\nYou got",z,"scraps.")
            elif y==4:
                z=random.randint(6,10)
                got("bone",z)
                w=random.randint(2,3)
                got("scrap",w)
                print("a rich mans tomb.\nYou got",z,"bones.\nYou got",w,"scraps.")
        elif sites[noun]==9:
            y=random.randint(1,4)
            if y==1:
                got("fragment",1)
                print("a shard of old magic.\nYou got a fragment.")
            elif y==2:
                z=random.randint(2,3)
                got("fragment",z)
                print("some strange magical devices.\nYou got",z,"fragments.")
            elif y==3:
                z=random.randint(3,7)
                got("scrap",z)
                got("fragment",1)
                print("an old magical stucture.\nYou got",z,"scraps.\nYou got a fragment.")

            elif y==4:
                z=random.randint(6,10)
                got("bone",z)
                w=random.randint(2,3)
                got("fragment",w)
                print("a magicians tomb.\nYou got",z,"bones.\nYou got",w,"fragments.")
        elif sites[noun]==10:
            y=random.randint(1,6)
            if y==1:
                got("artifact",1)
                print("an enchanted weapon from a bygone era.\nYou got an artifact.")
            elif y==2:
                z=random.randint(2,3)
                got("fragment",z)
                print("some strange magical devices.\nYou got",z,"artifacts.")
            elif y==3:
                z=random.randint(3,7)
                got("scrap",z)
                got("fragment",1)
                print("an old magical stucture.\nYou got",z,"scraps.\nYou got a fragment.")
            elif y==4:
                z=random.randint(6,10)
                got("bone",z)
                w=random.randint(2,3)
                got("fragment",w)
                print("a magicians tomb.\nYou got",z,"bones.\nYou got",w,"fragments.")
            elif y==5:
                z=random.randint(3,7)
                got("scrap",z)
                got("fragment",1)
                print("an old magical stucture.\nYou got",z,"scraps.\nYou got a fragment.")
            elif y==6:
                z=random.randint(6,10)
                got("bone",z)
                w=random.randint(4,6)
                got("fragmements",w)
                v=random.randint(2-3)
                got("artifacts",v)
                print("a sorcerer kings tomb.\nYou got",z,"bones.\nYou got",w,"scraps.\nYou got",v,"fragments.")

    else:
        print(noun,"is not a dig site.")


#Information
digsyn=['dig',"bore","bulldoze","burrow","clean","discover","dredge",
     "drill","enter","excavate","exhume","gouge","harvest","penetrate",
     "scoop","search",'shovel','sift','uncover','unearth',
     'investigate','mine','pierce','pit','probe','quarry','tunnel']
eatsyn=['eat','consume','scoff','scarf','ingest','devour','swallow',
     'masticate','munch','gobble','gormandize','gulp']
sitelist=['1,1','1,2','1,3','1,4','1,5','1,6','1,7','1,8','1,9',
      '2,1','2,2','2,3','2,4','2,5','2,6','2,7','2,8','2,9',
      '3,1','3,2','3,3','3,4','3,5','3,6','3,7','3,8','3,9',
      '4,1','4,2','4,3','4,4','4,5','4,6','4,7','4,8','4,9',
      '5,1','5,2','5,3','5,4','5,5','5,6','5,7','5,8','5,9',
      '6,1','6,2','6,3','6,4','6,5','6,6','6,7','6,8','6,9',
      '7,1','7,2','7,3','7,4','7,5','7,6','7,7','7,8','7,9',
      '8,1','8,2','8,3','8,4','8,5','8,6','8,7','8,8','8,9',
      '9,1','9,2','9,3','9,4','9,5','9,6','9,7','9,8','9,9',
      'campsite']
food={'apple':5,'potato':2,'onion':1,'yam':4,'carrot':1,
      'ginger':3,'tuber':3,'bulb':5}


def definesites():
    sites={}
    for item in sitelist:
        sites[item]=random.randint(1,5)+random.randint(0,5)
    return(sites)


#Input Processor

def actions():
    action=input("What would you like to do?\n").lower()
    x=action.split()
    if len(x)==2:
        #print(x)
        verb = x[0]
        noun = x[1]
        if verb in digsyn:
            dig(noun)
        elif verb in eat:
            if noun in food:
                a=lose(noun,1)
                if a == True:
                    print("You eat the",noun+".")
                    got("energy",food[noun])
                    return True
                else:
                    print("You don't have any",noun,"to eat.")
                    return False
            else:
                print("You can't eat",noun+".")
                return False
    elif action == "help":
        print("")
        return False
    else:
        print("Please input a two term phrase such as 'eat apple' or 'dig 1,1'.\nIf you are confused about possible actions type 'help'.")


sites=definesites()
while True:
    actions()
    takeinventory()
    print(sites)









