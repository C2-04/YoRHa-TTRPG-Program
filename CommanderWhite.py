# Please note that this program is bad and follows "garbage in, garbage out" philosophy.
# If incorrect input is given the program may do silly things.
# Avoid incorrect input and the program will avoid silly things.
import random
import math
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
        xCoord = random.randint(3, 10)
        yCoord = random.choice(["c", "d", "e", "f", "g", "h", "i", "j"])
        enemyPlaces.append(str(xCoord) + yCoord)
    print("Enemy places:", ', '.join(enemyPlaces))

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
    while weight >= enemiesList[selectedEnemy]:
        selectedWeight = enemiesList[selectedEnemy]
        if random.random() >= 0.9:
            selectedWeight = selectedWeight*2
            selectedEnemy = "Enhanced "+ selectedEnemy
        if random.random() >= 0.9:
            selectedWeight = selectedWeight*2
            selectedEnemy =  selectedEnemy + " with a Gun"
        weight = weight - selectedWeight
        chosenEnemies.append(selectedEnemy)
        enemNum = enemNum + 1
        selectedEnemy = random.choice(list(enemiesList.keys()))
    print(enemNum, "enemies:", ', '.join(chosenEnemies), "and a", abs(weight), "layer Defenseless Stack!")
    return enemNum

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

def creatifier():
    unittype = input("Need a specific type? ")
    if unittype == "no":
        unittype = random.choice(["A", "B", "C", "D", "E", "G", "H", "O", "R", "S"])
    unitNumber = input("Need a specific number? ")
    if unitNumber == 'no':
        unitNumber = random.randint(1, 100)
    print("Number", unitNumber, "Type", unittype)
    tgh = 5
    cha = 5
    itg = 5
    agi = 5
    mor = 5 
    stats = {}
    stats['TGH'] = statifier('tgh', tgh)
    stats['CHA'] = statifier('cha', cha)
    stats['ITG'] = statifier('itg', itg)
    stats['AGI'] = statifier('agi', agi)
    stats['MOR'] = statifier('mor', mor)
    stats['1H Sword'] = stats['TGH']*3
    stats['2H Sword'] = stats['TGH']*3
    stats['Spear'] = stats['TGH']*3
    stats['Speech'] = stats['CHA']*3
    stats['Crime'] = stats['CHA']*3
    stats['Trading'] = stats['CHA']*3
    stats['Medicine'] = stats['ITG']*3
    stats['Tactics'] = stats['ITG']*3
    stats['Tech'] = stats['ITG']*3
    stats['Stealth'] = stats['AGI']*3
    stats['Gun'] = stats['AGI']*3
    stats['Bracers'] = stats['AGI']*3
    stats['Pod'] = stats['MOR']*3
    stats['Explosive'] = stats['MOR']*3
    stats['Resolve'] = stats['MOR']*3
    stats['Health'] = stats['TGH']*5 + 80
    stats['Max Health'] = stats['TGH']*5 + 80
    stats['Defense'] = stats['TGH']*2
    stats['Evasion'] = stats['AGI']*0.01
    stats['Level'] = 1
    stats['TotalXP'] = 0
    stats["Unit Type"] = unittype
    stats['Personality'] = unitNumber
    if unittype == "A":
        unitName = unittype + str(unitNumber)
    elif unittype == "G":
        unitName = unittype + str(unitNumber)
    else:
        unitName = str(unitNumber) + unittype
    try:
        infile = open(unitName+'.YoRHa', 'r')
        print('Error: Unit already exists.')
        infile.close()
    except FileNotFoundError:
        with open(unitName+'.YoRHa', 'wb') as outfile:
            pickle.dump(stats, outfile)
        print('Unit created successfully.')
        outfile.close()

def statifier(name, stat):
    for i in range (5):
        statint = random.random()
        if  statint >= 0.6:
            stat = stat + 1
        elif statint <= 0.4:
            stat = stat - 1
    return(stat)

def statincreasifier(derstat, stats, desiredUnit):
    derstatToBasestat = {
        '1H Sword':'TGH',
        '2H Sword':'TGH',
        'Spear':'TGH',
        'Speech':'CHA',
        'Crime':'CHA',
        'Trading':'CHA',
        'Medicine':'ITG',
        'Tactics':'ITG',
        'Tech':'ITG',
        'Stealth':'AGI',
        'Gun':'AGI',
        'Bracers':'AGI',
        'Pod':'MOR',
        'Explosive':'MOR',
        'Resolve':'MOR',
    }
    targetstat = derstatToBasestat[derstat]
    basestat = stats[targetstat]
    if basestat >= random.randint(0, 5) + random.randint(0, 5):
        print("Yup! The relevant stat increased.")
        stats[derstat] = stats[derstat] + 1
        with open(desiredUnit+'.YoRHa', 'wb') as outfile: #WRITE BINARY DUMB FUCK
            pickle.dump(stats, outfile)
        outfile.close() 
    else:
        print("Fuck-a-doodle-doo! The stat didn't increase.")

def hitcalcifier(Attacker, Defender):
    atksts = getChar(Attacker)
    defsts = getChar(Defender)
    atk = atksts[atksts['Weapon Type']] + random.randint(-2, 3)
    mrl = atksts['MOR']
    dfs = defsts['Defense']
    acc = float(input('Enter accuracy: '))
    evd = defsts['Evasion']
    if atksts['Unit Type'] == 'B':
        atk = atk + 3
    if defsts['Unit Type'] == 'D':
        dfs = dfs+ 3
    if random.random() >= acc*(1 - evd):
        print("You missed.")
    elif random.randint(1, 100) <= mrl:
        print("Critical strike for", 2*max(atk-dfs, 1), "damage!")
    else:
        print("Hit for", max(atk-dfs, 1), 'damage!')

def getChar(unitName):
    infile = open(unitName+'.YoRHa', 'rb')
    stats = pickle.load(infile)
    infile.close()
    return(stats)

def editChar(desiredUnit, stats, desiredStat, newValue):
    stats[desiredStat] = newValue
    with open(desiredUnit+'.YoRHa', 'wb') as outfile: #WRITE BINARY DUMB FUCK
        pickle.dump(stats, outfile)
    print("Operation complete.")

def grantXP(toGrant, desiredUnit):
    stats = getChar(desiredUnit)
    startLevel = stats['Level']
    stats['TotalXP'] = stats['TotalXP'] + toGrant
    stats['Level'] = int(math.ceil(stats['TotalXP']**(1/3)))
    if startLevel < stats["Level"]:
        print(desiredUnit + ' has reached level ' + str(stats['Level']) + '.')
        for i in range((stats['Level'] - startLevel)*(math.floor(stats['Level']/20) + 1)):
            levelstat = input('Enter the stat to increase by 1: ')
            stats[levelstat] = stats[levelstat] + 1
    stats['Max Health'] = 80 + (stats["Level"] + 4)*stats['TGH']
    stats['Health'] = stats['Max Health']
    with open(desiredUnit+'.YoRHa', 'wb') as outfile: #WRITE BINARY DUMB FUCK
        pickle.dump(stats, outfile)
    print("Operation complete.")

def main():
    mode = None
    while mode != "quit":
        mode = input("Enter the needed operation (create, fightsetup, calcskill, calchit, getunit, editunit, grantXP, quit): ")
        if mode == "fightsetup":
            lower_bound = int(input("Enter lower reward bound: "))
            upper_bound = int(input("Enter upper reward bound: "))
            weight = calculateReward(lower_bound, upper_bound)
            enemNum = selectEnemies(weight)
            placeEnemies(enemNum)
            itemRewards(enemNum)
        if mode == "create":
            creatifier()
        if mode == "grantXP":
            toGrant = int(input("Enter the amount of XP you wish to give: "))
            desiredUnit = input("Enter the unit to grant XP to: ")
            grantXP(toGrant, desiredUnit)
        if mode == "editunit":
            desiredUnit = input("Enter the name of the unit you wish to test: ")
            desiredEditUnitStats = getChar(desiredUnit)
            desiredEditStat = input("Enter the stat you wish to edit: ")
            newValue = int(input("Enter the new value for the stat: "))
            editChar(desiredUnit, desiredEditUnitStats, desiredEditStat, newValue)
        if mode == "getunit":
            print(getChar(input("Enter the name of the unit you wish to display: ")))
        if mode == "calcskill":
            desiredUnit = input("Enter the name of the unit you wish to test: ")
            desiredUnitStats = getChar(desiredUnit)
            desiredStat = input("Enter the stat you wish to test: ")
            statincreasifier(desiredStat, desiredUnitStats, desiredUnit)
        if mode == "calchit":
            attackingUnit = input("Attacker: ")
            defendingUnit = input("Defender: ")
            hitcalcifier(attackingUnit, defendingUnit)

main()