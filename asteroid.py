import circleshape
from constants import *
import pygame
from logger import log_event
import random

class Asteroid(circleshape.CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)

    def update(self,dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20,50)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        new_1_rot = self.velocity.rotate(angle)
        new_2_rot = self.velocity.rotate(-angle)

        new_ast_1 = Asteroid(self.position[0],self.position[1],new_radius)
        new_ast_1.velocity = new_1_rot * 1.2

        new_ast_2 = Asteroid(self.position[0],self.position[1],new_radius)
        new_ast_2.velocity = new_2_rot * 1.2
              
    