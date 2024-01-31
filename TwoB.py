from CommanderWhite import *
from InstructorBlack import *
from Anemone import *

class Board:
    def __init__(size, self):
        #maybe the board should have a name
        self.size = int(size)
        self.squares = {}
        for i in size:
            for j in size:
                self.squares[[i, j]] = ''
        self.turn = 0
        self.enemies = []
        self.friendlies = []
    def nextTurn(self):
        self.turn = self.turn + 1
    def enemyTurn(enemies, self):
        for element in self.enemies:
            selectedenemy = self.squares[[element[1], element[2]]]
            selectedenemy.attack()
    def playerTurn(self):
        for element in self.friendlies:
            selectedfriendly = self.squares[[element[1], element[2]]]
            selectedfriendly.move()
            selectedfriendly.attack()
    def placeEnemy(enemy, position, self):
        self.squares[position] = enemy
        self.enemies.append([enemy.name, enemy.position[0], enemy.position[1]])
    def placeFriendly(friendly, position, self):
        self.squares[position] = friendly
        self.friendlies.append([friendly.name, friendly.position[0], friendly.position[1]])
class Enemy:
    def __init__(unittype, unitindex, health, allegiance, stats, position, self):
        self.unittype = unittype + str(unitindex)
        self.name = unittype 
        self.health = health
        self.allegiance = allegiance
        self.stats = stats
        self.position = position
    def takeDamage(damage, board, self):
        self.health = self.health - damage
        if self.health <= 0:
            self.die(board)
    def die(board, self):
        print('PLACEHOLDER')
        for element in board.enemies:
            if element[0] == self.name:
                board.squares[[element[1], element[2]]] = ''
                board.enemies.remove(element)
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
    def __init__(name, health, stats, position, weapon, self):
        self.name = name
        self.health = health
        self.stats = stats
        self.position = position
        if weapon['Type'] == 'Gun':
            self.atkrange = 4
        else:
            self.atkrange = 1
    def takeDamage(damage, board, self):
        self.health = self.health - damage
        if self.health <= 0:
            self.die(board)
    def levelUp(newLevel, newStats, self):
        self.stats = newStats
        self.health = self.stats['Max Health']
    def killEnemy(enemy, self):
        print('PLACEHOLDER')
    def die(board, self):
        for element in board.friendlies:
            if element[0] == self.name:
                board.squares[[element[1], element[2]]] = ''
                board.friendlies.remove(element)
    def attack(board, self):
        targetSquare = map(int, input('Enter target coordinates (comma-separated): ')).split(',')
        if (abs(self.position[0] - targetSquare[1]) <= self.atkrange and abs(self[1] - targetSquare[1]) <= self.atkrange):
            target = board.squares[targetSquare]
            if target == '':
                print("There's nothing on that square! You forfeit this unit's attack turn!!")
            elif type(target) == Friendly:
                print("Friendly fire is not permitted! You forfeit this unit's attack turn!")
            else:
                damage = hitcalcifier(self.name, target.name)
                target.takeDamage(damage, board)
                if target.health <= 0:
                    target.killEnemy(target)
        else:
            print("Out of range! You forfeit this unit's attack turn!")
    def move(board, self):
        startSquare = self.position
        endSquare = map(int, input('Enter new coordinates (comma-separated): ')).split(',')
        if (abs(startSquare[0] - endSquare[0]) <= 2 and abs(startSquare[1] - endSquare[1]) <= 2):
            self.position = endSquare
            board.squares[startSquare] = ''
            board.squares[endSquare] = self
        else:
            print("Invalid move! You forfeit this unit's move turn!")
