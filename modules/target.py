import pygame
from modules.colors import *

class Target():
    def __init__(self, location):
        self.location = location

    def draw(self, surface, colour=RED):
        pygame.draw.circle(surface, colour, self.location, 25, 0)


