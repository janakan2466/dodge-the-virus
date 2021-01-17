from pygame import *
import pygame
import random
import sys

screen = display.set_mode((950, 800))
font.init()


hand = image.load("Assets/hand.png")
handX, handY = 100, 500
hand = pygame.transform.scale(hand, (800, 200))
tap = image.load("Assets/waterTap.png")
bathroom = image.load("Assets/background.png")
germs = [pygame.transform.scale(image.load("Assets/germs.png"), (40, 40)) for i in range(10)]
germPos = [[random.randrange(200, 650), random.randrange(35, 65)] for i in range(10)]

def introScreen(tapX):
    screen.blit(bathroom, (0, 0))

    screen.blit(tap, (tapX - 1270, 25))
    screen.blit(hand, (handX, handY))

    display.flip()

pygame.init()
running = True
germKilled = True
killCount = 0
initialTimer = 300
timer = initialTimer
clock = time.Clock()

x = 0

class Window:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.screen = pygame.display.set_mode((self.w, self.h))

    def fill(self):
        self.screen.fill((255, 255, 255))

class Germ:
    def __init__(self):
        self.x = random.randrange(950)
        self.y = random.randrange(400, 750)
        self.image = image.load("Assets/germs.png")\

screen = Window(700, 525)
pygame.init()
clock = pygame.time.Clock()

while True:
    screen.fill()
    pygame.draw.rect(screen.screen, (25, 50, 200), (300, 200, 75, 500))
    screen.screen.blit(tap, (50, 10))

    mousePos = pygame.mouse.get_pos()
    screen.screen.blit(hand, (mousePos[0] - 500, mousePos[1]))

    for i in range(len(germs) -1, -1, -1):
        if germs[i] != "NA":
            germ = germs[i]
            x, y = germPos[i]
            mousePos = pygame.mouse.get_pos()
            screen.screen.blit(germ, (x + mousePos[0] - 500,y + mousePos[1]))
            x += mousePos[0] - 500
            y += mousePos[1]
            if 300 < x and x < 375:
                germs[i] = "NA"
                continue

    flag = True
    for i in range(len(germs)):
        if germs[i] != "NA": flag = False

    if flag: break

    for evnt in event.get():
        if evnt.type == QUIT:
            running = False
            sys.exit()

    pygame.display.update()
    clock.tick(70)  # Fps (Don't know why/how it does it)