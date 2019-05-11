import pygame
from modules.colors import *
from modules.gun import Gun
from modules.ball import Ball

class Cannon():
    def __init__(self, radius, location, gun_rotation=3, number_of_balls=3, ball_radius=20):
        self.radius = radius
        self.location = location
        self.gun_rotation = gun_rotation
        self.gun = Gun(self.location, self.gun_rotation, ball_radius // 2, self.radius // 2)
        self.balls = [Ball(location=self.location, direction=self.gun_rotation, radius=ball_radius)
                      for i in range(number_of_balls)]

    def draw(self, surface, colour=BLACK):
        pygame.draw.circle(surface, colour, self.location, self.radius, 0) # Base
        pygame.draw.polygon(surface, colour, self.gun.getPoints(), 0)  # Gun
