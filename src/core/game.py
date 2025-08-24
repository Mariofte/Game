import pygame as py
from entities import Player
from constants import GConstants

class Game:
    def __init__(self) -> None:
        py.init()
        self.screen = py.display.set_mode(GConstants.SIZE)
        self.clock = py.time.Clock()
        self.runnig = True
        self.dt = 0
        self.player = Player(self.screen)
        self.run()
        py.quit()
    
    def run(self) -> None:
        while self.runnig:
            self.event()
            self.update()
            self.draw()
            self.update()
    
    def event(self) -> None:
        for event in py.event.get():
            if event.type == py.QUIT: self.runnig = False
    
    def update(self) -> None:
        self.dt = self.clock.tick(GConstants.FPS) / 1000
    
    def draw(self) -> None:
        self.screen.fill(GConstants.COLORS["RED"])
        self.player.draw(self.dt)
        py.display.flip()