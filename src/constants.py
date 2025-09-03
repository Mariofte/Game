import os, sys
from dataclasses import dataclass
from typing import ClassVar

def path(path: str) -> str:
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, path) # pyright: ignore[reportAttributeAccessIssue]
    return os.path.join(os.path.abspath('.'), path)

SRC = os.path.dirname(__file__)

PROJECT = os.path.dirname(SRC)

@dataclass(frozen=True)
class GConstants:
    SIZE: tuple[int, int] = (1280, 720)
    FPS: int = 60
    COLORS: dict = {
        "BLACK": (0, 0, 0),
        "WHITE": (255, 255, 255),
        "RED": (255, 0, 0),
        "GREEN": (0, 255, 0),
        "BLUE": (0, 0, 255),
        "GRAY": (128, 128, 128),
    }

@dataclass(frozen=True)
class PConstants:
    COLORS: dict = {
        "BLACK": (0, 0, 0),
        "WHITE": (255, 255, 255),
        "RED": (255, 0, 0),
        "GREEN": (0, 255, 0),
        "BLUE": (0, 0, 255),
        "GRAY": (128, 128, 128),
    }
    PLAYER: ClassVar[str] = path(os.path.join(PROJECT, 'assets', 'sprites', 'player.png'))