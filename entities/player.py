import pygame as pg
from core import config

class Player:
    def __init__(self, x, y, screen):
        self.screen = screen
        self.pos = pg.Vector2(x / 2, y /2)
    
    def draw(self):
        pg.draw.circle(self.screen, config.BLUE, self.pos, config.RADIUS)
    
    def upadate(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.pos.y -= config.SPEED * config.DT
            
        if keys[pg.K_s]:
            self.pos.y += config.SPEED * config.DT
            
        if keys[pg.K_a]:
            self.pos.x -= config.SPEED * config.DT
        
        if keys[pg.K_d]:
            self.pos.x += config.SPEED * config.DT