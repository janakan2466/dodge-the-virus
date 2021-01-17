from pygame import *
from Boy import *
from Girl import *
from BoyAI import *
from GirlAI import *

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

boy = Boy(570,700, [[0 for x in range(3)] for y in range(4)])
warning = False

while running:
    for evnt in event.get():
        if evnt.type == QUIT:
            running = False

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

    # shows the various hitboxes
    #draw.rect(screen, (255,0,0), sitting_1_hitbox, 4)
    #draw.rect(screen, (255,0,0), sitting_2_hitbox, 4)
    #draw.rect(screen, (255,0,0), sitting_3_hitbox, 4)
    #draw.rect(screen, (255,0,0), sitting_4_hitbox, 4)
    #draw.rect(screen, (255,0,0), sitting_5_hitbox, 4)

    # Collision Rect drawings ----------------------------
    #draw.rect(screen, (255,0,0), rect1)
    #draw.rect(screen, (255,0,0), rect2)
    #draw.rect(screen, (255,0,0), rect3)
    #draw.rect(screen, (255,0,0), rect4)
    
    # Collision with upper Rectangles --------------------
    if (boy.hitbox.colliderect(rect1)):
        boy.y_pos += 5
    if (boy.hitbox.colliderect(rect2)):
        boy.x_pos += 5
    if (boy.hitbox.colliderect(rect3)):
        boy.x_pos -= 5
    if (boy.hitbox.colliderect(rect4)):
        boy.y_pos -= 5
        
    # Table Collision Drawings ---------------------------
    #draw.rect(screen, (255,0,0), tableRect1, 4)
    #draw.rect(screen, (255,0,0), tableRect2, 4)
    #draw.rect(screen, (255,0,0), tableRect3, 4)
    #draw.rect(screen, (255,0,0), tableRect4, 4)
    #draw.rect(screen, (255,0,0), tableRect5, 4)
    #draw.rect(screen, (255,0,0), tableRect6, 4)
    #draw.rect(screen, (255,0,0), tableRect7, 4)
    #draw.rect(screen, (255,0,0), tableRect8, 4)
    
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
        boy = Boy(570,700, [[0 for x in range(3)] for y in range(4)])
        warning = True   

    # goes to the next game if you collide with the correct rect
    if (boy.hitbox.colliderect(sitting_4_hitbox) or boy.hitbox.colliderect(sitting_5_hitbox)):
        print("done")
        
    
    boy.moveBoy(boy)
    boy.drawBoy()
    boy.update()
    # -------------------------------------------------------------------
    display.flip()
    
    myClock.tick(50)
    
quit()
