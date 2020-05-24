# -*- coding: utf-8 -*-
"""
Created on Sat May 23 11:15:11 2020

@author: Ashish T Vasant
"""
# Import the pygame library and initialise the game engine
import pygame, pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *
import pygame
#Let's import the Paddle Class & the Ball Class
from paddle import Paddle
from ball import Ball
from  brick import Brick
from random import randint
import sys
pygame.init()
 
# Define some colors
WHITE = (255,255,255)
DARKBLUE = (36,90,190)
LIGHTBLUE = (0,176,240)
RED = (255,0,0)
ORANGE = (255,100,0)
YELLOW = (255,255,0)
BLACK = (0,0,0) 
GREY = (210, 210, 210)
ANOTHERGREY=(122,122,122)
score = 0
lives = 15
current_string=''
# Open a new window
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout Game")

#This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()
input_text=" This is just some random lines of text which is meant to simulate the different types of letters you might actually need to type"
bigtext=input_text

paddles=[] 
#Create the ball sprite
ball = Ball(BLACK,20,20)
ball.rect.x = 345
ball.rect.y = 195

#THE BRICKS
all_bricks = pygame.sprite.Group()
for i in range(7):
    brick = Brick(RED,80,30)
    brick.rect.x = 60 + i* 100
    brick.rect.y = 60
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(7):
    brick = Brick(ORANGE,80,30)
    brick.rect.x = 60 + i* 100
    brick.rect.y = 100
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(7):
    brick = Brick(YELLOW,80,30)
    brick.rect.x = 60 + i* 100
    brick.rect.y = 140
    all_sprites_list.add(brick)
    all_bricks.add(brick)
 
# Add the paddle to the list of sprites
# all_sprites_list.add(paddle)
all_sprites_list.add(ball)
all_paddles_list=pygame.sprite.Group()
# The loop will carry on until the user exit the game (e.g. clicks the close button).
carryOn = True
 
# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()


###############special font function#####################
def create_font(t,s=52,c=(255,255,0), b=True,i=False):
    font = pygame.font.SysFont("Courier", s, bold=b, italic=i)
    text = font.render(t, True, c)
    return text

###############getting the big text################################
f=open('file.txt')
lines=f.readlines()
index=0

###########################################
# -------- Main Program Loop -----------

while carryOn:

    
    ####################capturing events###############################
    events= pygame.event.get()
    keys = pygame.key.get_pressed()
    for event in events:
        if event.type == pygame.QUIT:
             pygame.quit(); sys.exit()
             carryOn = False 
           
        elif event.type == pygame.KEYDOWN:

            inkey=event.key
            if inkey == K_BACKSPACE:
                 current_string = current_string[0:-1]
            
            elif keys[pygame.K_LEFT]:
                 paddle.moveLeft(5)
            elif keys[pygame.K_RIGHT]:
                paddle.moveRight(5)
            elif inkey == K_RETURN:
                 #######SOMETHING HAPPENS HERE###########################
                 
                 

                 paddles=[]
                 # current_string=" "+current_string+" "
                 s=current_string.split()
                 for i in s:
                    i=" "+i+" "

                    pos= bigtext.find(i)
                    length=len(i)
                    if pos !=-1:
                        paddles.append((pos,length))
                        print(paddles)
                 ########################################
                 current_string=""
                 ########################################
            elif inkey == K_MINUS:
                 current_string.append("_")
            else:
                current_string+=((event.unicode))
    #            print(current_string)
    ######################################################
        
        

        #####################here i have a group containing paddles#########################
       #Create the Paddles from the list
           # paddles=[(150,200),(150,600)]#width and position
            for p in paddles:
                paddle = Paddle(ANOTHERGREY, ((p[1])*31.5), 19)#width##################
                paddle.rect.x = 31.5*(p[0])#+(p[1]/2)
                paddle.rect.y = 520
                
                all_paddles_list.add(paddle)
                

    
    ###########################################################            
        
     
    # --- Game logic should go here
    all_sprites_list.update()
    all_paddles_list.update()
     
    #Check if the ball is bouncing against any of the 4 walls:
    if ball.rect.x>=790:
        ball.velocity[0] = -ball.velocity[0]#*randint(9,10)/10
    if ball.rect.x<=0:
        ball.velocity[0] = -ball.velocity[0]#*randint(9,10)/10
    if ball.rect.y>599:
        ########################game over or life reduction code################
        lives=lives-1
        if lives==0:
           #Display Level Complete Message for 3 seconds
            font = pygame.font.Font(None, 74)
            text = font.render("LEVEL FAILED", 1, RED)
            screen.blit(text, (200,300))
            pygame.display.flip()
            pygame.time.wait(3000)
     
            #Stop the Game
            carryOn=False
        
        
        ball.velocity[1] = -ball.velocity[1]#*randint(9,10)/10
    if ball.rect.y<40:
        ball.velocity[1] = -ball.velocity[1]#*randint(9,10)/10
        
    #Check if there is a car collision
    brick_collision_list = pygame.sprite.spritecollide(ball,all_bricks,False)
    for brick in brick_collision_list:
      ball.bounce()
      score += 1
      brick.kill()
      if len(all_bricks)==0:
           #Display Level Complete Message for 3 seconds
            font = pygame.font.Font(None, 74)
            text = font.render("LEVEL COMPLETE", 1, RED)
            screen.blit(text, (200,300))
            pygame.display.flip()
            pygame.time.wait(3000)
     
            #Stop the Game
            carryOn=False
     
    #Detect collisions between the ball and the paddles
    paddle_collision_list = pygame.sprite.spritecollide(ball, all_paddles_list,False)
    if paddle_collision_list:
        try :
            index+=1
            bigtext=lines[index]
            bigtext=" "+bigtext+" "
        except: 
            index=0
            bigtext=lines[index]
            bigtext=" "+bigtext+" "
    for pd in paddle_collision_list:
        
        ball.rect.x -= ball.velocity[0]
        ball.rect.y -= ball.velocity[1]
        ball.bounce()

        print("bounce")
        all_paddles_list=pygame.sprite.Group()
        paddles=[]

     
    # --- Drawing code should go here
    # First, clear the screen to dark blue.
    screen.fill(GREY)
    pygame.draw.line(screen, BLACK, [0, 38], [800, 38], 2)
     
    #Display the score and the number of lives at the top of the screen
    font = pygame.font.Font(None, 34)
    text = font.render("Score: " + str(score), 1, BLACK)
    screen.blit(text, (20,10))
    text = font.render("Lives: " + str(lives), 1, BLACK)
    screen.blit(text, (650,10))
    ###########displaying the text################
    
    
 
    modified_string="Input text:"+current_string
    font = pygame.font.Font(None, 30)
    text = font.render(modified_string, 1, BLACK)
    screen.blit(text, (20,300)) 
    
    
    ##############################################################
    #input_text=returned by the function that reads from the file


    text = create_font(bigtext)
    screen.blit(text, (0,530)) 
    
    

    
    
    #####################################
    #Display the rest of the things
    clock.tick(1000)
 
    #Now let's draw all the sprites in one go.
    all_sprites_list.draw(screen)
    all_paddles_list.draw(screen)
    
     
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
     

#Once we have exited the main program loop we can stop the game engine:
pygame.quit()
