from pygame import *
from Boy import *
from Girl import *
from BoyAI import *
from GirlAI import *
import pygame
import sys
import random

class Window:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.screen = pygame.display.set_mode((self.w, self.h))

    def fill(self):
        self.screen.fill((200, 222, 255))

class ProximityGame:
    def __init__(self):
        pygame.font.init()
        self.background = image.load("Assets/background.png")
        self.background = pygame.transform.scale(self.background, (screen.w, screen.h))
        self.myfont = pygame.font.SysFont('Comic Sans MS', 30)
        self.p = Boy(100, 700, [[0 for x in range(3)] for y in range(4)], screen.screen)
        self.otherP = []
        for i in range(7):
            self.otherP.append(BoyAI(4 * random.randrange(screen.w//4), 4 * random.randrange(75, screen.h//4), [[0 for x in range(3)] for y in range(4)],
                                 4 * random.randrange(screen.w//4), 4 * random.randrange(75, screen.h//4),4 * random.randrange(screen.w//4), 4 * random.randrange(75, screen.h//4)))
            self.otherP.append(BoyAI(0, 500, [[0 for x in range(3)] for y in range(4)], screen.w, 500, 0, 500))

    def checkCollision(self, p1, p2):
        if p1.x_pos > p2.x_pos and p1.x_pos < p2.x_pos + 72 and p1.y_pos > p2.y_pos and p1.y_pos < p2.y_pos + 72:
            p1.x_pos = 100
            p1.y_pos = 700
        elif p2.x_pos > p1.x_pos and p2.x_pos < p1.x_pos + 72 and p2.y_pos > p1.y_pos and p2.y_pos < p1.y_pos + 72:
            p1.x_pos = 100
            p1.y_pos = 700

    def update(self):
        # print(self.p)
        self.p.update()

    def draw(self):

        screen.screen.blit(self.background,(0,0,screen.w,screen.h))
        self.p.moveBoy()
        self.p.drawBoy()

        pygame.draw.rect(screen.screen, (255, 0, 0), (screen.w - 100, screen.h - 100, 100, 100))
        text1 = self.myfont.render('Finish', False, (0, 0, 0))
        text2 = self.myfont.render('Line', False, (0, 0, 0))
        screen.screen.blit(text1, (screen.w - 75, screen.h - 75))
        screen.screen.blit(text2, (screen.w - 75, screen.h - 50))
        if self.p.x_pos > screen.w - 100 and self.p.x_pos < screen.w and self.p.y_pos > screen.h - 100 and self.p.y_pos < screen.h:
            print("Collision")

        for other in self.otherP:
            self.checkCollision(self.p, other)
            other.drawBoyAI()
            if other.moveBoy(other.targetX, other.targetY) == "Turn":
                if other.targetX == other.endX and other.targetY == other.endY:
                    other.targetX = other.startX
                    other.targetY = other.startY
                else:
                    other.targetX = other.endX
                    other.targetY = other.endY

screen = Window(800, 800)
pygame.init()
clock = pygame.time.Clock()
g = ProximityGame()

while True:

    g.update()
    screen.fill()
    g.draw()


    # Check inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()
    clock.tick(70)  # Fps (Don't know why/how it does it)
