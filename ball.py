# -*- coding: utf-8 -*-
"""
Created on Wed May 20 13:09:18 2020

@author: Ashish T Vasant
"""


import pygame
# from random import 
import random

BLACK = (0, 0, 0)
RED = (255,0,0)
 
class Ball(pygame.sprite.Sprite):
    #This class represents a car. It derives from the "Sprite" class in Pygame.
    
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(RED)
        self.image.set_colorkey(RED)
 
        # Draw the ball (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        #pygame.draw.circle(self.image, color, (50, 50), 15)
        self.velocity = [-2,-2]
        
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_bounding_rect()
        
    def update(self):
        self.rect.x += self.velocity[0]#*randint(7,11)/10)
        self.rect.y += self.velocity[1]#*randint(7,11)/10)
        
    def bounce(self):
        #randommodulus=random.randrange(10,11)
        randommodulus=10
        self.velocity[0] = (self.velocity[0])*randommodulus/10#+randint(-1,1)
        self.velocity[1] = (-self.velocity[1])*randommodulus/10#randint(0,1)#randint(-8,8)
