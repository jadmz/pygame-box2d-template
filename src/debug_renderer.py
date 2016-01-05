
from Box2D import (b2DrawExtended, b2Vec2)

class Box2dDebugDrawer(b2DrawExtended):
    """
    This debug renderer implements the callback interface for Box2d to render debug information.
    This is heavily (very heavily) based off of pyBox2d pygame draw class found here:
    https://github.com/pybox2d/pybox2d/blob/master/examples/backends/pygame_framework.py
    """

    def __init__(self, surface, **kwargs):
        b2DrawExtended.__init__(self, **kwargs)

        # The pygame surface to draw to
        self.surface = surface
        
        self.flipX = False
        self.flipY = True
        self.convertVerticies = True


    def StartDraw(self):
        pass

    def EndDraw(self):
        pass

    def DrawPoint(self, p, size, color):
        pass
    
    def DrawAABB(self, aabb, color):
        pass

    def DrawSegment(self, p1, p2, color):
        pass

    def DrawTransform(self, xf):
        pass
    
    def DrawCircle(self, center, radius, color, drawwidth=1):
        pass

    def DrawSolidCircle(self, center, radius, axis, color):
        pass

    def DrawPolygon(self, verticies, color):
        pass

    def DrawSolidPolygon(self, verticies, color):
        pass

