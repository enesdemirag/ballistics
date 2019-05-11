import pygame
from modules.cannon import Cannon
from modules.target import Target
from modules.obstacle import Obstacle

class World():
    def __init__(self, size=(800, 400), gravity=9.8, wind_force=0.0, wind_direction=None, number_of_obstacles=3):
        self.size = size
        self.gravity = gravity
        self.wind_force = wind_force
        self.wind_direction = wind_direction
        self.cannon = Cannon(radius=50, location=(100, 400))
        self.target = Target(location=(600, 50))
        self.obstacles = [Obstacle(location=(0, 0), size=(50, 10))
                          for i in range(number_of_obstacles)]

    def getSize(self):
        return self.size
