import pygame 
import sys

def main ():
    
    # Inicializar pygame
    pygame.init()

    # Tamaño de la ventana
    tam = (800,600)
    screen = pygame.display.set_mode(size = tam)

    # Nombre de la ventana
    pygame.display.set_caption(title="El perdido")
    
    runnig = True
    while runnig:
        try:
            
            
            # Revisar los eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # Si el gugador cierra la vantana
                    runnig = False
            
            # Actualizar la pantalla
            pygame.display.flip()
            
        except ModuleNotFoundError as error:
            print(f"Error de líbrerias:{error}")
            
        except pygame.error as error:
            print(f"Error en el codígo: {error}")
            runnig = False
        
        except Exception as error:
            print(f"Error desconocido:{error}")
            
    # Salir de pygama
    pygame.quit()
    sys.exit()
    
if __name__ == '__main__':
    main()

