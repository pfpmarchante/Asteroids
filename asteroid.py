from circleshape import CircleShape
from constants import *
import pygame, random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        self.screen = screen
        pygame.draw.circle(
            screen,
            "white",
            (self.position.x, self.position.y),
            self.radius,
            2
        )
        
    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        split_angle = random.uniform(20, 50)  
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        vector_1 = self.velocity.rotate(split_angle)   
        vector_2 = self.velocity.rotate(-split_angle)

        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = vector_1

        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = vector_2
        
        
    
        
        