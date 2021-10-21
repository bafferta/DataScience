import pygame
from ball import Ball
import random 
import numpy as np 

def main():
    pygame.init()
    WIDTH = 800
    HEIGHT = 480
    VELOCITY = 5
    FPS = 30
    pygame.display.set_caption('Lab2')
    surface = pygame.display.set_mode((WIDTH,HEIGHT))

    #WALLS
    color = pygame.Color('purple')
    bgcolor = pygame.Color('black')
    BORDER = 30
    pygame.draw.rect(surface, color, pygame.Rect(0, 0, BORDER, HEIGHT))
    pygame.draw.rect(surface, color, pygame.Rect(0, HEIGHT-BORDER, WIDTH, BORDER))
    pygame.draw.rect(surface, color, pygame.Rect(0, 0, WIDTH, BORDER))

    #ball init
    x0 = WIDTH - Ball.RADIUS
    y0 = HEIGHT//2 
    angle = random.randrange(-45,45)
    vx0 = -VELOCITY * np.abs(np.cos(angle))
    vy0 = VELOCITY * np.abs(np.sin(angle))
    b0 = Ball(x0,y0,vx0,vy0,surface,color,bgcolor,BORDER)

    b0.show(color)
    pygame.display.update()


    # define a variable to control the main loop
    running = True
    clock = pygame.time.Clock()
        
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            pygame.display.update()
            clock.tick(FPS)
            b0.update()

if __name__ == "__main__":
    main()