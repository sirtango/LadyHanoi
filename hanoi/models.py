
from pygame import Surface, Rect
from hanoi.constants import *

class Tower(list):
    def __init__(self):
        self.rect = Rect()

    def draw(self, screen):
    	y = 0
        for disk in self:
            screen.blit(disk, (self.pos, y))


class Disk(Surface):
    def __init__(self, width, color):
        super(Disk, self).__init__((width, DISK_HEIGHT))
        self.color = color

