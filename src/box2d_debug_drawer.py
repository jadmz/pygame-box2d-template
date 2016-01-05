
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

        self.flags = dict(drawShapes=True,
                          drawJoints=True,
                          drawAABBs=True,
                          drawPairs=True,
                          drawCOMs=True,
                          convertVertices=True,
                          )


    def DrawPoint(self, p, size, color):
        print("Draw point")
    
    def DrawAABB(self, aabb, color):
        print("Draw aabb")

    def DrawSegment(self, p1, p2, color):
        print("Draw segment")

    def DrawTransform(self, xf):
        print("Draw Transform")
    
    def DrawCircle(self, center, radius, color, drawwidth=1):
        print("Draw Circle")

    def DrawSolidCircle(self, center, radius, axis, color):
        print("Draw Solid Circle")

    def DrawPolygon(self, verticies, color):
        print("Draw Polygon")

    def DrawSolidPolygon(self, verticies, color):
        print("Draw Solid Polygon")

