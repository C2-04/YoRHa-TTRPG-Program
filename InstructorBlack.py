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
def placeEnemies(enemies, boardSize = '12'):
    enemyPlaces = []
    for i in range(enemies):
        xCoord = random.randint(2, boardSize - 3)
        yCoord = random.randint(2, boardSize - 3)
        enemyPlaces.append([xCoord, yCoord])
    return(enemyPlaces)

def selectEnemies(weight):
    enemNum = 0
    chosenEnemies = []
    enemiesList = {"Small Stubby" : 20,
                   "Medium Biped" : 50,
                   "Horseback Machine" : 80,
                   "Small Flier": 30,
                   "Medium Flier": 140,
                   "Explodey Boy": 10,
                   "Axe Flier": 90,
                   "Gth Biped" : 500,
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
    return(rewardList)
def rareWards(weight):
    rewardList = []
    for i in range(weight):
        itemRNG = random.random()
        rewardList.append(random.choice(["Memory Alloy", "Machine Arm", "Machine Leg", 'Machine Torso', "Machine Head", "Machine Core"]))
    return(rewardList)

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
        atk = atksts[stats['Type']] + random.randint(-2, 3) + weaponDamage
    else:
        atksts = getEnemy(Attacker)
        acc = atksts['Accuracy']
        weaponDamage = 0
        atk = atksts['Machine']
    if len(Defender) <= 4:
        defsts = getChar(Defender)
    else:
        defsts = getEnemy(Defender)
    
    mrl = atksts['MOR']
    dfs = defsts['Defense']
    evd = defsts['Evasion']
    if atksts['Unit Type'] == 'B':
        atk = atk + 3
    if atksts['Unit Type'] == 'A':
        atksts['1H Sword'] = atksts['1H Sword']+6
        atksts['2H Sword'] = atksts['2H Sword']+6
    if defsts['Unit Type'] == 'D':
        dfs = dfs+ 3
    print('Chance to hit: '+ (str(round(acc*(1 - evd)*100))) + '%')
    print('Critical strike chance: '+ str(mrl) + '%')
    damage = max(atk-dfs, 1)
    if random.random() >= acc*(1 - evd):
        print("You missed.")
        damage = 0
    elif random.randint(1, 100) <= mrl:
        damage = damage*2
        print("Critical strike on", Defender, "for", damage, "damage!")
    else:
        print("Hit on", Defender, "for", damage, 'damage!')
    return(damage)
def weapKill(weapid):
    stats = getWeap(weapid)
    stats['Kills'] = stats['Kills'] + 1
    with open("weapons/"+weapid+'.throngler', 'wb') as outfile:
        pickle.dump(stats, outfile)
        outfile.close()
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