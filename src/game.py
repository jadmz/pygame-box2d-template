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

import pygame, sys
from pygame.locals import (QUIT, KEYDOWN, KEYUP, MOUSEBUTTONDOWN,
                           MOUSEBUTTONUP, MOUSEMOTION, KMOD_LSHIFT)

from renderer import Renderer

class Game:

    FRAMES_PER_SECOND = 60

    def __init__(self, title):
        pygame.init()
        pygame.display.set_caption(title)
        
        self.running = False
        self.clock = pygame.time.Clock()
        self.renderer = Renderer()


    def run(self):
        self.running = True

        while self.running:
            self.loop()

        pygame.quit()
        sys.exit()
    
    def loop(self):
        self.processEvents(pygame_sdl2.event.get())
        self.clock.tick(self.FRAMES_PER_SECOND)

    def processEvents(self, events):
        for event in events:
            if event.type == QUIT:
                self.running = False


