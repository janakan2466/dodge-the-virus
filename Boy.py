from pygame import *

screen = display.set_mode((800,800))

class Boy:

    def __init__(self, x_pos, y_pos, pics, screen):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.pics = pics #2d list
        self.hitbox = Rect(x_pos - 35, y_pos - 35, 70, 70)
        self.screen = screen

        self.hitbox_top = Rect(x_pos - 35, y_pos - 35, 70, 35)
        self.hitbox_bottom = Rect(x_pos - 35, y_pos, 70, 35)
        self.hitbox_left = Rect(x_pos - 35, y_pos - 35, 35, 70)
        self.hitbox_right = Rect(x_pos, y_pos - 35, 35, 70)

        right = []
        down = []
        up = []
        left = []
        
        for i in range(3):
            right.append(image.load("Boy_Character/right/right" + str(i) + ".png"))
        for i in range(3):
            down.append(image.load("Boy_Character/down/down" + str(i) + ".png"))
        for i in range(3):
            up.append(image.load("Boy_Character/up/up" + str(i) + ".png"))
        for i in range(3):
            left.append(image.load("Boy_Character/left/left" + str(i) + ".png"))

        pics[0] = right
        pics[1] = down
        pics[2] = up
        pics[3] = left
        
        self.move = 1
        self.frame = 0

    def moveBoy(self, boy):
        keys = key.get_pressed()
        newMove = -1
        
        if keys[K_RIGHT]:
            newMove = 0
            self.x_pos += 4.25
        elif keys[K_DOWN]:
            newMove = 1
            self.y_pos += 4.25
        elif keys[K_UP]:
            newMove = 2
            self.y_pos -= 4.25
        elif keys[K_LEFT]:
            newMove = 3
            self.x_pos -= 4.25
        else:
            self.frame = 0

        self.x_pos = min(max(35, self.x_pos), 800 - 35)
        self.y_pos = min(max(35, self.y_pos), 800 - 35)

        move = self.move
            
        if move == newMove:     # 0 is a standing pose, so we want to skip over it when we are moving
            self.frame = self.frame + 0.4 
            if self.frame >= len(self.pics[self.move]):
                self.frame = 1
        elif newMove != -1:     # a move was selected
            self.move = newMove      # make that our current move
            self.frame = 1

    def makeMove(self, name,start,end):
        move = []
        for i in range(start,end+1):
            move.append(image.load("%s/%s%d.png" % (name,name,i)))
            
        return move

    def drawBoy(self):
        move = self.move
        frame = self.frame
        pics = self.pics
        
        pic = pics[move][int(frame)]
        screen.blit(pic,(self.x_pos-pic.get_width()//2,self.y_pos-pic.get_height()//2))            

    def drawHitbox(self):
        draw.rect(screen, (255,0,0), self.hitbox)
        draw.rect(screen, (0,255,0), self.hitbox_top)
        draw.rect(screen, (0,0,255), self.hitbox_bottom)
        draw.rect(screen, (0,255,0), self.hitbox_left)
        draw.rect(screen, (0,0,255), self.hitbox_right)

    def update(self):
        self.hitbox = Rect(self.x_pos - 35, self.y_pos - 35, 70, 70)
        self.hitbox_top = Rect(self.x_pos - 35, self.y_pos - 35, 70, 35)
        self.hitbox_bottom = Rect(self.x_pos - 35, self.y_pos, 70, 35)
        self.hitbox_left = Rect(self.x_pos - 35, self.y_pos - 35, 35, 70)
        self.hitbox_right = Rect(self.x_pos, self.y_pos - 35, 35, 70)


        



        
