import pygame
class Ball:
    RADIUS = 10

    def __init__(self,x,y,vx,vy,screen,fgcolor,bgcolor, CONST_BORDER):
        self.x = x
        self.y = y
        self.screen = screen
        self.vx = vx
        self.vy = vy
        self.fgcolor = fgcolor
        self.bgcolor = bgcolor
        self.CONST_BORDER = CONST_BORDER

    def show(self,color):
        pygame.draw.circle(self.screen,color,(self.x,self.y),self.RADIUS)

    def update(self):
        w, h = self.screen.get_size()
        if self.x+self.vx < (self.CONST_BORDER + self.RADIUS) or self.x > w :
            self.vx = -self.vx 
        if self.y +self.vy < (self.CONST_BORDER + self.RADIUS) or self.y > (h-(self.CONST_BORDER + self.RADIUS)):
            self.vy = -self.vy 
        self.show(self.bgcolor)
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        self.show(self.fgcolor)
