import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        self.screen = screen
        pygame.draw.polygon(
            screen,
            "white",
            self.triangle(),
            2
        )
                

    def update(self, dt):
        # sub-classes must override
        pass
    
    def is_colliding(self, other):
        # check if two circles are colliding
        return self.position.distance_to(other.position) <= self.radius + other.radius