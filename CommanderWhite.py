# Please note that this program is bad and follows "garbage in, garbage out" philosophy.
# If incorrect input is given the program may do silly things.
# Avoid incorrect input and the program will avoid silly things.
import random
import math
import pickle
import os
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
    stats["Weapon"] = '00000'
    if unittype == "A":
        unitName = unittype + str(unitNumber)
    elif unittype == "G":
        unitName = unittype + str(unitNumber)
    else:
        unitName = str(unitNumber) + unittype
    try:
        infile = open('units/unitData/' + unitName+'.YoRHa', 'r')
        print('Error: Unit already exists.')
        infile.close()
    except FileNotFoundError:
        with open('units/unitData/' + unitName+'.YoRHa', 'wb') as outfile:
            pickle.dump(stats, outfile)
        print('Unit created successfully.')
        outfile.close()
    registerUnit(unitName)

def statifier(name, stat):
    for i in range (5):
        statint = random.random()
        if  statint >= 0.6:
            stat = stat + 1
        elif statint <= 0.4:
            stat = stat - 1
    return(stat)
def weaponAssign(unit, weapid):
    stats = getChar(unit)
    oldstats = getWeap(stats['Weapon'])
    oldOwner = getChar(oldstats['Owner'])
    oldOwner['Weapon'] = '00000'
    with open('units/unitData/' + oldstats['Owner']+'.YoRHa', 'wb') as outfile: #WRITE BINARY DUMB FUCK
        pickle.dump(oldOwner, outfile)
        outfile.close() 
    if stats['Weapon'] != '00000':
        oldstats = getWeap(stats['Weapon'])
        oldstats['Owner'] = ''
        with open("weapons/"+stats["Weapon"]+'.throngler', 'wb') as outfile:
            pickle.dump(oldstats, outfile)
            outfile.close()
    stats['Weapon'] = weapid
    with open('units/unitData/' + unit+'.YoRHa', 'wb') as outfile: #WRITE BINARY DUMB FUCK
        pickle.dump(stats, outfile)
        outfile.close() 
    newstats = getWeap(weapid)
    newstats['Owner'] = unit
    with open("weapons/"+stats["Weapon"]+'.throngler', 'wb') as outfile:
        pickle.dump(newstats, outfile)
        outfile.close()
    print('Operation complete.')
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
        with open('units/unitData/' + desiredUnit+'.YoRHa', 'wb') as outfile: #WRITE BINARY DUMB FUCK
            pickle.dump(stats, outfile)
            outfile.close() 
    else:
        print("Fuck-a-doodle-doo! The stat didn't increase.")

def getChar(unitName):
    infile = open('units/unitData/' + unitName+'.YoRHa', 'rb')
    stats = pickle.load(infile)
    infile.close()
    return(stats)
def getChips(unitName):
    infile = open('units/chipsets/' + unitName+'.chips', 'rb')
    chips = pickle.load(infile)
    infile.close()
    return(chips)
def getWeap(weapid):
    infile = open("weapons/"+weapid+'.throngler', 'rb')
    stats = pickle.load(infile)
    infile.close()
    if stats['Kills'] <= 25:
        stats['Level'] = 1
    elif stats['Kills'] <= 75:
        stats['Level'] = 2
    elif stats['Kills'] <= 150:
        stats['Level'] = 3
    else:
        stats['Level'] = 4
    with open("weapons/"+weapid+'.throngler', 'wb') as outfile:
        pickle.dump(stats, outfile)
        outfile.close()
    return(stats)

def getEnemy(unitName):
    infile = open("enemies/"+unitName+'.N2', 'rb')
    stats = pickle.load(infile)
    infile.close()
    return(stats)

def editChar(desiredUnit, stats, desiredStat, newValue):
    stats[desiredStat] = (newValue)
    with open('units/unitData/' + desiredUnit+'.YoRHa', 'wb') as outfile: #WRITE BINARY DUMB FUCK
        pickle.dump(stats, outfile)
    print("Operation complete.")
def registerUnit(unitName):
    offset = {'A': 0, 'B': 100, 'C': 200, 'D': 300, 'E': 400, 'G': 500, 'H': 600, 'O': 700, 'R': 800, 'S': 900}
    with open('savedata/YoRHa Registry', 'rb') as infile:
        units = pickle.load(infile)
        infile.close()
    unitNumber = int("".join(filter(str.isdigit, unitName)))
    unitType = ("".join(filter(str.isalpha, unitName)))
    unitIndex = unitNumber + offset[unitType] - 1
    units[unitIndex] = unitName
    with open('savedata/YoRHa Registry', 'wb') as outfile:
        units = pickle.dump(units, outfile)
        outfile.close()
def printTable():
    with open('savedata/YoRHa Registry', 'rb') as infile:
        units = pickle.load(infile)
        infile.close()
    for i in range(10):
        for j in range(10):
            for k in range(10):
                if units[100*i + 10*j+ k] != '':
                    print('{:4}'.format(units[100*i + 10*j + k]), sep = ' ', end = ' ')
                else:
                    print('----', sep = ' ', end = ' ')
            print()
        print()
def listweapons():
    idFile = open('weapons/bases/totalweapons.txt', 'r')
    id = int(idFile.readline().strip())
    idFile.close
    for i in range(id -1):
        with open("weapons/"+str(i + 1).zfill(5)+'.throngler', 'rb') as infile:
            stats = pickle.load(infile)
            print('ID:', stats['ID'], 'Owner:', stats['Owner'], 'Name:', stats['name'],'Type:' ,stats['Type'], 'Level:', stats['Level'], 'Kills:', stats['Kills'])
            infile.close()
def listunits():
    with open('savedata/YoRHa Registry', 'rb') as infile:
        units = pickle.load(infile)
        infile.close()
    for element in units:
        if element != '':
            infile = open('units/unitData/' + element+'.YoRHa', 'rb')
            stats = pickle.load(infile)
            infile.close()
            print(element, 'Level:', stats['Level'])

def printStats(unit):
    stats = getChar(unit)
    statlist = stats.keys()
    for element in statlist:
        print(element,':', stats[element], end = '   ')
    print()
def deleteUnit():
    unit = input('Enter the name of the unit to be deleted: ')
    if input('Are you sure about this?: ') == 'Y':
        if input('Are you REALLY sure about this?: ') == 'Y':
            if input('This unit will be permanently deleted!: ') == 'Y':
                if input('Is this really what you want? Think of ' + unit +'! Do you really want to throw them away?') == 'Y':
                    if input('Enter the name of the unit to be deleted: ') == unit:
                        os.remove('units/unitData/' + unit + ".YoRHa")
                        with open('savedata/YoRHa Registry', 'rb') as infile:
                            units = pickle.load(infile)
                            infile.close()
                        for i in range(1000):
                            if units[i] == unit:
                                units[i] = ''
                        with open('savedata/YoRHa Registry', 'wb') as outfile:
                            units = pickle.dump(units, outfile)
                            outfile.close()
                        print('Operation complete. Farewell, ' + unit +". You have served well.")
                    else:
                        print('The incorrect name was entered. No deletion will proceed.')
                else:
                    print('Deletion cancelled.')
            else:
                print('Deletion cancelled.')
        else:
            print('Deletion cancelled.')
    else:
         print('Deletion cancelled.')

def grantXP(desiredUnit, toGrant):
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
    with open('units/unitData/' + desiredUnit+'.YoRHa', 'wb') as outfile: #WRITE BINARY DUMB FUCK
        pickle.dump(stats, outfile)
    print("Operation complete.")

def main():
    mode = None
    while mode != "quit":
        mode = input("Enter the needed operation (create, listweap, listunit, printCube, printUnit, editunit, register, assignWeap, delete, quit): ")
        if mode == "create":
            creatifier()
        if mode == 'listweap':
            listweapons()
        if mode == 'listunit':
            listunits()
        if mode == 'printCube':
            printTable()
        if mode == "editunit":
            desiredUnit = input("Enter the name of the unit you wish to test: ")
            desiredEditUnitStats = getChar(desiredUnit)
            desiredEditStat = input("Enter the stat you wish to edit: ")
            newValue = input("Enter the new value for the stat: ")
            editChar(desiredUnit, desiredEditUnitStats, desiredEditStat, newValue)
        if mode == "register":
            registerUnit(input("Enter the name of the unit you wish to register: "))
        if mode == "printUnit":
            printStats(input("Enter the name of the unit you wish to get: ")) 
        if mode == 'assignWeap':
            unit = input("Enter the name of the unit to whom you wish to give a weapon: ")
            weapid = input('Enter the ID of the weapon you wish to give them: ')
            weaponAssign(unit, weapid)
        if mode == 'delete':
            deleteUnit()
if __name__ == "__main__":
    main()