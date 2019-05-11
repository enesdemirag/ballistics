import pygame
from pygame.locals import *
from modules.colors import *

class Obstacle():
    def __init__(self, location, size):
        self.location = location
        self.size = size
        self.rect = Rect(self.location[0] - (self.size[0] // 2),
                         self.location[1] - (self.size[1] // 2),
                         self.size[0],
                         self.size[1])

    def getSize(self):
        return self.size

    def setSize(self, size):
        self.size = size
        self.rect = Rect(self.location[0] - (self.size[0] // 2),
                         self.location[1] - (self.size[1] // 2),
                         self.size[0],
                         self.size[1])

    def draw(self, surface, colour=BLACK):
        pygame.draw.rect(surface, colour, self.rect, 0)

    def setLocation(self, location):
        self.location = location
        self.rect = Rect(self.location[0] - (self.size[0] // 2),
        self.location[1] - (self.size[1] // 2),
        self.size[0],
        self.size[1])
