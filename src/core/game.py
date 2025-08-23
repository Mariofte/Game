from tkinter import NO
import pygame as py

class Game:
    def __init__(self) -> None:
        py.init()
        self.screen = py.display.set_mode((1280, 720))
        self.clock = py.time.Clock()
        self.runnig = True
        self.run()
        py.quit()
    
    def run(self) -> None:
        while self.runnig:
            self.event()
            self.screen.fill("white")
            py.display.flip()
            self.clock.tick(60)
    
    def event(self) -> None:
        for event in py.event.get():
            if event.type == py.QUIT: self.runnig = False