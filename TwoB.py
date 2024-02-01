from CommanderWhite import *
from InstructorBlack import *
from Anemone import *
# I was listening to the Drakengard 1 OST as I created this thing so please excuse any terrible code moments
# It also might be a good idea to have some more input validation on this -- I really want to avoid having to scrap an entire battle because
# a single mistyped input caused the whole thing to shit itself
class Board:
    def __init__(self, size):
        #maybe the board should have a name
        self.size = int(size)
        self.squares = {}
        for i in range(size):
            for j in range(size):
                self.squares[tuple([i, j])] = ''
        self.turn = 0
        self.enemies = []
        self.friendlies = []
    def nextTurn(self):
        self.playerTurn()
        if len(self.enemies) == 0:
            exit
        if len(self.friendlies) == 0:
            exit
    def enemyTurn(self):
        for element in self.enemies:
            selectedenemy = element
            selectedenemy.attack()
            print('Enemy has taken a turn.')
        self.playerTurn()
    def playerTurn(self):
        for element in self.friendlies:
            print('Your turn.')
            self.printBoard()
            selectedfriendly = element
            selectedfriendly.move()
            selectedfriendly.attack()
        self.enemyTurn()
    def placeEnemy(self, enemy, position):
        self.squares[tuple(position)] = enemy
        self.enemies.append(enemy)
    def placeFriendly(self, friendly, position):
        self.squares[tuple(position)] = friendly
        self.friendlies.append(friendly)
    def printBoard(self):
        neededSize = self.size
        for i in range(neededSize):
            print('|'+ '{:^15}'.format(str(i)) +'|', end = '')
        print()
        for i in range(neededSize):
            for j in range(neededSize):
                print('|' + '{:^15}'.format(str(self.squares[(i, j)])) + '|', end='')
            print('   ' + str(i))
    def __str__(self):
        return(self.squares)
class Enemy:
    def __init__(self, unittype, unitindex, health, stats, position, board):
        self.name = unittype 
        self.health = health
        self.stats = stats
        self.position = position
        self.board = board
    def takeDamage(self, damage):
        self.health = self.health - damage
        if self.health <= 0:
            self.die()
    def __str__(self):
        return(self.name)
    def die(self):
        self.board.squares[self.position] = ''
        self.board.friendlies.remove(self)
    def attack(self):
        # if a friendly is in range attack it
        #if not, move
        nonenemy = []
        target = None
        closestTargetPos = None
        minDistance = self.board.size
        for element in self.board.friendlies:
            nonenemy.append(element.position)
        for element in nonenemy:
            distance = max(abs(element[0] - self.position[0]), abs(element[1] - self.position[1]))
            if distance <= minDistance:
                minDistance = distance
                closestTargetPos = element
        if distance == 1:
            target = self.board.squares[tuple(closestTargetPos)]
            damage = hitcalcifier(self.name, target.name)
            target.takeDamage(damage)
    def move(self):
        # pseudocode! for all elements in friendlies:
        # check the distance (adjacent squares) to each one
        friendlyplaces = []
        closestTargetPos = None
        minDistance = self.board.size
        for element in self.board.friendlies:
            friendlyplaces.append(element.position)
        for element in friendlyplaces:
            distance = max(abs(element[0] - self.position[0]), abs(element[1] - self.position[1]))
            if distance <= minDistance:
                minDistance = distance
                closestTargetPos = element
        movement = self.stats['Movement']
        # then attempt to move to the closest one
        endSquare = [None, None]
        if minDistance <= movement:
            endSquare = closestTargetPos
        else:
            if closestTargetPos[0] < self.position[0]:
                endSquare[0] = self.position[0] - movement
            else:
                endSquare[0] = self.position[0] + movement
            if closestTargetPos[1] < self.position[1]:
                endSquare[1] = self.position[1] - movement
            else:
                endSquare[1] = self.position[1] + movement
        for element in endSquare:
            if element < 0: element = 0
            if element > self.board.size -1 : element = self.board.size -1 #don't move off the board and break the program
        while self.board.squares[tuple(endSquare)] != '': # if its target is occupied then move to an adjacent valid square
            i = 0
            if i%8 == 0:
                endSquare[1] = endSquare [1] + 1
            if self.board.squares[endSquare] == '':
                break
            if i%8 == 1:
                endSquare[0] = endSquare [0] + 1
            if self.board.squares[endSquare] == '':
                break
            if i%8 == 2:
                endSquare[1] = endSquare [1] - 1  
            if self.board.squares[endSquare] == '':
                break
            if i%8 == 3:
                endSquare[1] = endSquare [1] - 1
            if self.board.squares[endSquare] == '':
                break
            if i%8 == 4:
                endSquare[0] = endSquare [0] - 1 
            if self.board.squares[endSquare] == '':
                break 
            if i%8 == 5:
                endSquare[0] = endSquare [0] - 1    
            if self.board.squares[endSquare] == '':
                break              
            if i%8 == 6:
                endSquare[1] = endSquare [1] + 1    
            if self.board.squares[endSquare] == '':
                break              
            if i%8 == 7:
                endSquare[1] = endSquare [1] + 1    
            if self.board.squares[endSquare] == '':
                break                     
            else:
                print('Enemy is blocked! It loses its move!')                 
        self.board.squares[self.position] = ''
        self.position = endSquare
        self.board.squares[tuple(endSquare)] = self
class Friendly:
    def __init__(self, name, health, stats, position, weapon, board):
        self.name = name
        self.health = health
        self.stats = stats
        self.position = position
        if weapon['Type'] == 'Gun':
            self.atkrange = 4
        else:
            self.atkrange = 1
        self.board = board
    def takeDamage(self, damage):
        self.health = self.health - damage
        if self.health <= 0:
            self.die()
    def levelUp(self, newStats):
        self.stats = newStats
        self.health = self.stats['Max Health']
    def killEnemy(self, enemy, weapon):
        self.stats['XP'] = self.stats['XP'] + enemy.stats['XP Yield']
        weapon['Kills'] = weapon['Kills'] +1
    def die(self):
        self.board.squares[self.position] = ''
        self.board.friendlies.remove(self)
    def attack(self):
        targetSquare = [None, None]
        targetSquare[0], targetSquare[1] = map(int, input('Enter target coordinates (comma-separated): ').split(','))
        targetSquare = tuple(targetSquare)
        if (abs(self.position[0] - targetSquare[1]) <= self.atkrange and abs(self.position[1] - targetSquare[1]) <= self.atkrange):
            target = self.board.squares[targetSquare]
            if target == '':
                print("There's nothing on that square! You forfeit this unit's attack turn!!")
            elif type(target) == Friendly:
                print("Friendly fire is not permitted! You forfeit this unit's attack turn!")
            else:
                damage = hitcalcifier(self.name, target.name)
                target.takeDamage(damage)
                if target.health <= 0:
                    target.killEnemy(target)
        else:
            print("Out of range! You forfeit this unit's attack turn!")
    def move(self):
        startSquare = tuple(self.position)
        endSquare = [None, None]
        endSquare[0], endSquare[1] = map(int, input('Enter new coordinates (comma-separated): ').split(','))
        tuple(endSquare)
        if self.board.squares[endSquare] != '':
            print("Square is blocked! You forfeit this unit's move turn!")
            return()
        if (abs(startSquare[0] - endSquare[0]) <= 2 and abs(startSquare[1] - endSquare[1]) <= 2):
            self.position = endSquare
            self.board.squares[startSquare] = ''
            self.board.squares[tuple(endSquare)] = self
        else:
            print("Invalid move! You forfeit this unit's move turn!")
    def __str__(self):
        return(self.name)
def main():
    if input('Start battle? ') == 'Y':
        neededSize = int(input('Enter board size: '))
        gameBoard = Board(neededSize)
        lower_bound = int(input("Enter lower reward bound: "))
        upper_bound = int(input("Enter upper reward bound: "))
        weight = calculateReward(lower_bound, upper_bound)
        selectedEnemies = selectEnemies(weight)
        enemNum = selectedEnemies[0]
        placementList = placeEnemies(enemNum, neededSize)
        itemRewards(enemNum)
        for i in range(enemNum - 1):
            enemyName = str(selectedEnemies[1][i]) + str(i)
            try:
                stats = getEnemy(selectedEnemies[1][i])
                enemyName = Enemy(selectedEnemies[1][i], i, stats['Max Health'], stats, tuple(placementList[i]), gameBoard)
                gameBoard.placeEnemy(enemyName, placementList[i] )
            except FileNotFoundError:
                print('Enemy skipped, not defined yet.')
        gameBoard.printBoard()
        friendlySelect = []
        while len(friendlySelect) < 10:
            chooseUnit = input('Choose a unit: ')
            if chooseUnit != 'end':
                friendlySelect.append(chooseUnit)
            else:
                break
        i = 0
        while i < len(friendlySelect):
            position = [None, None]
            position[0], position[1] = map(int, input('Deploy ' + friendlySelect[i] + ' to (comma-separated): ').split(','))
            tuple(position)
            if gameBoard.squares[tuple(position)] == '':
                element = friendlySelect[i]
                stats = getChar(element)
                weapon = getWeap(stats['Weapon'])
                element = Friendly(element, stats['Max Health'], stats, tuple(position), weapon, gameBoard)
                gameBoard.placeFriendly(element, position)
                i = i + 1
            else:
                ('Square already occupied.')
        gameBoard.nextTurn()
if __name__ == "__main__":
    main()