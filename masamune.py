import pickle
from CommanderWhite import *
from InstructorBlack import *
def createTemplate():
    weapbase = {}
    weapbase['name'] = "YoRHa-Issue Rifle"
    weapbase['Shot'] = [7, 0.9, 1]
    weapbase['Targeted Shot'] = [8, 1, 2]
    weapbase["Scoped Shot"] = [12, 1, 3]
    weapbase["Desperate Burst"] = [11, 0.6, 4]
    weapbase['Type'] = 'Gun'
    with open("weapons/bases/"+weapbase['name']+'.throngler', 'wb') as outfile:
        pickle.dump(weapbase, outfile)
        outfile.close()
def createWeapon(name):
    with open("weapons/bases/"+name+'.throngler', 'rb') as infile:
        stats = pickle.load(infile)
        infile.close()
    idFile = open('weapons/bases/totalweapons.txt', 'r')
    id = int(idFile.readline().strip())
    idFile.close
    idFile = open('weapons/bases/totalweapons.txt', 'w')
    newID = id + 1
    print(newID, file=idFile)
    stats['ID'] = str(id).zfill(5)
    stats['Level'] = 1
    stats['Kills'] = 0
    stats['Owner'] = ''
    with open("weapons/"+stats['ID']+'.throngler', 'wb') as outfile:
        pickle.dump(stats, outfile)
        outfile.close()
def createEnemy(enemName):
    stats = {}
    stats['Machine'] = int(input('Enter machine attack: '))
    stats['Defense'] = int(input('Enter defense: '))
    stats['Movement'] = int(input('Enter movement: '))
    stats['MOR'] = 2
    stats['Yield'] = int(input('Enter XP Yield: '))
    stats['Max Health'] = int(input('Enter max health: '))
    stats['Weapon Type'] = 'Machine'
    stats['Evasion'] = float(input('Enter evasion: '))
    stats['Accuracy'] = float(input('Enter accuracy: '))
    stats['Unit Type'] = 'Machine'
    stats['Personality'] = 'Machine'
    with open("enemies/"+enemName+'.N2', 'wb') as outfile:
        pickle.dump(stats, outfile)
        outfile.close()
