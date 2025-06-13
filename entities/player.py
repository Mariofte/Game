import pygame as pg
from core import config

class Player:
    def __init__(self, x, y):
        self.pos = pg.Vector2(x / 2, y /2)
        self.img = pg.image.load('img/nabe.png').convert_alpha()
        self.img = pg.transform.scale(self.img, config.PLAYER_SIZE)
        self.rect = self.img.get_rect(center=self.pos)
        
    def draw(self, surface):
        self.rect.center = self.pos
        surface.blit(self.img, self.rect)
        
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