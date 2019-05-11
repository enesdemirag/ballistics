import pygame
from modules.colors import *
from modules.states import BallState 

class Ball():
    def __init__(self, location, direction, radius=10, initial_velocity=0.0, mass=1.0, elasticity=0.5):
        self.location = location
        self.direction = direction
        self.radius = radius
        self.initial_velocity = initial_velocity
        self.mass = mass
        self.elasticity = elasticity
        self.state = BallState.PENDING

    def draw(self, surface, colour=BLACK):
        pygame.draw.circle(surface, colour, self.location, self.radius, 0)
