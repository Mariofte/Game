import pygame as pg
import sys
from core import config
from entities import Player

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(config.SCREEN_SIZE)
        self.clock = pg.time.Clock()
        self.player = Player(
            x = self.screen.get_width(),
            y = self.screen.get_height(),
            screen = self.screen
        )
        self.run()
    
    def run(self):
        while config.RUNNIG:
            self.quit()
            self.screen.fill(config.RED)
            self.player.draw()
            self.player.upadate()
            pg.display.update()
            config.DT = self.clock.tick(config.FPS) / 1000

                    
        pg.quit()
        sys.exit()
    
    def quit(self):
        for event in pg.event.get():
            if event.type == pg.QUIT: config.RUNNIG = False
        
        