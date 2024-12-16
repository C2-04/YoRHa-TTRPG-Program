#oh boy, a GUI
from CommanderWhite import *
from InstructorBlack import *
from masamune import *
from Anemone import *
from TwoB import *
from time import sleep
import pygame as pg
import pygame_menu
from pygame_menu import themes
 
pg.init()
surface = pg.display.set_mode((600, 400))
 
def setMissionType(missionName, missionID):
    print(missionName)
    print(missionID)
 
def start_the_game():
    pass
 
def level_menu():
    mainmenu._open(level)
 
 
mainmenu = pygame_menu.Menu('Welcome', 600, 400, theme=themes.THEME_SOLARIZED)
mainmenu.add.text_input('Name: ', default='username', maxchar=20)
mainmenu.add.button('Play', start_the_game)
mainmenu.add.button('Mission Types', level_menu)
mainmenu.add.button('Quit', pygame_menu.events.EXIT)
 
level = pygame_menu.Menu('Select Mission Parameters', 600, 400, theme=themes.THEME_BLUE)
level.add.selector('Type :', [('Standard', 1), ('Endless', 2)], onchange=setMissionType)


TITLE = "Grid"
TILES_HORIZONTAL = 12
TILES_VERTICAL = TILES_HORIZONTAL
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000
TILE_SIZE = (WINDOW_WIDTH-50)/TILES_HORIZONTAL

def start_the_game():
    mygame = Game()
    mygame.main()
class Player:
    def __init__(self, surface):
        self.surface = surface
        self.pos = (40, 40)

    def draw(self):
        pg.draw.circle(self.surface, (255, 255, 255), self.pos, TILE_SIZE/2)

    def move(self, target):
        x = (TILE_SIZE * (target[0] // TILE_SIZE)) + TILE_SIZE/2 + 25
        y = (TILE_SIZE * (target[1] // TILE_SIZE)) + TILE_SIZE/2 + 25

        self.pos = (x, y)


class Game:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        pg.display.set_caption(TITLE)
        self.surface = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.loop = True
        self.player = Player(self.surface)

    def main(self):
        while self.loop:
            self.grid_loop()
        pg.quit()

    def grid_loop(self):
        self.surface.fill((0, 0, 0))
        for row in range(TILES_HORIZONTAL):
            for col in range(row % 2, TILES_HORIZONTAL, 2):
                pg.draw.rect(
                    self.surface,
                    (40, 40, 40),
                    (row * TILE_SIZE + 25, col * TILE_SIZE+ 25, TILE_SIZE, TILE_SIZE),
                )
        self.player.draw()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.loop = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.loop = False
            elif event.type == pg.MOUSEBUTTONUP:
                mousePos = pg.mouse.get_pos()
                realPos = list(mousePos)
                realPos[0], realPos[1] = realPos[0] - 25, realPos[1] - 25
                self.player.move(realPos)
        pg.display.update()



while True:
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            exit()
 
    if mainmenu.is_enabled():
        mainmenu.update(events)
        mainmenu.draw(surface)
 
    pg.display.update()