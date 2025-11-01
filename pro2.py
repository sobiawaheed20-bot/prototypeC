import pygame
pygame.init()

WIDTH=500
HEIGHT=500

screen=pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill("grey")

class rectangle5000000():
    def __init__(self,width,height,x,y,color):
        self.color=color
        self.height=height
        self.x=x
        self.y=y
        self.width=width
        self.surf=screen
    def brh(self):
        pygame.draw.rect(self.surf,self.color,(self.x,self.y,self.width,self.height))
    def grow(self):
       self.width=self.width+5
       self.height=self.height+5
       pygame.draw.rect(self.surf,self.color,(self.x,self.y,self.width,self.height))
    def mleft(self):
       self.x=self.x-2.5
       self.pos=(self.x,self.y)
       pygame.draw.rect(self.surf,self.color,(self.x,self.y,self.width,self.height))
    def mright(self):
       self.x=self.x+2.5
       self.pos=(self.x,self.y)
       pygame.draw.rect(self.surf,self.color,(self.x,self.y,self.width,self.height))
    def mup(self):
       self.y=self.y-2.5
       self.pos=(self.x,self.y)
       pygame.draw.rect(self.surf,self.color,(self.x,self.y,self.width,self.height))
    def mdown(self):
        self.y=self.y+2.5
        self.pos=(self.x,self.y)
        pygame.draw.rect(self.surf,self.color,(self.x,self.y,self.width,self.height))


c1=rectangle5000000(50,60,250,250,"black")


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