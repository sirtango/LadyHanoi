
from pygame import Surface
from hanoi.constants import *

class Tower(list):
    def __init__(self):
        self.pos = 0

class Disk(Surface):
    def __init__(self, width, color):
        super(Disk, self).__init__((width, DISK_HEIGHT))
        self.color = color

t = Tower()
t.append(Disk(180, (255, 0, 0)))
t.append(Disk(160, (0, 123, 0)))