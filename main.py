import pygame
import random
from modules.states import *
from modules.colors import *
from modules.engine import *
from modules.world import World
from modules.cannon import Cannon
from modules.target import Target
from modules.obstacle import Obstacle

# Initialize
pygame.init()
pygame.display.set_caption("Ballistics")
world = World()

# Random Obstacles
for obstacle in world.obstacles:
    x = random.randint(obstacle.getSize()[0], (world.getSize()[0] - obstacle.getSize()[0]))
    y = random.randint(obstacle.getSize()[1], (world.getSize()[1] - obstacle.getSize()[1]))
    size_x = random.randint(10, 100)
    size_y = random.randint(10, 100)
    obstacle.setLocation((x, y))
    obstacle.setSize((size_x, size_y))

# Parameters
screen = pygame.display.set_mode(world.size)
clock = pygame.time.Clock()
FPS = 60
direction = 0
font = pygame.font.SysFont('Arial', 20)
balls_label = font.render('3', False, (0, 0, 0))

# Redraw everything on screen
def refresh():
    screen.fill(WHITE)
    world.cannon.draw(screen)
    world.target.draw(screen)
    for obstacle in world.obstacles:
        obstacle.draw(screen)
    for ball in world.cannon.balls:
        ball.draw(screen)


# Loop
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
    screen.blit(balls_label, (5, 5))
    pygame.display.update()
