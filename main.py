import pygame 
from constants import *
from player import Player
from circleshape import CircleShape 
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot 


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    
    
    
    clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    
    
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            
        updatable.update(dt)
        
        for asteroid in asteroids:
            if asteroid.is_colliding(player):
                print("Game Over!")
                pygame.quit()
                exit()
        
        screen.fill((0, 0, 0))
        
        for sprite in drawable:
            sprite.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000.0
        
        

   
    
    
    
    





if __name__ == "__main__":
    main()