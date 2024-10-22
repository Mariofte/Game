import pygame
import numpy as np

def nave_player ():
    try:
        WHITE = np.array([255,255,255])
        BLACK = np.array([0,0,0])
        RED = np.array([255,0,0])
        BLUE = np.array([0,0,255])
        GREEN = np.arry([0,255,0])


    except ModuleNotFoundError as MNFE:
        print(f"No se encontro las librerias:{MNFE}")

    except Exception as error:
        print(f"Hubo un error desconocdo:{error}")