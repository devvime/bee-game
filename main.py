import pygame as pg
from game.scenes.menu import Menu
from game.scenes.game import Game
from game.scenes.gameover import GameOver

class Main:
    
    def __init__(self, size_x, size_y, title):
        
        pg.init()
        pg.mixer.init()
        pg.mixer.music.load("assets/sounds/bg.ogg")
        pg.mixer.music.play(-1)
        
        self.window = pg.display.set_mode([size_x, size_y])
        self.title = pg.display.set_caption(title)
        self.loop = True
        self.fps = pg.time.Clock()
        
        self.menu = Menu()
        self.game = Game()
        self.gameover = GameOver()
        
    def draw(self):
        self.window.fill([0, 0, 0])
        if not self.menu.change_scene:
            self.menu.draw(self.window)
        elif not self.game.change_scene:
            self.game.draw(self.window)
            self.game.update()
        elif not self.gameover.change_scene:
            self.gameover.draw(self.window)
        else:
            self.menu.change_scene = False
            self.gameover.change_scene = False
            self.game.change_scene = False
            self.game.bee.life = 3
            self.game.bee.pts = 0
    
    def events(self):
        for events in pg.event.get():
            if events.type == pg.QUIT:
                self.loop = False
            
            if not self.menu.change_scene:
                self.menu.events(events)
            elif not self.game.change_scene:
                self.game.events(events)
            elif not self.gameover.change_scene:
                self.gameover.events(events)
                
    def update(self):
        while self.loop:
            self.fps.tick(30)
            self.draw()
            self.events()
            pg.display.update()
        
        
game = Main(360, 640, "BeHoney")
game.update()