import pygame
from pygame.locals import *
from enum import Enum
import math
import random

BLACK = pygame.Color("black")
WHITE = pygame.Color("white")
RED = pygame.Color("red")

class State(Enum):
    PENDING = -1
    FIRE = 0
    HIT = 1
    MISS = 2

class Ball():
    def __init__(self, location, direction, radius=10, initial_velocity=0.0, mass=1.0, elasticity=0.5):
        self.location = location
        self.direction = direction
        self.radius = radius
        self.initial_velocity = initial_velocity
        self.mass = mass
        self.elasticity = elasticity
        self.state = State.PENDING

    def draw(self, surface, colour=BLACK):
        pygame.draw.circle(surface, colour, self.location, self.radius, 0)

class Gun():
    def __init__(self, center, rotation, size_x, size_y):
        self.center = center
        self.points = [((center[0] - size_x), (center[1] + size_y)),
                       ((center[0] + size_x), (center[1] + size_y)),
                       ((center[0] + size_x), (center[1] + 3 * size_y)),
                       ((center[0] - size_x), (center[1] + 3 * size_y))]
        self.rotation = 0
        self.rotate(rotation)

    def getPoints(self):
        return self.points

    def getRotation(self):
        return self.rotation

    def rotate(self, angle):
        ox, oy = self.center # Origin
        new_points = []
        self.rotation += angle
        if self.rotation <= 1.85 or self.rotation >= 4.40:
            self.rotation -= angle
            return
        for point in self.points:
            px, py = point
            qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
            qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
            new_points.append((qx, qy))
        self.points = new_points


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


class Obstacle():
    def __init__(self, location, size):
        self.location = location
        self.size = size
        self.rect = Rect(self.location[0] - (self.size[0] // 2), self.location[1] - (self.size[1] // 2), self.size[0], self.size[1])

    def getSize(self):
        return self.size
    
    def setSize(self, size):
        self.size = size
        self.rect = Rect(self.location[0] - (self.size[0] // 2), self.location[1] - (self.size[1] // 2), self.size[0], self.size[1])

    def draw(self, surface, colour=BLACK):
        pygame.draw.rect(surface, colour, self.rect, 0)

    def setLocation(self, location):
        self.location = location
        self.rect = Rect(self.location[0] - (self.size[0] // 2), self.location[1] - (self.size[1] // 2), self.size[0], self.size[1])

class Target():
    def __init__(self, location):
        self.location = location

    def draw(self, surface, colour=RED):
        pygame.draw.circle(surface, colour, self.location, 25, 0)

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

# Initialize

pygame.init()
pygame.display.set_caption("Ballistics")

world = World()
for obstacle in world.obstacles:
    x = random.randint(obstacle.getSize()[0], (world.getSize()[0] - obstacle.getSize()[0]))
    y = random.randint(obstacle.getSize()[1], (world.getSize()[1] - obstacle.getSize()[1]))
    size_x = random.randint(10, 100)
    size_y = random.randint(10, 100)
    obstacle.setLocation((x, y))
    obstacle.setSize((size_x, size_y))

screen = pygame.display.set_mode(world.size)
clock = pygame.time.Clock()
FPS = 60
direction = 0
font = pygame.font.SysFont('Arial', 20)
balls = font.render('3', False, (0, 0, 0))

def refresh():
    screen.fill(WHITE)
    world.cannon.draw(screen)
    world.target.draw(screen)
    for obstacle in world.obstacles:
        obstacle.draw(screen)
    for ball in world.cannon.balls:
        ball.draw(screen)


while True:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = -1
            elif event.key == pygame.K_RIGHT:
                direction = 1
            elif event.key == pygame.K_UP:
                if world.cannon.gun.getRotation() >= 3.2:
                    direction = -1
                else:
                    direction = 1
            elif event.key == pygame.K_DOWN:
                if world.cannon.gun.getRotation() >= 3.2:
                    direction = 1
                else:
                    direction = -1
        elif event.type == pygame.KEYUP:
            direction = 0
    
    if direction != 0:
        world.cannon.gun.rotate(direction * 0.05)
    

    # checkCollision()
    refresh()
    screen.blit(balls, (5, 5))
    pygame.display.update()
