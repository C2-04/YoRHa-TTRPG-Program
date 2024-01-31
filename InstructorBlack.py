from CommanderWhite import *
import math
import random
import pickle

def calculateReward(lower_bound, upper_bound):
    reward = math.floor((upper_bound - lower_bound)/2) + lower_bound
    for i in range(0, upper_bound - lower_bound):
        if random.random() >= 0.5:
            reward = reward + 1
        else:
            reward = reward - 1
    print("Reward:", reward)
    return(reward)
def placeEnemies(enemies):
    enemyPlaces = []
    for i in range(enemies):
        xCoord = random.randint(2, 9)
        yCoord = random.randint(2, 9)
        enemyPlaces.append([xCoord, yCoord])
    print("Enemy places:", end = ' ')
    for element in enemyPlaces:
        print(element, end = ' ')
    print()
    return(enemyPlaces)

def selectEnemies(weight):
    enemNum = 1
    chosenEnemies = []
    enemiesList = {"Small Stubby" : 20,
                   "Medium Biped" : 50,
                   "Horseback Machine" : 80,
                   "Small Flier": 30,
                   "Medium Flier": 140,
                   "Explodey Boy": 10,
                   "Axe Flier": 90,
                   "Mech Worm": 150,
                   "Gunslinger": 70,
                   }
    selectedEnemy = random.choice(list(enemiesList.keys()))
    enhancements = ['']
    while weight >= enemiesList[selectedEnemy]:
        selectedWeight = enemiesList[selectedEnemy]
        if random.random() >= 0.9:
            selectedWeight = selectedWeight*2
            enhancements[-1] = enhancements[-1] + 'E'
        if random.random() >= 0.9:
            selectedWeight = selectedWeight*2
            enhancements[-1] = enhancements[-1] + 'G'
        weight = weight - selectedWeight
        chosenEnemies.append(selectedEnemy)
        enemNum = enemNum + 1
        enhancements.append('')
        selectedEnemy = random.choice(list(enemiesList.keys()))
    print(enemNum, "enemies:", ', '.join(chosenEnemies), "and a", abs(weight), "layer Defenseless Stack!")
    print(enhancements)
    return (enemNum, chosenEnemies, enhancements, weight)

def itemRewards(weight):
    rewardList = []
    for i in range(weight):
        itemRNG = random.random()
        if itemRNG <= 0.67:
            rewardList.append(random.choice(["Dented Plate", "Broken Circuit", 'Stripped Screw', 'Small Gear',
                                             "Broken Key", 'Warped Wire', 
                                             'Rusty Bolt', 'Crushed Nut', 'Dented Socket', 'Severed Cable', 'Broken Battery']))
        elif itemRNG <= 0.92:
            rewardList.append(random.choice(["Titanium Alloy", 'Large Gear', 'Stretched Coil', 'Sturdy Socket', "Pristine Cable",
                                              "Large Battery"]))
        elif itemRNG <= 0.99:
            rewardList.append(random.choice(["Memory Alloy", "Machine Arm", "Machine Leg", 'Machine Torso', "Machine Head"]))
        else:
            rewardList.append("Machine Core")
    print(weight, "rewards:", ', '.join(rewardList))

def hitcalcifier(Attacker, Defender):
    if len(Attacker) <= 4:
        atksts = getChar(Attacker)
        with open("weapons/"+atksts['Weapon']+'.throngler', 'rb') as infile:
            stats = pickle.load(infile)
            infile.close()
        selectedAttack = input('Enter the desired attack: ')
        weaponDamage = stats[selectedAttack][0]
        acc = stats[selectedAttack][1]
        minLevel = stats[selectedAttack][2]
        if stats['Level'] < minLevel:
            print('Weapon level must be higher.')
            return()
    else:
        atksts = getEnemy(Attacker)
        acc = atksts['Accuracy']
        weaponDamage = 0
    if len(Defender) <= 4:
        defsts = getChar(Defender)
    else:
        defsts = getEnemy(Defender)
    atk = atksts[stats['Type']] + random.randint(-2, 3) + weaponDamage
    mrl = atksts['MOR']
    dfs = defsts['Defense']
    evd = defsts['Evasion']
    if atksts['Unit Type'] == 'B':
        atk = atk + 3
    if defsts['Unit Type'] == 'D':
        dfs = dfs+ 3
    print('Chance to hit: '+ (str(round(acc*(1 - evd)*100))) + '%')
    print('Critical strike chance: '+ str(mrl) + '%')
    damage = max(atk-dfs, 1)
    if random.random() >= acc*(1 - evd):
        print("You missed.")
    elif random.randint(1, 100) <= mrl:
        damage = damage*2
        print("Critical strike for", damage, "damage!")
    else:
        print("Hit for", damage, 'damage!')
    return(damage)
def main():
    mode = None
    while mode != "quit":
        mode = input("Enter the needed operation (fightsetup, calchit, calcskill, quit): ")
        if mode == "fightsetup":
            lower_bound = int(input("Enter lower reward bound: "))
            upper_bound = int(input("Enter upper reward bound: "))
            weight = calculateReward(lower_bound, upper_bound)
            enemNum = selectEnemies(weight)[0]
            placeEnemies(enemNum)
            itemRewards(enemNum)
        if mode == "calchit":
            attackingUnit = input("Attacker: ")
            defendingUnit = input("Defender: ")
            hitcalcifier(attackingUnit, defendingUnit)
        if mode == "calcskill":
            desiredUnit = input("Enter the name of the unit you wish to test: ")
            desiredUnitStats = getChar(desiredUnit)
            desiredStat = input("Enter the stat you wish to test: ")
            statincreasifier(desiredStat, desiredUnitStats, desiredUnit)
if __name__ == "__main__":
    main()