import random
import pygame
import sys
from pygame.locals import *
import love_eating_snake_not_ai_class
#一个有用的函数
#退出:
def close():
    pygame.quit()
    sys.exit()
#PREPERATION FOR THE GAME WITH PYGAME:

import tkinter as tk
from tkinter import messagebox
win = tk.Tk()
win.title("snake_not_ai")
screenWidth = win.winfo_screenwidth()  # 获取显示区域的宽度
screenHeight = win.winfo_screenheight()  # 获取显示区域的高度
width = 300  # 设定窗口宽度
height = 160  # 设定窗口高度
left = (screenWidth - width) / 2
top = (screenHeight - height) / 2
# 在设定宽度和高度的基础上指定窗口相对于屏幕左上角的偏移位置
win.geometry("%dx%d+%d+%d" % (width, height, left, top))
win.resizable(0,0)
# 将俩个标签分别布置在第一行、第二行
tk.Label(win, text="WIDTH(400-1200 & WIDTH%20=0)").grid(row=0)
tk.Label(win, text="HEIGHT(400-1200 & HEIGHT%20=0)").grid(row=1)
tk.Label(win, text="GAME_RATE(1-20)").grid(row=2)
# 创建输入框控件
e1 = tk.Entry(win)
e2 = tk.Entry(win)
e3 = tk.Entry(win)
e1.grid(row=0, column=1, padx=10, pady=5)
e2.grid(row=1, column=1, padx=10, pady=5)
e3.grid(row=2, column=1, padx=10, pady=5)
# 使用 grid()的函数来布局，并控制按钮的显示位置
def get_input():
    global WIDTH,HEIGHT,GAME_RATE
    WIDTH= e1.get()
    HEIGHT=e2.get()
    GAME_RATE=e3.get()
    if (int(WIDTH)>=400 and int(WIDTH)<=1200 and int(WIDTH)%20==0) and (int(HEIGHT)>=400 and int(HEIGHT)<=1200 and int(HEIGHT)%20==0) and (int(GAME_RATE)>=1 and int(GAME_RATE)<=20):
        win.destroy()
    else:
        answer = messagebox.askyesno("warning!", "please follow the tips!")
        win.mainloop()

tk.Button(win, text="GO", width=10,command=get_input).grid(row=3, column=0, sticky="w", padx=10, pady=5)
win.mainloop()

WIDTH=int(WIDTH)
HEIGHT=int(HEIGHT)
GAME_RATE=float(GAME_RATE)
#（1）界面处理
#屏幕大小:
#错误码:
ERR=-1145141919810
#游戏颜色设置(black):
Background_Color=(0,0,0)
#（2）蛇的处理
#一小块蛇的身体大小:
BODY_SIZE=20
#蛇头:
HEAD=0
#等价大小(将蛇的身体平均放在整个格子中):
BLOCK_W=int(WIDTH/BODY_SIZE)
BLOCK_H=int(HEIGHT/BODY_SIZE)

from love_eating_snake_not_ai_class import value_tranport
value_tranport(WIDTH,HEIGHT,BLOCK_H,BLOCK_W,BODY_SIZE)
#直接沿用ai蛇的所有性质
#FUNCTIONS:///////////////////////////////////////////////////////////////////////////////////////#################游戏控制开始
#pygame开始界面:
def start():
        title_Font=pygame.font.Font(None,45)
        title_content=title_Font.render('love_eating_snake_not_ai', True, (255, 255, 255), (0, 0, 0))#黑底白字
        while True:
            Main_Display.fill(Background_Color)#背景黑色
            rect1=pygame.Rect(50,50,100,100)
            rect1.center=((WIDTH/2)-120,HEIGHT/2)
            Main_Display.blit(title_content,rect1)
            #下面的小字
            press_start=Main_Font.render('press anything to go on',True, (255, 255, 255))#白字黑底
            press_Rect=press_start.get_rect()
            press_Rect.topleft=(WIDTH-300,HEIGHT-30)
            Main_Display.blit(press_start,press_Rect)
            if check_press():#检查和进入下一层,任意键作为操作列表的第一个元素存在，所以从道理上讲是个true
                pygame.event.get()     
                return 
            pygame.display.update()

def net_generate():
    # 垂直方向
    for x in range(0, WIDTH, BODY_SIZE):
        pygame.draw.line(Main_Display, (40, 40, 40), (x, 0), (x, HEIGHT))
    # 水平方向
    for y in range(0, HEIGHT, BODY_SIZE):
        pygame.draw.line(Main_Display, (40, 40, 40), (0, y), (WIDTH, y))

#读取操作的函数：
def check_press():
    if len(pygame.event.get(QUIT))>0:
        close()
    key_events=pygame.event.get(KEYUP)#从quene中获取keyup的事件，keyup（key，mod））
    if len(key_events)==0:
        return None
    elif key_events[0].key==K_ESCAPE:#第一个操作
        close()
    return key_events[0].key #返回

##############################################################################################################################游戏控制结束
from love_eating_snake_not_ai_class import Snake_not_ai
##############################################################################################################################class
def game_startal():
    #蛇的出生
    start_x = random.randint(5, BLOCK_W-8)
    start_y = random.randint(5, BLOCK_H-8)
    direction='right'
    snake_locations=[{'x': start_x, 'y': start_y},{'x': start_x-1, 'y': start_y},{'x': start_x-2, 'y': start_y}]
    snake=Snake_not_ai()
    snake.same_locations(snake_locations)
    food_location=snake.random_food(snake_locations)
    snake.same_pace(food_location)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                close()
            #键盘读取操作
            if (event.type == KEYDOWN):
                if (event.key == K_LEFT) and (direction != 'right'):
                    direction = 'left'
                elif (event.key == K_RIGHT) and (direction != 'left'):
                    direction = 'right'
                elif (event.key == K_UP) and (direction != 'down'):
                    direction = 'up'
                elif (event.key == K_DOWN) and (direction != 'up'):
                    direction = 'down'
                elif (event.key == K_ESCAPE):
                    close()
        #检查snake是不是炸了：
        snake.check_boom(snake_locations)
        #snake的snake_locations：(吃东西)
        if (snake_locations[HEAD]['x']==food_location['x']) and (snake_locations[HEAD]['y']==food_location['y']):
            food_location=snake.random_food(snake_locations)
            snake.same_pace(food_location)
        else:
            del snake_locations[-1]
        #转向
        snake.same_turn(direction)
        snake.turn_over(direction,snake_locations)
        #开始运行
        Main_Display.fill(Background_Color)
        net_generate()
        snake.snake_show(snake_locations)
        snake.random_food_show(food_location)#
        a=(len(snake_locations)-3)
        snake.same_score(a)
        snake.scores(a)
        pygame.display.update()
        Snake_Clock.tick(GAME_RATE)

#运行开始！
global Main_Display,Main_Font,Snake_Clock
pygame.init()
Snake_Clock=pygame.time.Clock()#snake clock的定义
Main_Display=pygame.display.set_mode((WIDTH,HEIGHT))#画图
Main_Font=pygame.font.Font(None,20)
from love_eating_snake_not_ai_class import transfer
transfer(Main_Display,Main_Font)
pygame.display.set_caption('love_eating_snake_ai.py')
start()
while True:
    game_startal()