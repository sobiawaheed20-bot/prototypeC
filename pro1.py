import pygame
pygame.init()

WIDTH=500
HEIGHT=500

screen=pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill("grey")

class CIrcle():
    def __init__(self,color,x,y,r):
     self.color=color
     self.x=x
     self.y=y
     self.r=r
     self.surf=screen
     self.pos=(self.x,self.y)
    def brh(self):
     pygame.draw.circle(self.surf,self.color,self.pos,self.r)
    def grow(self):
       self.r=self.r+5
       pygame.draw.circle(self.surf,self.color,self.pos,self.r)
    def mleft(self):
       self.x=self.x-2.5
       self.pos=(self.x,self.y)
       pygame.draw.circle(self.surf,self.color,self.pos,self.r)
    def mright(self):
       self.x=self.x+2.5
       self.pos=(self.x,self.y)
       pygame.draw.circle(self.surf,self.color,self.pos,self.r)
    def mup(self):
       self.y=self.y-2.5
       self.pos=(self.x,self.y)
       pygame.draw.circle(self.surf,self.color,self.pos,self.r)
    def mdown(self):
        self.y=self.y+2.5
        self.pos=(self.x,self.y)
        pygame.draw.circle(self.surf,self.color,self.pos,self.r)


c1=CIrcle("black",250,250,70)


while True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.QUIT()
        if event.type==pygame.MOUSEBUTTONDOWN:
           c1.brh()
        if event.type==pygame.MOUSEBUTTONUP:
           c1.grow()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                screen.fill("grey")
                c1.mleft()
            if event.key==pygame.K_RIGHT:
               screen.fill("grey")
               c1.mright()
            if event.key==pygame.K_UP:
               screen.fill("grey")
               c1.mup()
            if event.key==pygame.K_DOWN:
               screen.fill("grey")
               c1.mdown()

    pygame.display.update()