from dataclasses import dataclass

@dataclass(frozen=True)
class GConstants:
    SIZE: tuple[int, int] = (1280, 720)
    FPS: int = 60
    COLORS = {
        "BLACK": (0, 0, 0),
        "WHITE": (255, 255, 255),
        "RED": (255, 0, 0),
        "GREEN": (0, 255, 0),
        "BLUE": (0, 0, 255),
        "GRAY": (128, 128, 128),
    }

dataclass(frozen=True)
class PConstants:
    COLORS = {
        "BLACK": (0, 0, 0),
        "WHITE": (255, 255, 255),
        "RED": (255, 0, 0),
        "GREEN": (0, 255, 0),
        "BLUE": (0, 0, 255),
        "GRAY": (128, 128, 128),
    }