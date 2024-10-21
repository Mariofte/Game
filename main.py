import pygame 
import sys
import os 

def main ():
    # posicionar la vaentana en la pantalla
    os.environ['SDL_VIDEO_WINDOW_POS'] = "300,100"
    
    # Inicializar pygame
    pygame.init()

    # Tamaño de la ventana
    tam = (800,800)
    screen = pygame.display.set_mode(size = tam)
    
    # fps
    #clock = pygame.time.Clock()

    # Nombre de la ventana
    pygame.display.set_caption(title="El perdido")
    
    running = True
    while running:
        try:
            
            
            # Revisar los eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # Si el gugador cierra la vantana
                    running = False
            
            # Actualizar la pantalla
            pygame.display.flip()
            
            # clock.tick(framerate=60)
            
        except ModuleNotFoundError as error:
            print(f"Error de líbrerias:{error}")
            running = False
        
        except pygame.error as error:
            print(f"Error en el codígo: {error}")
            running = False
        
        except Exception as error:
            print(f"Error desconocido:{error}")
            running = False
            
    # Salir de pygame
    pygame.quit()
    sys.exit()
    
if __name__ == '__main__':
    main()

