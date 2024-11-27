import pygame as pg

class Entity:

    def __init__(self, image_path, x, y):
        
        self.frame = 1
        self.tick = 0
        
        self.group = pg.sprite.Group()
        self.sprite = pg.sprite.Sprite(self.group)
        self.sprite.image = pg.image.load(image_path)
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect[0] = x
        self.sprite.rect[1] = y
        
    def draw(self, window):
        self.group.draw(window)
        
    def anim(self, image, tick=None, frames=0):
        self.tick += 1
        if self.tick >= tick:
            self.tick = 0
            self.frame += 1
            
        if self.frame > frames:
            self.frame = 1
            
        self.sprite.image = pg.image.load("assets/"+ image + str(self.frame) + ".png")
        
class Text:
    
    def __init__(self, text="0", size=30, pos=(0, 0), color=(255, 255, 255)):
        
        self.pos = pos
        self.color = color
        
        self.font = pg.font.Font("assets/font/PixelGameFont.ttf", size)
        self.reder = self.font.render(text, False, self.color)
        
    def draw(self, window):
        window.blit(self.reder, self.pos)
        
    def update_text(self, text):
        self.reder = self.font.render(text, False, self.color)