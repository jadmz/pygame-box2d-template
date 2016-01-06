

class GameObject:
    
    def __init__(self, game, physics=None, renderable=None):
        self.game = game
        self.physics = physics
        self.renderable = renderable

    def update(self):
        print(self.getGamePosition())

    def render(self, renderer):
        pass

    def getGamePosition(self):
        position = self.physics.body.position
        position.y *= -1
        return (position.x, position.y)

    def setGamePosition(self, x, y):
        self.physics.body.position.x = x
        self.physics.body.position.y = y * -1
