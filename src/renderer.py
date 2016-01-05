
import pygame

from box2d_debug_drawer import Box2dDebugDrawer

class Renderer:
    
    def __init__(self):
        self.windowSurface = pygame.display.set_mode((640, 480))
        
    def gameWillRender(self):
        self.windowSurface.fill((255, 255, 255))

    def gameDidRender(self):
        pygame.display.flip()

    def setupDebugDraw(self, world):
        self.debugDrawer = Box2dDebugDrawer(self.windowSurface)
        world.renderer = self.debugDrawer
        
