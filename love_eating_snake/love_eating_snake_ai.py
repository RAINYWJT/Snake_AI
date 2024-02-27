import random
from random import randint
import pygame
import sys
from pygame.locals import *
import time
# 一个有用的函数
# 退出:
def close():
    pygame.quit()
    sys.exit()
####################################################################################################tkinter处理部分
# （1）界面处理
# 屏幕大小:
import tkinter as tk
from tkinter import messagebox

win = tk.Tk()
win.title("snake_ai")
screenWidth = win.winfo_screenwidth()  # 获取显示区域的宽度
screenHeight = win.winfo_screenheight()  # 获取显示区域的高度
width = 300  # 设定窗口宽度
height = 160  # 设定窗口高度
left = (screenWidth - width) / 2
top = (screenHeight - height) / 2
# 在设定宽度和高度的基础上指定窗口相对于屏幕左上角的偏移位置
win.geometry("%dx%d+%d+%d" % (width, height, left, top))
win.resizable(0, 0)
win.resizable(0, 0)
# 将俩个标签分别布置在第一行、第二行
tk.Label(win, text="WIDTH(300-1200 & WIDTH%20=0)").grid(row=0)
tk.Label(win, text="HEIGHT(300-1200 & HEIGHT%20=0)").grid(row=1)
tk.Label(win, text="GAME_RATE(1-500)").grid(row=2)
# 创建输入框控件
e1 = tk.Entry(win)
e2 = tk.Entry(win)
e3 = tk.Entry(win)
e1.grid(row=0, column=1, padx=10, pady=5)
e2.grid(row=1, column=1, padx=10, pady=5)
e3.grid(row=2, column=1, padx=10, pady=5)
# 使用 grid()的函数来布局，并控制按钮的显示位置
def get_input():
    global WIDTH, HEIGHT, GAME_RATE
    WIDTH = e1.get()
    HEIGHT = e2.get()
    GAME_RATE = e3.get()
    if (int(WIDTH) >= 300 and int(WIDTH) <= 1200 and int(WIDTH) % 20 == 0) and (
            int(HEIGHT) >= 300 and int(HEIGHT) <= 1200 and int(HEIGHT) % 20 == 0) and (
            int(GAME_RATE) >= 1 and int(GAME_RATE) <= 500):
        win.destroy()
    else:
        answer = messagebox.askyesno("warning!", "please follow the tips!")
        win.mainloop()
tk.Button(win, text="GO", width=10, command=get_input).grid(row=3, column=0, sticky="w", padx=10, pady=5)
win.mainloop()
############################################################################################################tkinter结束
#基础设置
WIDTH = int(WIDTH)
HEIGHT = int(HEIGHT)
GAME_RATE = int(GAME_RATE)
# 错误码
ERR = -1145141919810
# 蛇的大小
BODY_SIZE = 20
# 等价的运动区域大小
BLOCK_W = int(WIDTH / BODY_SIZE)
BLOCK_H = int(HEIGHT / BODY_SIZE)
FIELD_SIZE = BLOCK_W * BLOCK_H
# 背景颜色
Background_Color = (0, 0, 0)
# 蛇头索引
HEAD = 0
# 运动方向
best_move = ERR
# 不同东西在矩阵里用不同的数字表示
FOOD = 0
FREE_PLACE = (BLOCK_W + 1) * (BLOCK_H + 1)
BODY_PLACE = 2 * FREE_PLACE
# 运动方向
move_directions = {'left': -1, 'right': 1, 'up': -BLOCK_W, 'down': BLOCK_W}

from love_eating_snake_ai_class import value_tranport
value_tranport(WIDTH,HEIGHT,BLOCK_H,BLOCK_W,FREE_PLACE,BODY_PLACE,FIELD_SIZE,BODY_SIZE,best_move)
# PREPERATION FOR THE GAME WITH PYGAME:#///////////////////////////////////////////////////////////小函数我们不用class来写（我不想用继承啊啊啊啊）
# 检测按键（主要用于键盘读取）
def check_press():
    if len(pygame.event.get(QUIT)) > 0:
        close()
    KeyUp_Events = pygame.event.get(KEYUP)
    if len(KeyUp_Events) == 0:
        return None
    elif KeyUp_Events[0].key == K_ESCAPE:#退出
        close()
    return KeyUp_Events[0].key

# 画网格
def net_generate():
    # 垂直方向
    for x in range(0, WIDTH, BODY_SIZE):
        pygame.draw.line(Main_Display, (40, 40, 40), (x, 0), (x, HEIGHT))
    # 水平方向
    for y in range(0, HEIGHT, BODY_SIZE):
        pygame.draw.line(Main_Display, (40, 40, 40), (0, y), (WIDTH, y))

# 显示开始界面
def start():
    title_Font = pygame.font.Font(None, 45)
    title_content = title_Font.render('love_eating_snake(ai)', True, (255, 255, 255), (0, 0, 0))  # 黑底白字
    while True:
        Main_Display.fill(Background_Color)  # 背景黑色
        rect1 = pygame.Rect(50, 50, 100, 100)
        rect1.center = ((WIDTH / 2) - 70, HEIGHT / 2)
        Main_Display.blit(title_content, rect1)
        # 下面的小字
        press_start = Main_Font.render('press anything to go on', True, (255, 255, 255))  # 白字黑底
        press_Rect = press_start.get_rect()
        press_Rect.topleft = (WIDTH - 300, HEIGHT - 30)
        Main_Display.blit(press_start, press_Rect)
        if check_press():  # 检查和进入下一层,任意键作为操作列表的第一个元素存在，所以从道理上讲是个true
            pygame.event.get()
            return
        pygame.display.update()

# 显示结束界面
def end():
    def choose():
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_a:
                    pygame.quit()
                    import love_eating_snake_combine
    pygame.quit()
    pygame.init()
    Main_Display1 = pygame.display.set_mode((400, 400))
    Main_Font1 = pygame.font.Font(None, 20)
    pygame.display.set_caption('end_board')
    title_Font1 = pygame.font.Font(None, 22)
    title_content1 = title_Font1.render('Game over!(maybe there is no solution/or ended)', True, (255, 255, 255),(0, 0, 0))
    while True:
        Main_Display1.fill((0, 0, 0))
        rect1 = pygame.Rect(50, 50, 100, 100)
        rect1.center = (80, 200)
        Main_Display1.blit(title_content1, rect1)
        press_end = Main_Font1.render('q for quit or a for again!', True, (255, 255, 255))
        press_Rect1 = press_end.get_rect()
        press_Rect1.topleft = (100, 350)
        Main_Display1.blit(press_end, press_Rect1)
        if choose():
            pass
        pygame.display.update()
######################################################################################
from love_eating_snake_ai_class import Snake_ai
#########################################################################################################################以上是一些游戏界面控制函数
#流程监控函数两个：
# 蛇在最后一般剩下10个左右的时候会产生无解的情况，我们将这种情况纳入处理范围（蛇可以自动退出）
def end_the_game(time_now):
    time_temp_now = time.time()
    if time_temp_now - time_now >= 20:
        return end()
    else:
        pass
        print(time_temp_now-time_now)

# 一个估值函数：
def evaluate(w, h):
    w = BLOCK_W  # 10s
    h = BLOCK_H  # 10s
    time = 20 + (BLOCK_H - 15) * 0.5 + (BLOCK_W - 15) * 0.5
    return time
##########################################################################################################################流程控制结束
# 运行游戏
def Run_Game():
    # 一维数组来表示蛇运动的矩形场地
    board = [0] * FIELD_SIZE  # 全部为零
    # 蛇出生地
    start_x = random.randint(5, BLOCK_W - 8)
    start_y = random.randint(5, BLOCK_H - 8)
    snake_locations = [{'x': start_x, 'y': start_y}]#蛇初始化
    snake = Snake_ai()  # 类定义
    snake.same_snake(snake_locations)  # 传值
    snake.same_board(board)
    food_location = snake.random_food(snake_locations)#food_location定义
    snake.same_food_location(food_location)  # 传值
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                close()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    close()
        # 进行基本塑造
        # print(snake_locations)
        Main_Display.fill(Background_Color)
        net_generate()
        snake.snake_show(snake_locations)
        snake.random_food_show(food_location)
        a = len(snake_locations) - 1
        snake.same_scores(a)
        snake.scores(a)
        # 初始化开始
        reset_board = snake.board_reset(snake_locations, board, food_location)  # 每走一次，就对这个board进行重置
        board = reset_board
        snake.same_board(board)#重置
        result, refresh_board = snake.BFS(snake_locations, food_location, board)  # 每走一次，就对这个进行广搜
        board = refresh_board
        snake.same_board(board)#重置
        # print(board,food_location,snake_locations)#这里是有传值的
        # 开始
        # print(food_location)
        if result:  # 如果蛇可以吃到食物
            best_move = snake.safe_way(snake_locations, board, food_location)#最好路径就是蛇的安全路径
        else:
            #print(snake_locations)
            best_move = snake.move_to_tail(snake_locations, board, food_location)  # 没有就追着尾巴跑
            snake.same_food_location(food_location)#将此处三个值重置
            snake.same_board(board)#将此处三个值重置
            snake.same_snake(snake_locations)#将此处三个值重置
            # print(snake_locations,board,food_location)
            #print("no!!!")
        if best_move == ERR:  #没有解
            best_move = snake.wander(snake_locations, board, food_location)  # 在bfs搜不到的时候，蛇进行wander这样就保证可能走几步就有解了
            #print("no!!!!!!!")
        if best_move != ERR:  # 如果可以走
            snake.same_direction(best_move) #重置
            #print(best_move)  # 有解，而且可以吃一个了，说明第二次没有起作用#############################################################
            newHead1 = snake.head_place(snake_locations, best_move)  # 新走的蛇头的坐标定义为一个newhead
            snake_locations.insert(0, newHead1) #新增一个snake_location
            # snake.same_snake(snake_locations)
            head_index = snake_locations[HEAD]['x'] + snake_locations[HEAD]['y'] * BLOCK_W  # 找出蛇的头坐标
            tail_index = snake_locations[-1]['x'] + snake_locations[-1]['y'] * BLOCK_W  # 找出蛇的尾坐标
            if (snake_locations[HEAD]['x'] == food_location['x']) and (snake_locations[HEAD]['y'] == food_location['y']):  # 吃到东西了
                # print(snake_locations[HEAD]['x'],food_location['x'])
                #print(food_location)
                board[head_index] = BODY_PLACE  # 头坐标属于body（将食物吃进来）
                # print(BODY_PLACE)
                # snake.same_snake(snake_locations)
                # snake.same_board(board)
                snake.same_snake(snake_locations)#重置
                snake.same_board(board)#重置
                time_now = time.time()#记录时间
                if len(snake_locations) < FIELD_SIZE:  # 没满
                    food_location = snake.random_food(snake_locations)  # 继续生成食物
                    snake.same_food_location(food_location)#重置
                    #print("yes")
            else:  # 如果不是一样的坐标
                board[head_index] = BODY_PLACE  # head是body
                board[tail_index] = FREE_PLACE  # tail是空的
                #print(snake_locations)
                del snake_locations[-1]  # 尾部减一，相当于动了一步
                snake.same_snake(snake_locations)#重置
                snake.same_board(board)#重置
        else:  # 如果以上都没有解
            return end()#结束
        if len(snake_locations) - 1 >= 1:
            end_the_game(time_now)#吃了一个就开始计时
        pygame.display.update()
        Snake_Clock.tick(GAME_RATE)#更新

# 主函数
global Main_Display, Main_Font, Snake_Clock
pygame.init()#初始化
Snake_Clock = pygame.time.Clock()
Main_Display = pygame.display.set_mode((WIDTH, HEIGHT))
Main_Font = pygame.font.Font(None, 18)
from love_eating_snake_ai_class import transfer
transfer(Main_Display,Main_Font)
pygame.display.set_caption('AI_snake')
start()
while True:
    Run_Game()#主函数


























