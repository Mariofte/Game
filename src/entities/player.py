from turtle import Screen
import pygame as py
from constants import PConstants

class Player:
    def __init__(self, screen: py.Surface) -> None:
        self.position = py.Vector2(screen.get_width() / 2, screen.get_height() / 2)
        self.screen = screen
        
    def draw(self, dt:float = 0) -> None:
        py.draw.circle(self.screen, PConstants.COLORS['BLUE'], self.position, 40)
        keys = py.key.get_pressed()
        if keys[py.K_w]:
            self.position.y -= 300 * dt
        if keys[py.K_d]:
            self.position.x += 300 * dt
        if keys[py.K_a]:
            self.position.x -= 300 * dt
        if keys[py.K_s]:
            self.position.y += 300 * dt