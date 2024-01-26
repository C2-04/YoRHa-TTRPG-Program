# Please note that this program is bad and follows "garbage in, garbage out" philosophy.
# If incorrect input is given the program may do silly things.
# Avoid incorrect input and the program will avoid silly things.
import random
import math
import pickle

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
        infile = open(unitName+'.YoRHa', 'r')
        print('Error: Unit already exists.')
        infile.close()
    except FileNotFoundError:
        with open(unitName+'.YoRHa', 'wb') as outfile:
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
    stats['Weapon'] = weapid
    with open(unit+'.YoRHa', 'wb') as outfile: #WRITE BINARY DUMB FUCK
        pickle.dump(stats, outfile)
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
        with open(desiredUnit+'.YoRHa', 'wb') as outfile: #WRITE BINARY DUMB FUCK
            pickle.dump(stats, outfile)
        outfile.close() 
    else:
        print("Fuck-a-doodle-doo! The stat didn't increase.")

def getChar(unitName):
    infile = open(unitName+'.YoRHa', 'rb')
    stats = pickle.load(infile)
    infile.close()
    return(stats)
def getEnemy(unitName):
    infile = open("enemies/"+unitName+'.N2', 'rb')
    stats = pickle.load(infile)
    infile.close()
    return(stats)

def editChar(desiredUnit, stats, desiredStat, newValue):
    stats[desiredStat] = newValue
    with open(desiredUnit+'.YoRHa', 'wb') as outfile: #WRITE BINARY DUMB FUCK
        pickle.dump(stats, outfile)
    print("Operation complete.")
def registerUnit(unitName):
    offset = {'A': 0, 'B': 100, 'C': 200, 'D': 300, 'E': 400, 'G': 500, 'H': 600, 'O': 700, 'R': 800, 'S': 900}
    with open('YoRHa Registry', 'rb') as infile:
        units = pickle.load(infile)
        infile.close()
    unitNumber = int("".join(filter(str.isdigit, unitName)))
    unitType = ("".join(filter(str.isalpha, unitName)))
    unitIndex = unitNumber + offset[unitType] - 1
    units[unitIndex] = unitName
    with open('YoRHa Registry', 'wb') as outfile:
        units = pickle.dump(units, outfile)
        outfile.close()
def printUnits():
    with open('YoRHa Registry', 'rb') as infile:
        units = pickle.load(infile)
        infile.close()
    print(units)

def listweapons():
    idFile = open('weapons/bases/totalweapons.txt', 'r')
    id = int(idFile.readline().strip())
    idFile.close
    for i in range(id):
        with open("weapons/"+str(i + 1).zfill(5)+'.throngler', 'rb') as infile:
            stats = pickle.load(infile)
            print('ID:', stats['ID'], 'Name:', stats['name'],'Type:' ,stats['Type'], 'Level:', stats['Level'], 'Kills:', stats['Kills'])
            infile.close()
def listunits():
    with open('YoRHa Registry', 'rb') as infile:
        units = pickle.load(infile)
        infile.close()
    for element in units:
        if element != '':
            infile = open(element+'.YoRHa', 'rb')
            stats = pickle.load(infile)
            infile.close()
            print(element, 'Level:', stats['Level'])

def main():
    mode = None
    while mode != "quit":
        mode = input("Enter the needed operation (create, listweap, lisunit, editunit, register, assignWeap, quit): ")
        if mode == "create":
            creatifier()
        if mode == 'listweap':
            listweapons()
        if mode == 'listunit':
            listunits()
        if mode == "editunit":
            desiredUnit = input("Enter the name of the unit you wish to test: ")
            desiredEditUnitStats = getChar(desiredUnit)
            desiredEditStat = input("Enter the stat you wish to edit: ")
            newValue = int(input("Enter the new value for the stat: "))
            editChar(desiredUnit, desiredEditUnitStats, desiredEditStat, newValue)
        if mode == "register":
            registerUnit(input("Enter the name of the unit you wish to register: "))
        if mode == "getunit":
            print(getChar(input("Enter the name of the unit you wish to display: ")))  
        if mode == 'assignWeap':
            unit = input("Enter the name of the unit to whom you wish to give a weapon: ")
            weapid = input('Enter the ID of the weapon you wish to give them: ')
            weaponAssign(unit, weapid)
main()