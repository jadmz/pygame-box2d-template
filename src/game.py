import sys
import warnings

try:
    import pygame_sdl2
except ImportError:
    if sys.platform in ('darwin', ):
        warnings.warn('OSX has major issues with pygame/SDL 1.2 when used '
                      'inside a virtualenv. If this affects you, try '
                      'installing the updated pygame_sdl2 library.')
else:
    # pygame_sdl2 is backward-compatible with pygame:
    pygame_sdl2.import_as_pygame()

import pygame

from pygame.locals import (QUIT, KEYDOWN, KEYUP, MOUSEBUTTONDOWN,
                           MOUSEBUTTONUP, MOUSEMOTION, KMOD_LSHIFT)

from Box2D import (b2World, b2PolygonShape)

from renderer import Renderer
from game_object import GameObject

class Game:

    FRAMES_PER_SECOND = 60

    def __init__(self, title):
        pygame.init()
        pygame.display.set_caption(title)
        
        self.running = False
        self.clock = pygame.time.Clock()
        self.renderer = Renderer()
        self.world = b2World(gravity=(0,-10), doSleep=True)
        self.renderer.setupDebugDraw(self.world)
        self.gameObjects = []

        body = self.world.CreateDynamicBody(position=(10,-10))
        box = body.CreatePolygonFixture(box=(1,1), density=1, friction=0.3)
        self.player = self.createObject(physics=box)

    def run(self):
        self.running = True

        while self.running:
            self.loop()

        pygame.quit()
        sys.exit()
    
    def loop(self):
        time = self.clock.tick(self.FRAMES_PER_SECOND)                
        self.processEvents(pygame_sdl2.event.get())
        self.world.Step(1.0/self.FRAMES_PER_SECOND, 6, 2)
        self.update()
        self.renderer.gameWillRender()
        self.render()
        self.world.DrawDebugData()
        self.renderer.gameDidRender()

    def processEvents(self, events):
        for event in events:
            if event.type == QUIT:
                self.running = False

    def update(self):
        for obj in self.gameObjects:
            obj.update()


    def render(self):
        for obj in self.gameObjects:
            obj.render(self.renderer)

    def createObject(self, physics=None, renderable=None):
        gameObject = GameObject(game=self, physics=physics, renderable=renderable)
        
        self.gameObjects.append(gameObject)
        return gameObject
