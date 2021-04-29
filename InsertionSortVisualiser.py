import random
import pygame
import time
from pygame.locals import *

pygame.init()

# CONSTANTS
NUMITEMS = 50
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
GREY = (125,125,125)

# SCREEN
screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])

screen.fill((125,125,125))

# MAIN LOOP

running = True
clock = pygame.time.Clock()

# CLASSES

class Bar:
    height = 0
    width = 0
    posX = 0
    posY = 0
    colour = (0,0,0)

    def __init__(self,posX,posY,width,height,colour=(0,0,0)):
        self.height = height
        self.width = width
        self.posX = posX
        self.posY = posY
        
    def Draw(self,surface):
        pygame.draw.rect(surface,self.colour,[self.posX,self.posY-self.height,self.width,self.height])

class Visualiser:
    barNum = 0
    barWidth = 0
    barMaxHeight = 0
    screenWidth = 0
    screenHeight = 0
    barGap = 0

    def __init__(self,barNum,barWidth,barMaxHeight,height=10):
        self.barNum = barNum
        self.barWidth = barWidth
        self.barMaxHeight = barMaxHeight
        self.screenWidth,self.screenHeight = pygame.display.get_surface().get_size()
        self.height = height

    def DrawBars(self,surface,bars):
        screen.fill((125,125,125))
        self.barGap = (self.screenWidth-(self.barWidth*self.barNum))/(self.barNum+1)
        currentX = self.barGap
        for bar in bars:
            bar.posX = currentX
            bar.Draw(screen)
            currentX += self.barWidth + self.barGap
            
    def CreateBars(self):
        bars = []
        count = 1
        height = self.screenHeight - self.height
        for i in range(self.barNum):
            bars.append(Bar(0,height,self.barWidth,int(self.barMaxHeight/self.barNum)*count))
            count += 1 
        return bars

def InsertionSort(bars):
    for j in range(len(bars)):
        
        while j > 0 and bars[j-1].height > bars[j].height:
            bars[j], bars[j-1] = bars[j-1], bars[j]
            j -= 1
            for bar in bars:
                if bars.index(bar) < bars.index(bars[j]) and j != 0:
                    bar.colour = GREEN
                if bars.index(bar) == j:
                    bar.colour = WHITE
            clock.tick(30)
            vis.DrawBars(screen,bars) 
            pygame.display.update()
    for bar in bars:
        bar.colour = GREEN
    vis.DrawBars(screen,bars) 
    pygame.display.update()
   
    

def BubbleSort(bars):
    length = len(bars)
    sorted = []
    for j in range(length-1):
        print(j)
        for i in range(length):
            if not i == length -1:                
                if bars[i].height > bars[i+1].height:
                    count = 0   
                    for bar in bars:
                        bar.colour = BLACK
                        if bars.index(bar) > bars.index(bars[-j]) and j != 0:
                            
                            bar.colour = GREEN
                        

                    bars[i],bars[i+1] = bars[i+1],bars[i] 
                    bars[i].colour,bars[i+1].colour = WHITE, WHITE
                    clock.tick(120)
                    
                    vis.DrawBars(screen,bars) 
                    pygame.display.update()

    for bar in bars:
        bar.colour = GREEN
    vis.DrawBars(screen,bars) 
    pygame.display.update()

vis = Visualiser(NUMITEMS,5,SCREEN_HEIGHT*0.8)
bars = vis.CreateBars()

random.shuffle(bars)
vis.DrawBars(screen,bars)

vis.DrawBars(screen,bars)



while running:
    
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            if event.key == K_F5:
                random.shuffle(bars)
                vis.DrawBars(screen,bars)
        elif event.type == QUIT:
            running = False
        InsertionSort(bars)

    
                    

        
                                 
        
        
        