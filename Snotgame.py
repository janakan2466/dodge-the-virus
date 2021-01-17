from pygame import *
from Boy import *
from Girl import *
from BoyAI import *
from GirlAI import *

screen = display.set_mode((1000,300))
font.init()

# --- Loading Assets ----------------
background = image.load("Assets/hallway.jpg")
titleFont = font.SysFont("Comic Sans MS", 60)
buttonFont = font.SysFont("Comic Sans MS", 20)
# -----------------------------------
def introScreen():
    screen.blit(background, (-5,0))
    titleText = "Move away from the sneezes!"
    buttonText = "Use the arrow keys to get to the classroom!"
    
    title = titleFont.render(titleText, True, (0,0,0))
    button = buttonFont.render(buttonText, True, (0,0,0))

    screen.blit(title, (100,10))
    screen.blit(button, (300, 300))
    
    display.flip()

running = True
myClock = time.Clock()

boy = Boy(300,300, [[0 for x in range(3)] for y in range(4)], screen)

while running:
    for evnt in event.get():
        if evnt.type == QUIT:
            running = False

    introScreen()
    
    boy.moveBoy(boy)
    boy.drawBoy()
    boy.update()

    myClock.tick(50)
    

quit()
