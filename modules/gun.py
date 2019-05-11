import pygame
import math

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

    # TODO: Move to Engine module
    def rotate(self, angle):
        ox, oy = self.center  # Origin
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
