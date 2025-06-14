import pygame as pg
from core import config

class Player:
    def __init__(self, x, y):
        self.pos = pg.Vector2(x / 2, y /2)
        self.img = pg.image.load('img/nave.png').convert_alpha()
        self.img = pg.transform.scale(self.img, config.PLAYER_SIZE)
        self.rect = self.img.get_rect(center=self.pos)
        
    def draw(self, surface):
        self.rect.center = self.pos
        surface.blit(self.img, self.rect)
        
    def upadate(self, surface):
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.pos.y -= config.SPEED * config.DT
            
        if keys[pg.K_s]:
            self.pos.y += config.SPEED * config.DT
            
        if keys[pg.K_a]:
            self.pos.x -= config.SPEED * config.DT
        
        if keys[pg.K_d]:
            self.pos.x += config.SPEED * config.DT
        
        self.pos.x = max(0, min(self.pos.x, surface.get_width()))
        self.pos.y = max(0, min(self.pos.y, surface.get_height()))

class Weapon:
    def __init__(self):
        pass