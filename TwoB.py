from CommanderWhite import *
from InstructorBlack import *
from Anemone import *

class Board:
    def __init__(size, self):
        #maybe the board should have a name
        self.size = int(size)
        self.squares = 'how do I do this'
        self.turn = 0
        self.enemies = []
        self.friendlies = []
    def nextTurn(self):
        self.turn = self.turn + 1
    def enemyTurn(self):
        print('PLACEHOLDER')
    def playerTurn(self):
        print('PLACEHOLDER')
    def moveUnit(name, newPos, self):
        name.position = newPos
class Enemy:
    def __init__(unittype, name, unitindex, health, allegiance, stats, position, self):
        self.unittype = unittype
        self.name = unittype + str(unitindex)
        self.health = health
        self.allegiance = allegiance
        self.stats = stats
        self.position = position
    def takeDamage(damage, self):
        self.health = self.health - damage
        if self.health <= 0:
            self.die()
    def die(self):
        print('PLACEHOLDER')
        #remove it from the friendlies
        #then grant kill credit to whatever killed it
        #actually wait no put it in the killEnemy method
    def attack(self):
        # if a friendly is in range attack it
        #if not, move
        print('PLACEHOLDER')
    def move(self):
        # pseudocode! for all elements in friendlies:
        # check the distance (adjacent squares) to each one
        # then attempt to move to the closest one
        # if its target is occupied then move to an adjacent valid square
        print('PLACEHOLDER')
class Friendly:
    def __init__(name, health, stats, position, self):
        self.name = name
        self.health = health
        self.stats = stats
        self.position = position
    def takeDamage(damage, self):
        self.health = self.health - damage
        if self.health <= 0:
            self.die()
    def levelUp(newLevel, newStats, self):
        self.stats = newStats
        self.health = self.stats['Max Health']
    def killEnemy(enemyType, self):
        
        print('PLACEHOLDER')
    def die(self):
        print('PLACEHOLDER')
    def attack(self):
        print('PLACEHOLDER')
    def move(self):
        startSquare = self.position
        endSquare = input('Enter new coordinates (comma-separated): ')
        if (abs(startSquare[0] - endSquare[0]) <= 2 and abs(startSquare[1] - endSquare[1]) <= 2):
            self.position = endSquare
        else:
            print("Invalid move! You lose this unit's turn! Goofball!")
        print('PLACEHOLDER')