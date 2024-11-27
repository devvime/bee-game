import pygame as pg
from game.core.entity import Entity

class GameOver:

    def __init__(self):
        self.bg = Entity("assets/gameover.png", 0, 0)
        self.change_scene = False
        
    def draw(self, window):
        self.bg.draw(window)
        
    def events(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RETURN:
                self.change_scene = True
        
        if event.type == pg.KEYUP:
            pass