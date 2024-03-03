from CommanderWhite import *
from InstructorBlack import *
from Anemone import *
# I was listening to the Drakengard 1 OST as I created this thing so please excuse any terrible code moments
# It also might be a good idea to have some more input validation on this -- I really want to avoid having to scrap an entire battle because
# a single mistyped input caused the whole thing to shit itself
# Update, 2024-02-15: yup
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
        self.log = ""
    def enemyTurn(self):
        for element in self.enemies:
            selectedenemy = element
            selectedenemy.attack()
        if len(self.friendlies) == 0:
            input('All of your units have died!')
            print(self.log)
            exit
        self.playerTurn()
    def playerTurn(self):
        for element in self.friendlies:
            print('Your turn.')
            self.printBoard()
            selectedfriendly = element
            selectedfriendly.move()
            selectedfriendly.attack()
        if len(self.enemies) == 0:
            input('Well done, you have won!')
            print(self.log)
            exit
        self.enemyTurn()
    def placeEnemy(self, enemy, position):
        self.squares[tuple(position)] = enemy
        self.enemies.append(enemy)
    def placeFriendly(self, friendly, position):
        self.squares[tuple(position)] = friendly
        self.friendlies.append(friendly)
    def printBoard(self):
        neededSize = self.size
        print('     ', end = '')
        for i in range(neededSize):
            print('|'+ '{:^15}'.format(str(i)) +'|', end = '')
        print()
        print('     '+ '—————————————————'*neededSize) 
        for i in range(neededSize):
            print('{:^5}'.format(str(i)), end = '')
            for j in range(neededSize):
                if self.squares[(i, j)] != '':
                    print('|' + '{:^15}'.format(str(self.squares[(i, j)])+ ' '+ str(self.squares[(i, j)].health)) + '|', end='')
                else:
                    print('|               |', end = '')
            print('{:^5}'.format(str(i)))
            print('     '+ '—————————————————'*neededSize)    
            
    def __str__(self):
        return(self.squares)
class Enemy:
    def __init__(self, unittype, health, stats, position, board):
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
        self.board.enemies.remove(self)
        self.board.log = self.board.log + self.name + " has died. \n"
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
        if distance <= 1:
            target = self.board.squares[tuple(closestTargetPos)]
            damage = hitcalcifier(self.name, target.name)
            target.takeDamage(damage)
            self.board.log = self.board.log + self.name + " attacked " + target.name + ' and dealt ' + str(damage) + ' damage. \n'
        else:
            self.move()
    def move(self):
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
            endSquare = list(closestTargetPos)
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
            if self.board.squares[tuple(endSquare)] == '':
                break
            if i%8 == 1:
                endSquare[0] = endSquare [0] + 1
            if self.board.squares[tuple(endSquare)] == '':
                break
            if i%8 == 2:
                endSquare[1] = endSquare [1] - 1  
            if self.board.squares[tuple(endSquare)] == '':
                break
            if i%8 == 3:
                endSquare[1] = endSquare [1] - 1
            if self.board.squares[tuple(endSquare)] == '':
                break
            if i%8 == 4:
                endSquare[0] = endSquare [0] - 1 
            if self.board.squares[tuple(endSquare)] == '':
                break 
            if i%8 == 5:
                endSquare[0] = endSquare [0] - 1    
            if self.board.squares[tuple(endSquare)] == '':
                break              
            if i%8 == 6:
                endSquare[1] = endSquare [1] + 1    
            if self.board.squares[tuple(endSquare)] == '':
                break              
            if i%8 == 7:
                endSquare[1] = endSquare [1] + 1    
            if self.board.squares[tuple(endSquare)] == '':
                break                     
            else:
                print('Enemy is blocked! It loses its move!')    
        try:
            self.board.squares[tuple(self.position)] = ''
            self.board.log = self.board.log + self.name + " moved from (" + str(self.position[0]) + "," + str(self.position[1]) + ') to (' +  str(endSquare[0])+ ',' + str(endSquare[1]) +  '). \n'
            self.position = tuple(endSquare)
            self.board.squares[tuple(endSquare)] = self
        except KeyError:
            print('Enemy is blocked! It loses its move!')
        
class Friendly:
    def __init__(self, name, health, stats, position, weapon, board):
        self.name = name
        self.health = health
        self.stats = stats
        self.position = position
        self.weapon = weapon
        if self.weapon['Type'] == 'Gun':
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
    def killEnemy(self, enemy):
        for element in self.board.friendlies:
            grantXP(element.name, enemy.stats['Yield']//2)
        grantXP(self.name, enemy.stats['Yield'])
        self.stats = getChar(self.name)
        weapKill(self.stats['Weapon'])
        statincreasifier(self.weapon['Type'], self.stats, self.name)
        self.weap = getWeap(self.stats['Weapon'])
        for element in itemRewards(1):
            print(element, "dropped by the enemy!")
            addItem(element)
    def die(self):
        self.board.squares[self.position] = ''
        self.board.friendlies.remove(self)
        self.board.log = self.board.log + self.name + " has died. \n"
    def attack(self):
        targetSquare = [None, None]
        targetSquare[0], targetSquare[1] = map(int, input('Enter target coordinates (comma-separated): ').split(','))
        targetSquare = tuple(targetSquare)
        if (abs(self.position[0] - targetSquare[0]) <= self.atkrange and abs(self.position[1] - targetSquare[1]) <= self.atkrange):
            target = self.board.squares[targetSquare]
            if target == '':
                print("There's nothing on that square! You forfeit this unit's attack turn!!")
            elif type(target) == Friendly:
                print("Friendly fire is not permitted! You forfeit this unit's attack turn!")
            else:
                damage = hitcalcifier(self.name, target.name)
                target.takeDamage(damage)
                self.board.log = self.board.log + self.name + " attacked " + target.name + ' and dealt ' + str(damage) + ' damage. \n'
                if target.health <= 0:
                    self.killEnemy(target)
        else:
            print("Out of range! You forfeit this unit's attack turn!")
    def move(self):
        startSquare = tuple(self.position)
        endSquare = [None, None]
        endSquare[0], endSquare[1] = map(int, input('Enter new coordinates (comma-separated): ').split(','))
        tuple(endSquare)
        if self.board.squares[tuple(endSquare)] != '':
            print("Square is blocked! You forfeit this unit's move turn!")
            return()
        if (abs(startSquare[0] - endSquare[0]) <= 2 and abs(startSquare[1] - endSquare[1]) <= 2):
            self.board.log = self.board.log + self.name + " moved from (" + str(self.position[0]) + "," + str(self.position[1]) + ') to (' +  str(endSquare[0])+ ',' + str(endSquare[1]) +  '). \n'
            self.position = endSquare
            self.board.squares[startSquare] = ''
            self.board.squares[tuple(endSquare)] = self
            self.board.printBoard()
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
                enemyName = Enemy(selectedEnemies[1][i], stats['Max Health'], stats, tuple(placementList[i]), gameBoard)
                gameBoard.placeEnemy(enemyName, placementList[i] )
            except FileNotFoundError:
                print('Enemy skipped, not defined yet.')
        gameBoard.printBoard()
        friendlySelect = []
        while len(friendlySelect) < 10:
            chooseUnit = input('Choose a unit: ')
            if (chooseUnit != 'end') and (chooseUnit not in friendlySelect):
                friendlySelect.append(chooseUnit)
            else:
                break
        i = 0
        while i < len(friendlySelect):
            position = [None, None]
            try:
                position[0], position[1] = map(int, input('Deploy ' + friendlySelect[i] + ' to (comma-separated): ').split(','))
            except ValueError:
                print('What?')
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
        gameBoard.enemyTurn()
if __name__ == "__main__":
    main()