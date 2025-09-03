import pygame as py

class Gamepad:
    def __init__(self) -> None:
        py.joystick.init()