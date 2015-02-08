
from pygame import Surface, Rect
from hanoi.constants import *

class Tower(list):
    def __init__(self, n):
        left = SCREEN_HMARGIN + TOWER_MARGIN * (n * 2 + 1) + TOWER_WIDTH * n
        top = SCREEN_VMARGIN

        self.rect = Rect(left, top, TOWER_WIDTH, TOWER_HEIGHT)

    def draw(self, screen):
        pos = 1
        for disk in self:
            left = self.rect.left + (self.rect.width - disk.get_width()) / 2
            top = self.rect.top + self.rect.height - pos * disk.get_height()
            screen.blit(disk, (left, top))
            pos = pos + 1


class Disk(Surface):
    def __init__(self, n, color):
        width = TOWER_WIDTH - n * DISK_WIDTH_STEP
        super(Disk, self).__init__((width, DISK_HEIGHT))
        self.color = color
        self.fill(color)

