from pygame import *

screen = display.set_mode((800,600))

class BoyAI:

    def __init__(self, x_pos, y_pos, pics, startX, startY, endX, endY):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.pics = pics #2d list
        self.hitbox = Rect(x_pos - 35, y_pos - 35, 70, 70)
        self.startX = startX
        self.startY = startY
        self.endX = endX
        self.endY = endY
        self.targetX = endX
        self.targetY = endY

        right = []
        down = []
        up = []
        left = []
        
        for i in range(3):
            right.append(image.load("Boy_AI/right/right" + str(i) + ".png"))
        for i in range(3):
            down.append(image.load("Boy_AI/down/down" + str(i) + ".png"))
        for i in range(3):
            up.append(image.load("Boy_AI/up/up" + str(i) + ".png"))
        for i in range(3):
            left.append(image.load("Boy_AI/left/left" + str(i) + ".png"))

        pics[0] = right
        pics[1] = down
        pics[2] = up
        pics[3] = left
        
        self.move = 0
        self.frame = 0



    def moveBoy(self, newX, newY):

        newMove = -1

        if self.x_pos < newX:
            newMove = 0
            self.x_pos += 4
        elif self.y_pos < newY:
            newMove = 1
            self.y_pos += 4
        elif self.y_pos > newY:
            newMove = 2
            self.y_pos -= 4
        elif self.x_pos > newX:
            newMove = 3
            self.x_pos -= 4
        else:
            self.frame = 0

        move = self.move

        if move == newMove:  # 0 is a standing pose, so we want to skip over it when we are moving
            self.frame = self.frame + 0.27
            if self.frame >= len(self.pics[self.move]):
                self.frame = 1
        elif newMove != -1:  # a move was selected
            self.move = newMove  # make that our current move
            self.frame = 1

        if self.frame == 0:
            return "Turn"

    def makeMove(self, name, start,end):
        move = []
        for i in range(start,end+1):
            move.append(image.load("%s/%s%d.png" % (name,name,i)))
            
        return move

    def drawBoyAI(self):

        move = self.move
        frame = self.frame
        pics = self.pics

        pic = pics[move][int(frame)]
        screen.blit(pic,(self.x_pos-pic.get_width()//2,self.y_pos-pic.get_height()//2))

    def drawHitbox(self):
        draw.rect(screen, (255,0,0), self.hitbox)

    def update(self):
        self.hitbox = Rect(self.x_pos - 35, self.y_pos - 35, 70, 70)




