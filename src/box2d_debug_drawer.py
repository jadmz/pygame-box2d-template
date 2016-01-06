
from Box2D import (b2DrawExtended, b2Vec2)

class Box2dDebugDrawer(b2DrawExtended):
    """
    This debug renderer implements the callback interface for Box2d to render debug information.
    This is heavily (very heavily) based off of pyBox2d pygame draw class found here:
    https://github.com/pybox2d/pybox2d/blob/master/examples/backends/pygame_framework.py
    """

    def __init__(self, renderer, zoom, offset, **kwargs):
        b2DrawExtended.__init__(self, **kwargs)

        # The renderer to use
        self.renderer = renderer
        
        self.flipX = False
        self.flipY = True
        self.convertVerticies = True
        self.offset = offset
        self.zoom = zoom

        self.flags = dict(drawShapes=True,
                          drawJoints=True,
                          drawAABBs=True,
                          drawPairs=True,
                          drawCOMs=True,
                          convertVertices=True,
                          )


    def DrawPoint(self, p, size, color):
        self.DrawCircle(p, size, color)
    
    def DrawAABB(self, aabb, color):
        points = [(aabb.lowerBound.x, aabb.lowerBound.y),
                  (aabb.upperBound.x, aabb.lowerBound.y),
                  (aabb.upperBound.x, aabb.upperBound.y),
                  (aabb.lowerBound.x, aabb.upperBound.y)]

        self.renderer.drawLines(points, color, False)
    def DrawSegment(self, p1, p2, color):
        self.renderer.drawLine(p1, p2, color.bytes, False)

    def DrawTransform(self, xf):
        p1 = xf.position
        p2 = self.to_screen(p1 + 1 * xf.R.x_axis)
        p3 = self.to_screen(p1 + 1 * xf.R.y_axis)
        p1 = self.to_screen(p1)

        self.renderer.drawLine(p1, p2, (255, 0, 0), False)
        self.renderer.drawLine(p1, p3, (0, 255, 0), False)
    
    def DrawCircle(self, center, radius, color, drawwidth=1):
        radius *= self.zoom
        self.renderer.drawCircle(center, radius, color.bytes, False)

    def DrawSolidCircle(self, center, radius, axis, color):
        self.renderer.drawFilledCircle(center, radius, color, False)
        self.renderer.drawLine(center,
                               (center[0] - radius * axis[0],
                                center[1] + radius * axis[1]),
                                (255, 0, 0), False)

    def DrawPolygon(self, vertices, color):
        if not vertices:
            return
        if len(vertices) == 2:
            self.DrawSegment(vertices[0], vertices[1], color)
        else:
            self.renderer.drawPolygon(vertices, color.bytes, False)

    def DrawSolidPolygon(self, vertices, color):
        if not vertices:
            return
        if len(vertices) == 2:
            self.DrawSegment(vertices[0], vertices[1], color)
        else:
            self.renderer.drawFilledPolygon(vertices, color.bytes, False)

