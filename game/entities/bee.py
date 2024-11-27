import pygame as pg
import random
from game.core.entity import Entity

class Bee(Entity):

    def __init__(self, image, x, y):
        super().__init__(image, x, y)
        
        self.life = 3
        self.pts = 0
        
        pg.mixer.init()
        self.sound_pts = pg.mixer.Sound("assets/sounds/score.ogg")
        self.sound_hit = pg.mixer.Sound("assets/sounds/hit.ogg")
        
    def move(self, event):
        if event.type == pg.MOUSEMOTION:
            self.sprite.rect[0] = pg.mouse.get_pos()[0] - 35
            self.sprite.rect[1] = pg.mouse.get_pos()[1] - 30
            
    def collision(self, group, name):
        collision = pg.sprite.spritecollide(self.sprite, group, True)
        
        if name == "Flower" and collision:
            self.pts += 1
            self.sound_pts.play()
        elif name == "Spider" and collision:
            self.life -= 1
            self.sound_hit.play()