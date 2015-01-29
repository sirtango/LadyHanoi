
import pygame
from pygame.locals import *

def main():
    """ejecuta el juego hanoi"""
    
    pygame.init()
    pygame.display.set_mode((640, 480))

    screen = pygame.display.get_surface()

    square = pygame.Surface((64, 64))
    square.fill((255, 255, 0))

    square_x = 128

    clock = pygame.time.Clock()

    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == QUIT:
                return

        screen.fill((68, 123, 200))
        screen.blit(square, (square_x, 128))
        square_x = square_x + 1

        pygame.display.update()


if __name__ == '__main__':
    main()
