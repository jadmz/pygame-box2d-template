from Box2D import (b2BodyDef, b2PolygonShape)

class Ground:
    
    def __init__(self, world):
        self.groundBody = world.CreateStaticBody(
            position=(0,-10),
            shapes=b2PolygonShape(box=(50,10)),
            )

        self.dynamicBody = world.CreateDynamicBody(position=(0,4))
        box = self.dynamicBody.CreatePolygonFixture(box=(1,1), density=1, friction=0.3)
