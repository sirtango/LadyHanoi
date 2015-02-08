
import pygame
from pygame.locals import *
from hanoi.models import Tower, Disk
from hanoi.constants import *
from hanoi.logic import select_tower

def main():
    """ejecuta el juego hanoi"""
    
    pygame.init()
    pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    screen = pygame.display.get_surface()

    tower1 = Tower(0)
    tower2 = Tower(1)
    tower3 = Tower(2)

    tower1.append(Disk(0, (255, 0, 0)))
    tower1.append(Disk(1, (255, 102, 51)))
    tower1.append(Disk(2, (191, 0, 255)))
    tower1.append(Disk(3, (61, 255, 255)))
    tower1.append(Disk(4, (61, 255, 61)))
    tower1.append(Disk(5, (255, 255, 61)))

    tower_selected = None

    clock = pygame.time.Clock()

    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == KEYUP:
                if event.key == K_1:
                    tower_selected = select_tower(tower_selected, tower1)
                elif event.key == K_2:
                    tower_selected = select_tower(tower_selected, tower2)
                elif event.key == K_3:
                    tower_selected = select_tower(tower_selected, tower3)

        screen.fill((68, 123, 200))

        tower1.draw(screen)
        tower2.draw(screen)
        tower3.draw(screen)

        if len(tower3) == 6:
            tower3 = Tower(2)

        pygame.display.update()


if __name__ == '__main__':
    main()
