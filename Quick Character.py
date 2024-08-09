#Quick Character

import random

def roll(dice):
    total = 0
    lyst = [0 for i in range(dice)]
    for i in range(dice):
        lyst[i]=random.randint(1,6)
        #print(lyst)
    for i in range(min(dice,3)):
        large = 0
        for j in range(len(lyst)):
            if large < lyst[j]:
                large = lyst[j]
        total += large
        lyst.remove(large)
    return total
    
def rollhp(n,size,bonus,overten):
    hp = 0
    for i in range(min(n,9)):
        hp += random.randint(1,size)+bonus
    if n > 9:
        for i in range(n-9):
            hp += overten
    hp = max(1,hp)
    return hp

def stats(num,dice):
    for i in range(num):
        print("Str",roll(dice))
        print("Int",roll(dice))
        print("Wis",roll(dice))
        print("Dex",roll(dice))
        print("Con",roll(dice))
        print("Cha",roll(dice),"\n")


Bonus = {3:-3, 4:-2, 5:-2, 6:-1, 7:-1,
         8:-1, 9:0, 10:0, 11:0, 12:0,
         13:1, 14:1, 15:1, 16:2, 17:2, 18:3}

def gen(dice,level):
    Str = roll(dice)
    Int = roll(dice)
    Wis = roll(dice)
    Dex = roll(dice)
    Con = roll(dice)
    Cha = roll(dice)
    GP = roll(dice)*10
    
    if 9 > max(Str,Int,Wis,Dex):
        Class = "Village Idiot"
        HP = rollhp(level,4,Bonus[Con],1)
        
    elif 60 > (Str+Int+Wis+Dex+Con+Cha):
        Class = "Farmer"
        HP = rollhp(level,4,Bonus[Con],1)
        
    elif Str == max(Str,Int,Wis,Dex):
        Class = "Fighter"
        HP = rollhp(level,8,Bonus[Con],2)

        
    elif Int == max(Str,Int,Wis,Dex):
        Class = "Magic-User"
        HP = rollhp(level,4,Bonus[Con],1)

        
    elif Wis == max(Str,Int,Wis,Dex):
        Class = "Cleric"
        HP = rollhp(level,6,Bonus[Con],1)

        
    else:
        Class = "Thief"
        HP = rollhp(level,4,Bonus[Con],2)

        
    print(Class, "Level",level)
    print("HP =",HP)
    print("")
    print("Str",Str,Bonus[Str])
    print("Int",Int,Bonus[Int])
    print("Wis",Wis,Bonus[Wis])
    print("Dex",Dex,Bonus[Dex])
    print("Con",Con,Bonus[Con])
    print("Cha",Cha,Bonus[Cha])
    print("")
    print("Gold",GP)
    print("")



for i in range(10):
    gen(3,3)

