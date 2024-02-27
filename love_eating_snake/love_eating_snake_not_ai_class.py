#蛇类
import random
from random import randint
import pygame
import sys
from pygame.locals import *
def value_tranport(width,height,block_h,block_w,body_size):
    global WIDTH,HEIGHT,BLOCK_H,BLOCK_W,BODY_SIZE,ERR,HEAD
    WIDTH=width
    HEIGHT=height
    BLOCK_H=block_h
    BLOCK_W=block_w
    BODY_SIZE=body_size
    ERR = -1145141919810
    HEAD=0
    #Main_Display = main_display

def transfer(main_display,main_font):
    global Main_Display,Main_Font
    Main_Display = main_display
    Main_Font = main_font

def end():
    def choose():
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_q:
                    pygame.quit()
                    sys.exit()
                elif event.key==pygame.K_a:
                    pygame.quit()
                    import love_eating_snake_combine
    pygame.quit()
    pygame.init()
    Main_Display1=pygame.display.set_mode((400,400))
    Main_Font1=pygame.font.Font(None,20)
    pygame.display.set_caption('end_board')
    title_Font1=pygame.font.Font(None,45)
    title_content1=title_Font1.render('Game over!!! You died!!!',True,(255,255,255),(0,0,0))
    while True:
        Main_Display1.fill((0,0,0))
        rect1=pygame.Rect(50,50,100,100)
        rect1.center=(80,200)
        Main_Display1.blit(title_content1,rect1)
        press_end=Main_Font1.render('q for quit or a for again!',True, (255, 255, 255))
        press_Rect1=press_end.get_rect()
        press_Rect1.topleft=(100,350)
        Main_Display1.blit(press_end,press_Rect1)
        if choose():
            pass
        pygame.display.update()

class Snake_not_ai:
    def __init__(self):
        self.score=None
        self.snake_locations=None
        self.food_location=None
        self.direction=None

    def same_pace(self,food_location):
        self.food_location=food_location 

    def same_score(self,score):
        self.score=score

    def same_turn(self,direction):
        self.direction=direction

    def same_locations(self,snake_locations):
        self.snake_locations=snake_locations
    #得分函数：
    def scores(self,score):
        score_Content=Main_Font.render('scores:%s' % (self.score),True,(255,255,255))#白色的分数
        score_rect=score_Content.get_rect()
        score_rect.topleft=(WIDTH-100,10)
        Main_Display.blit(score_Content,score_rect)
        #这算是个公式了，先content决定内容的长相，然后get_rect(),再决定位置，最后用bilt结合一下

    #random爆米函数：
    def random_food(self,snake_locations):
        #这个函数随机生成了米
        mi=True
        while mi:
            food_location={'x':random.randint(0,BLOCK_W-1),'y':random.randint(0,BLOCK_H-1)}
            if food_location not in (self.snake_locations): #判断米的生成位置合不合法
                mi=False
        return food_location

    def random_food_show(self,food_location):
        #这个函数展示了米
        x=self.food_location['x']*BODY_SIZE #米的长度
        y=self.food_location['y']*BODY_SIZE#米的高度
        food_rect=pygame.Rect(x,y,BODY_SIZE,BODY_SIZE) #获取米的位置和大小
        pygame.draw.rect(Main_Display,(255,0,0),food_rect) #显示米

    #蛇蛇生成函数：
    def snake_show(self,snake_locations):
        x=self.snake_locations[0]['x']*BODY_SIZE
        y=self.snake_locations[0]['y']*BODY_SIZE
        Snake_head_rect=pygame.Rect(x,y,BODY_SIZE,BODY_SIZE)#蛇头部分的填充
        pygame.draw.rect(Main_Display,(255,127,0),Snake_head_rect)
        for location in self.snake_locations[1:]:
            x=location['x']*BODY_SIZE
            y=location['y']*BODY_SIZE
            Snake_part_Rect=pygame.Rect(x,y,BODY_SIZE,BODY_SIZE)
            pygame.draw.rect(Main_Display,(0,127,255),Snake_part_Rect)

    #转向函数：
    def turn_over(self,direction,snake_locations):
        if self.direction == 'up':
            NEW = {'x': self.snake_locations[HEAD]['x'],'y': self.snake_locations[HEAD]['y']-1}
        elif self.direction == 'down':
            NEW = {'x': self.snake_locations[HEAD]['x'],'y': self.snake_locations[HEAD]['y']+1}
        elif self.direction == 'left':
            NEW = {'x': self.snake_locations[HEAD]['x']-1,'y': self.snake_locations[HEAD]['y']}
        elif self.direction == 'right':
            NEW = {'x': self.snake_locations[HEAD]['x']+1,'y': self.snake_locations[HEAD]['y']}
        self.snake_locations.insert(0,NEW)
        return self.direction,self.snake_locations

    #判断函数：
    def check_boom(self,snake_locations):
        if(self.snake_locations[HEAD]['x']==-1) or (self.snake_locations[HEAD]['x']==BLOCK_W) or  (self.snake_locations[HEAD]['y']==-1) or (self.snake_locations[HEAD]['y']==BLOCK_H):
            return end()
        if self.snake_locations[HEAD] in self.snake_locations[1:]:
            return end()