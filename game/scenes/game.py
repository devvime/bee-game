import pygame as pg
import random
from game.core.entity import Entity, Text
from game.entities.bee import Bee

class Game:

    def __init__(self):
        self.bg = Entity("assets/bg.png", 0, 0)
        self.bg2 = Entity("assets/bg.png", 0, -640)
        self.change_scene = False
        
        self.spider = Entity("assets/spider1.png", random.randrange(0, 300), -50)
        self.florwer = Entity("assets/florwer1.png", random.randrange(0, 300), -50)
        self.bee = Bee("assets/bee1.png", 150, 500)
        
        self.score = Text(text="0", size=80, pos=(150, 50))
        self.lifes = Text(text="3", size=40, pos=(50, 50))
        
    def draw(self, window):
        self.bg.draw(window)
        self.bg2.draw(window)
        self.bee.draw(window)
        self.spider.draw(window)
        self.florwer.draw(window)
        self.score.draw(window)
        self.lifes.draw(window)
        
    def events(self, event):        
        self.bee.move(event)
          
    def update(self):
        self.move_bg()
        self.bee.anim("bee", tick=2, frames=4)
        self.spider.anim("spider", tick=8, frames=4)
        self.florwer.anim("florwer", tick=8, frames=2)
        self.move_spiders()
        self.move_florwer()
        
        self.bee.collision(self.spider.group, "Spider")
        self.bee.collision(self.florwer.group, "Flower")
        
        self.gameover()
        
        self.score.update_text(str(self.bee.pts))
        self.lifes.update_text(str(self.bee.life))
            
    def move_bg(self):
        self.bg.sprite.rect[1] += 4
        self.bg2.sprite.rect[1] += 4
        
        if self.bg.sprite.rect[1] >= 640:
            self.bg.sprite.rect[1] = 0
            
        if self.bg2.sprite.rect[1] >= 0:
            self.bg2.sprite.rect[1] = -640
            
    def move_spiders(self):
        self.spider.sprite.rect[1] += 10
        
        if self.spider.sprite.rect[1] >= 700:
            self.spider.sprite.kill()
            self.spider = Entity("assets/spider1.png", random.randrange(0, 300), -50)
            
    def move_florwer(self):
        self.florwer.sprite.rect[1] += 6
        
        if self.florwer.sprite.rect[1] >= 700:
            self.florwer.sprite.kill()
            self.florwer = Entity("assets/florwer1.png", random.randrange(0, 300), -50)
            
    def gameover(self):
        if self.bee.life <= 0:
            self.change_scene = True