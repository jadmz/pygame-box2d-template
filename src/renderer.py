
import pygame

from box2d_debug_drawer import Box2dDebugDrawer

class Renderer:
    
    def __init__(self):
        self.surface = pygame.display.set_mode((640, 480))
        self.zoom = 15
        
    def gameWillRender(self):
        self.surface.fill((255, 255, 255))

    def gameDidRender(self):
        pygame.display.flip()

    def setupDebugDraw(self, world):
        self.debugDrawer = Box2dDebugDrawer(self, self.zoom)
        world.renderer = self.debugDrawer

    def drawLine(self, p1, p2, color):
        pygame.draw.aaline(self.surface, color, p1, p2)

    def drawLines(self, points, color):
        pygame.draw.lines(self.surface, color, True, points)

    def drawPolygon(self, vertices, color):
        pygame.draw.polygon(self.surface, color, vertices, 1)

    def drawFilledPolygon(self, vertices, color):
        pygame.draw.polygon(self.surface, color, vertices)

    def drawCircle(self, center, radius, color):
        pygame.draw.circle(self.surface, color,
                           center, radius, 1)
    def drawFilledCircle(self, center, radius, color):
        pygame.draw.circle(self.surface, color,
                           center, radius, 0)
