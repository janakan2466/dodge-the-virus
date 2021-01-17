from pygame import *
from Boy import *
from Girl import *
from BoyAI import *
from GirlAI import *
from proximityGame import *
import random

screen = display.set_mode((800,800))

font.init()

# --- Loading Assets ----------------
background = image.load("Assets/background.png")
classroom = image.load("Assets/classroom.png")

titleFont = font.SysFont("Comic Sans MS", 60)
buttonFont = font.SysFont("Comic Sans MS", 48)
classroomFont = font.SysFont("Comic Sans MS", 48)
warningFont = font.SysFont("Comic Sans MS", 32)

sitting_1 = image.load("Assets/Sitting/sitting0.png")
sitting_2 = image.load("Assets/Sitting/sitting1.png")
sitting_3 = image.load("Assets/Sitting/sitting2.png")
sitting_4 = image.load("Assets/Sitting/sitting3.png")

sitting_1_hitbox = Rect(135,650,70,70)
sitting_2_hitbox = Rect(505,525,70,70)
sitting_3_hitbox = Rect(135,418,70,70)
sitting_4_hitbox = Rect(505,320,70,70)
sitting_5_hitbox = Rect(220,320,70,70)
# -----Buttons-------------------
buttonText = "Click here to start!"
button = buttonFont.render(buttonText, True, (255,255,255))

buttonRect = Rect(250, 700, 295, 30)
draw.rect(screen, (255,0,0), buttonRect, 4)
screen.blit(button, (250, 700))

# ----Collisions Rects on the edges--------------------
rect1 = Rect(0,0,800,110) # upper rect
rect2 = Rect(0,0,100,800) # left rect
rect3 = Rect(700,0,105,800) # right rect
rect4 = Rect(0,740,800,60) # bottom rect

# ----Collisions Rects for the Tables------------------
tableRect1 = Rect(115, 600, 196, 30)
tableRect2 = Rect(115, 490, 196, 30)
tableRect3 = Rect(115, 385, 196, 30)
tableRect4 = Rect(115, 280, 196, 30)

tableRect5 = Rect(485, 600, 196, 30)
tableRect6 = Rect(485, 490, 196, 30)
tableRect7 = Rect(485, 385, 196, 30)
tableRect8 = Rect(485, 280, 196, 30)
# -----------------------------------------------------
def titleScreen():
    screen.blit(background, (-5,0))
    titleText = "A Day at School during COVID-19"
    
    title = titleFont.render(titleText, True, (0,0,0))
    screen.blit(title, (190,200))
        
    buttonRect = Rect(250, 700, 295, 30)
    draw.rect(screen, (255,0,0), buttonRect, 4)
    screen.blit(button, (250, 700))
# -----------------------------------------------------

running = True
myClock = time.Clock()

boy = Boy(570,700, [[0 for x in range(3)] for y in range(4)], screen)
warning = False

titleScreen = True

while running:
    for evnt in event.get():
        if evnt.type == QUIT:
            running = False

        if evnt.type == MOUSEBUTTONDOWN:
            if buttonRect.collidepoint(mouse.get_pos()):
                titleScreen = False

    if titleScreen:
        screen.blit(background, (-5,0))
        titleText = "A Day at School during COVID-19"
        
        title = titleFont.render(titleText, True, (0,0,0))
        screen.blit(title, (80,200))
            
        buttonRect = Rect(250, 700, 295, 30)
        #draw.rect(screen, (255,0,0), buttonRect, 4)
        screen.blit(button, (250, 700))

    else: 

    # CLASSROOM GAME ----------------------------------------------------

        classroomTitle = "Sit in the right spot, away from other students!"
        warningTitle = "Incorrect! Sit further away to social distance."
        
        classroomText = classroomFont.render(classroomTitle, True, (255,255,255))
        warningText = warningFont.render(warningTitle, True, (255,255,255))

        # background image
        screen.blit(classroom, (0,0))

        # top text of the instructions
        screen.blit(classroomText, (20,5))

        # images of all the children
        screen.blit(sitting_1, (135, 650))
        screen.blit(sitting_2, (505, 525))
        screen.blit(sitting_3, (135, 418))

        # Collision with upper Rectangles --------------------
        if (boy.hitbox.colliderect(rect1)):
            boy.y_pos += 5
        if (boy.hitbox.colliderect(rect2)):
            boy.x_pos += 5
        if (boy.hitbox.colliderect(rect3)):
            boy.x_pos -= 5
        if (boy.hitbox.colliderect(rect4)):
            boy.y_pos -= 5
            
        # Collision with tables ------------------------------
        if (boy.hitbox_top.colliderect(tableRect1)):
            boy.y_pos += 5
        if (boy.hitbox_top.colliderect(tableRect2)):
            boy.y_pos += 5
        if (boy.hitbox_top.colliderect(tableRect3)):
            boy.y_pos += 5
        if (boy.hitbox_top.colliderect(tableRect4)):
            boy.y_pos += 5
        if (boy.hitbox_top.colliderect(tableRect5)):
            boy.y_pos += 5
        if (boy.hitbox_top.colliderect(tableRect6)):
            boy.y_pos += 5
        if (boy.hitbox_top.colliderect(tableRect7)):
            boy.y_pos += 5
        if (boy.hitbox_top.colliderect(tableRect8)):
            boy.y_pos += 5

        if (boy.hitbox_left.colliderect(tableRect1)):
            boy.x_pos +=5
        if (boy.hitbox_left.colliderect(tableRect2)):
            boy.x_pos +=5
        if (boy.hitbox_left.colliderect(tableRect3)):
            boy.x_pos +=5
        if (boy.hitbox_left.colliderect(tableRect4)):
            boy.x_pos +=5

        if (boy.hitbox_right.colliderect(tableRect5)):
            boy.x_pos -=5
        if (boy.hitbox_right.colliderect(tableRect6)):
            boy.x_pos -=5
        if (boy.hitbox_right.colliderect(tableRect7)):
            boy.x_pos -=5
        if (boy.hitbox_right.colliderect(tableRect8)):
            boy.x_pos -=5

        if (boy.hitbox_bottom.colliderect(tableRect1)):
            boy.y_pos -= 5
        if (boy.hitbox_bottom.colliderect(tableRect2)):
            boy.y_pos -= 5
        if (boy.hitbox_bottom.colliderect(tableRect3)):
            boy.y_pos -= 5
        if (boy.hitbox_bottom.colliderect(tableRect4)):
            boy.y_pos -= 5
        if (boy.hitbox_bottom.colliderect(tableRect5)):
            boy.y_pos -= 5
        if (boy.hitbox_bottom.colliderect(tableRect6)):
            boy.y_pos -= 5
        if (boy.hitbox_bottom.colliderect(tableRect7)):
            boy.y_pos -= 5
        if (boy.hitbox_bottom.colliderect(tableRect8)):
            boy.y_pos -= 5

        # ----------------------------------------------------
        if warning:
            screen.blit(warningText, (40, 765)) 

        # if you collide with the other children, sends you back to the start of the room
        if (boy.hitbox.colliderect(sitting_1_hitbox) or boy.hitbox.colliderect(sitting_2_hitbox) or boy.hitbox.colliderect(sitting_3_hitbox)):
            boy = Boy(570,700, [[0 for x in range(3)] for y in range(4)], screen)
            warning = True   

        # goes to the next game if you collide with the correct rect
        if (boy.hitbox.colliderect(sitting_4_hitbox) or boy.hitbox.colliderect(sitting_5_hitbox)):
            break
            
        
        boy.moveBoy(boy)
        boy.drawBoy()
        boy.update()
        # -------------------------------------------------------------------

    display.flip()    
    myClock.tick(50)

g = ProximityGame()
while True:

    g.update()
    if g.draw() == "Break":
        print("end")
        break

    # Check inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()
    myClock.tick(70)  # Fps (Don't know why/how it does it)

hand = image.load("Assets/hand.png")
handX, handY = 100, 500
hand = pygame.transform.scale(hand, (800, 200))
tap = image.load("Assets/waterTap.png")
bathroom = image.load("Assets/background.png")
germs = [pygame.transform.scale(image.load("Assets/germs.png"), (40, 40)) for i in range(10)]
germPos = [[random.randrange(200, 650), random.randrange(35, 65)] for i in range(10)]

clock = pygame.time.Clock()
print("continue")
while True:
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (25, 50, 200), (300, 200, 75, 500))
    screen.blit(tap, (50, 10))

    mousePos = pygame.mouse.get_pos()
    screen.blit(hand, (mousePos[0] - 500, mousePos[1]))

    for i in range(len(germs) -1, -1, -1):
        if germs[i] != "NA":
            germ = germs[i]
            x, y = germPos[i]
            mousePos = pygame.mouse.get_pos()
            screen.blit(germ, (x + mousePos[0] - 500,y + mousePos[1]))
            x += mousePos[0] - 500
            y += mousePos[1]
            if 300 < x and x < 375:
                germs[i] = "NA"
                continue

    flag = True
    for i in range(len(germs)):
        if germs[i] != "NA": flag = False

    if flag:
        screen.fill((53,215,255))
        exitTitle1 = "Congrats! You've learned about"
        exitTitle2 = "how to keep safe from COVID-19!"
        exitScreen1 = titleFont.render(exitTitle1, True, (255,255,255))
        exitScreen2 = titleFont.render(exitTitle2, True, (255,255,255))
        screen.blit(exitScreen1, (100,255))
        screen.blit(exitScreen2, (100,300))
        

    for evnt in pygame.event.get():
        if evnt.type == QUIT:
            sys.exit()

    pygame.display.update()
    clock.tick(70)  # Fps (Don't know why/how it does it)
