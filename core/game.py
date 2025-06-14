import pygame as pg
import sys
from core import config
from entities import Player

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(config.SCREEN_SIZE)
        pg.display.set_caption('El segundo B')
        self.clock = pg.time.Clock()
        self.player = Player(
            x = self.screen.get_width(),
            y = self.screen.get_height(),
        )
        self.run()
    
    def run(self):
        while config.RUNNIG:
            self.quit()
            self.player.upadate(self.screen)
            self.screen.fill(config.WHITE)
            self.player.draw(self.screen)
            self.player.upadate(self.screen)
            pg.display.update()
            config.DT = self.clock.tick(config.FPS) / 1000

        
        pg.time.wait(1000)   
        pg.quit()
        sys.exit()
    
    def quit(self):
        for event in pg.event.get():
            if event.type == pg.QUIT: config.RUNNIG = False