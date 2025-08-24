import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="pygame.pkgdata")

from core import Game

def main():
    Game()

if __name__ == '__main__':
    main()