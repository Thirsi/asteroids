import pygame
import sys
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from constants import *
from logger import log_state,log_event

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #pygame setup
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()
    
    dt = 0
    player1 = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

    #game loop
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for ast in asteroids:
            if ast.collides_with(player1):
                log_event("player_hit")
                print("Game Over!")
                sys,exit()
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()

        #tick
        ellapsed = clock.tick(60)
        dt = ellapsed/1000

        



if __name__ == "__main__":
    main()
