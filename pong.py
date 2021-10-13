import pygame
def main():
    pygame.init()
    WIDTH = 800
    HEIGHT = 480
    pygame.display.set_caption('Lab2')
    surface = pygame.display.set_mode((WIDTH,HEIGHT))

    #WALLS
    color = pygame.Color('purple')
    BORDER = 30
    pygame.draw.rect(surface, color, pygame.Rect(0, 0, BORDER, HEIGHT))
    pygame.draw.rect(surface, color, pygame.Rect(0, HEIGHT-BORDER, WIDTH, BORDER))
    pygame.draw.rect(surface, color, pygame.Rect(0, 0, WIDTH, BORDER))

    pygame.display.update()


    # define a variable to control the main loop
    running = True
        
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

if __name__ == "__main__":
    main()