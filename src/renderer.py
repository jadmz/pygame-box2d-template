
import pygame

from box2d_debug_drawer import Box2dDebugDrawer

class Renderer:
    
    def __init__(self):
        self.surface = pygame.display.set_mode((640, 480))
        self.zoom = 15
        self.offset = (0,0)
        
    def gameWillRender(self):
        self.surface.fill((255, 255, 255))

    def gameDidRender(self):
        pygame.display.flip()

    def setupDebugDraw(self, world):
        self.debugDrawer = Box2dDebugDrawer(self, self.zoom, self.offset)
        world.renderer = self.debugDrawer

    def drawLine(self, p1, p2, color, convertPoints=True):
        if convertPoints:
            p1 = self.toScreenPoint(p1)
            p2 = self.toScreenPoint(p2)

        pygame.draw.aaline(self.surface, color, p1, p2)

    def drawLines(self, points, color, convertPoints=True):
        if convertPoints:
            points = map((lambda point: self.toScreenPoint(point)), points)
                
        pygame.draw.lines(self.surface, color, True, points)

    def drawPolygon(self, vertices, color, convertPoints=True):
        if convertPoints:
            vertices = map((lambda vertex: self.toScreenPoint(vertex)), vertices)
        pygame.draw.polygon(self.surface, color, vertices, 1)

    def drawFilledPolygon(self, vertices, color, convertPoints=True):
        if convertPoints:
            vertices = map((lambda vertex: self.toScreenPoint(vertex)), vertices)
        pygame.draw.polygon(self.surface, color, vertices)

    def drawCircle(self, center, radius, color, convertPoints=True):
        if convertPoints:
            center = self.toScreenPoint(center)
            radius = radius * self.zoom
        radius = int(radius)
        pygame.draw.circle(self.surface, color,
                           center, radius, 1)
    def drawFilledCircle(self, center, radius, color, convertPoints=True):
        if convertPoints:
            center = self.toScreenPoint(center)
            radius = radius * self.zoom
        radius = int(radius)
        pygame.draw.circle(self.surface, color,
                           center, radius, 0)

    def toScreenPoint(self, point):
        """
        Takes a world point and converts it to a screen point. Takes into account the
        rendering zoom and offset.
        """

        x=(point.x * self.zoom)-self.offset.x
        y=(point.y * self.zoom)-self.offset.y
        return (x, y)
