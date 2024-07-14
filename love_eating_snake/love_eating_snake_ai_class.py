#蛇类
import random
from random import randint
import pygame
import sys
from pygame.locals import *
def value_tranport(width,height,block_h,block_w,free_place,body_place,field_size,body_size,Best_move):
    global WIDTH,HEIGHT,BLOCK_H,BLOCK_W,FREE_PLACE,BODY_PLACE,FIELD_SIZE,BODY_SIZE,best_move,FOOD,move_directions,HEAD,ERR
    WIDTH=width
    HEIGHT=height
    BLOCK_H=block_h
    BLOCK_W=block_w
    FREE_PLACE=free_place
    BODY_PLACE=body_place
    FIELD_SIZE=field_size
    BODY_SIZE=body_size
    best_move=Best_move
    FOOD = 0
    move_directions = {'left': -1, 'right': 1, 'up': -BLOCK_W, 'down': BLOCK_W}
    HEAD = 0
    ERR = -1145141919810
    #Main_Display = main_display

def transfer(main_display,main_font):
    global Main_Display,Main_Font
    Main_Display = main_display
    Main_Font = main_font
    
class Snake_ai:
    def __init__(self):
        self.score = None
        self.food_location = None
        self.index = None
        self.snake = None
        self.board = None
        self.move_direction = None
        self.direction = None

    # 传入函数：
    def same_scores(self, score):
        self.score = score

    def same_food_location(self, food_location):
        self.food_location = food_location

    def same_index(self, index):
        self.index = index

    def same_snake(self, snake):
        self.snake = snake

    def same_board(self, board):
        self.board = board

    def same_move_directionss(self, move_direction):
        self.move_directions = move_direction

    def same_direction(self, direction):
        self.direction = direction

    # 显示当前得分
    def scores(self, score):
        score_Content = Main_Font.render('得分：%s' % (self.score), True, (255, 255, 255))
        score_Rect = score_Content.get_rect()
        score_Rect.topleft = (WIDTH - 120, 10)
        Main_Display.blit(score_Content, score_Rect)

    # 爆米位置（出现食物）
    def random_food(self, snake):
        flag = True
        while flag:
            food_location = {'x': random.randint(0, BLOCK_W - 1), 'y': random.randint(0, BLOCK_H - 1)}#出去边界情况之后出现食物
            if food_location not in self.snake:#不与蛇重复
                flag = False
        return food_location
    # 随机爆米显示函数（把食物展示出来）
    def random_food_show(self, food_location):
        x = self.food_location['x'] * BODY_SIZE
        y = self.food_location['y'] * BODY_SIZE
        food_rect = pygame.Rect(x, y, BODY_SIZE, BODY_SIZE)
        pygame.draw.rect(Main_Display, (255, 0, 0), food_rect)

    # 蛇蛇显示函数
    def snake_show(self, snake):
        x = self.snake[0]['x'] * BODY_SIZE#蛇头
        y = self.snake[0]['y'] * BODY_SIZE#蛇头
        Snake_head_Rect = pygame.Rect(x, y, BODY_SIZE, BODY_SIZE)
        pygame.draw.rect(Main_Display, (255, 127, 0), Snake_head_Rect)
        x = self.snake[-1]['x'] * BODY_SIZE
        y = self.snake[-1]['y'] * BODY_SIZE
        Snake_tail_Rect = pygame.Rect(x, y, BODY_SIZE , BODY_SIZE)
        pygame.draw.rect(Main_Display, (255, 100, 100),Snake_tail_Rect)
        for location in self.snake[1:]:
            if location!=self.snake[-1]:
                x = location['x'] * BODY_SIZE#蛇身
                y = location['y'] * BODY_SIZE#蛇身
                Snake_part_Rect = pygame.Rect(x, y, BODY_SIZE, BODY_SIZE)
                pygame.draw.rect(Main_Display, (0, 127, 255), Snake_part_Rect)

    # 判断该位置是否为空
    def place_free(self, index, snake):
        location_x = self.index % BLOCK_W
        location_y = self.index // BLOCK_W
        index1 = {'x': location_x, 'y': location_y}
        return (index1 not in self.snake)#为空

    # 重置board
    def board_reset(self, snake, board, food_location):
        temp_board = self.board[:]
        food_index = self.food_location['x'] + self.food_location['y'] * BLOCK_W#食物坐标
        for i in range(FIELD_SIZE):#在场地里面搜索
            self.same_index(i)#重置
            if i == food_index:
                temp_board[i] = FOOD#是食物就归为食物
            elif Snake_ai.place_free(self, i, self.snake):
                temp_board[i] = FREE_PLACE#没有就free
            else:
                temp_board[i] = BODY_PLACE#有就是蛇
        # Snake_ai.same_board(self,temp_board)####################possible error
        return temp_board#返回更新的board

    # 检查位置index是否可以向当前move方向运动
    def check_move(self, index, move_directions):
        flag = False
        if self.move_directions == 'left':#向左走
            if self.index % BLOCK_W > 0:
                flag = True
            else:
                flag = False
        elif self.move_directions == 'right':#向右走
            if self.index % BLOCK_W < BLOCK_W - 1:
                flag = True
            else:
                flag = False
        elif self.move_directions == 'up':#向上走
            if self.index > BLOCK_W - 1:
                flag = True
            else:
                flag = False
        elif self.move_directions == 'down':#向下走
            if self.index < FIELD_SIZE - BLOCK_W:
                flag = True
            else:
                flag = False
        return flag

    # //////上面没问题
    # BFS
    def BFS(self, snake, food_location, board):
        temp_board = self.board[:]  # 建立一个临时版
        food_index = self.food_location['x'] +self.food_location['y'] * BLOCK_W  # 找出食物坐标
        # Snake_ai.same_food_location(self,food_index)
        # Snake_ai.same_board(self,board)出现问题
        res = []  # 存储路径走法
        res.append(food_index)  # 第一位定位为食物坐标
        inres = [0] * FIELD_SIZE#把board遍历为0
        flag = False
        while len(res) != 0:  # 如果存在情况
            index = res.pop(0)  # 将食物坐标整成这个，并且pop出去
            Snake_ai.same_index(self, index)  # 传入index
            if inres[index] == 1:#变为1
                continue
            inres[index] = 1
            for move_direction in ['left', 'right', 'up', 'down']:  # 每个方向都查一次
                Snake_ai.same_move_directionss(self, move_direction)#重置
                if Snake_ai.check_move(self, index, move_direction):#可以走
                    if (index + move_directions[move_direction]) == (self.snake[HEAD]['x'] + self.snake[HEAD]['y'] * BLOCK_W):#找到
                        flag = True
                    # print(temp_board[index+move_directions[move_direction]])
                    if temp_board[index + move_directions[move_direction]] < BODY_PLACE:#没找到
                        if temp_board[index + move_directions[move_direction]] > temp_board[index] + 1:#大于1的情况，继续走
                            temp_board[index + move_directions[move_direction]] = temp_board[index] + 1
                            Snake_ai.same_board(self, temp_board)
                            # print(self.board)
                        if inres[index + move_directions[move_direction]] == 0:#找到，加1
                            res.append(index + move_directions[move_direction])
        return (flag, temp_board)#返回一个bool值（是否找到），另外一个路线

    # 找到食物的最短路径
    def shortest_way(self, snake, board):
        best_move = ERR
        min_way = BODY_PLACE
        for move_direction in ['left', 'right', 'up', 'down']:
            index = self.snake[HEAD]['x'] + self.snake[HEAD]['y'] * BLOCK_W#蛇头坐标
            Snake_ai.same_index(self, index)#重置
            Snake_ai.same_move_directionss(self, move_direction)#重置
            if Snake_ai.check_move(self, index, move_direction) and (self.board[index + move_directions[move_direction]] < min_way):#可以走，而且还小
                min_way = self.board[index + move_directions[move_direction]]#最小路径
                best_move = move_direction#最好的方向
        return best_move

    # 找到移动后蛇头的位置
    def head_place(self, snake, direction):
        if self.direction == 'up':#向上
            newHead = {'x': self.snake[HEAD]['x'], 'y': self.snake[HEAD]['y'] - 1}
        elif self.direction == 'down':#向下
            newHead = {'x': self.snake[HEAD]['x'], 'y': self.snake[HEAD]['y'] + 1}
        elif self.direction == 'left':#想左
            newHead = {'x': self.snake[HEAD]['x'] - 1, 'y': self.snake[HEAD]['y']}
        elif self.direction == 'right':#向右
            newHead = {'x': self.snake[HEAD]['x'] + 1, 'y': self.snake[HEAD]['y']}
        # print(newHead)
        return newHead

    # 虚拟运行一次蛇，看是不是有通路（没有问题）#让蛇更聪明，这样蛇不会跑死
    def vis_snake(self, snake, board, food_location):
        temp_snake = self.snake[:]
        temp_board = self.board[:]#临时板和蛇
        reset_tboard = Snake_ai.board_reset(self, temp_snake, temp_board, self.food_location)
        temp_board = reset_tboard
        Snake_ai.same_board(self, temp_board)  # 重置
        food_eated = False
        while not food_eated:#没有吃到东西
            Snake_ai.same_board(self, temp_board)
            Snake_ai.same_snake(self, temp_snake)#传入
            refresh_tboard = Snake_ai.BFS(self, temp_snake, self.food_location, temp_board)[1]#bfs找到路径
            temp_board = refresh_tboard
            Snake_ai.same_board(self, temp_board)  # 重置
            move_direction1 = Snake_ai.shortest_way(self, temp_snake, temp_board)#最小移动方向是最小路径
            snake_locations = temp_snake[:]  # 目前为止正确###################################################################################
            Snake_ai.same_snake(self, snake_locations)
            Snake_ai.same_direction(self, move_direction1)
            # print(self.direction)
            temp_snake.insert(0, Snake_ai.head_place(self, snake_locations, move_direction1))#虚拟蛇移动
            # 如果新的蛇头正好是食物的位置
            if temp_snake[HEAD] == self.food_location:
                reset_tboard = Snake_ai.board_reset(self, temp_snake, temp_board, self.food_location)
                temp_board = reset_tboard
                Snake_ai.same_board(self, temp_board)
                food_index = self.food_location['x'] + self.food_location['y'] * BLOCK_W
                temp_board[food_index] = BODY_PLACE
                food_eated = True#结束
            else:  # 如果并不是
                print(temp_snake[0]['x'],temp_snake[0]['y'])
                newHead_index = temp_snake[0]['x'] + temp_snake[0]['y'] * BLOCK_W
                temp_board[newHead_index] = BODY_PLACE#移动
                tail_index = temp_snake[-1]['x'] + temp_snake[-1]['y'] * BLOCK_W
                temp_board[tail_index] = FREE_PLACE#移动
                del temp_snake[-1]#移动
        print("yes",temp_snake,food_location)
        return temp_snake, temp_board

    # 找蛇头到蛇尾的安全函数，
    def tail_find(self, snake, board, food_location):
        temp_board = self.board[:]
        temp_snake = self.snake[:]
        # 将蛇尾看作食物
        tail_index = temp_snake[-1]['x'] + temp_snake[-1]['y'] * BLOCK_W
        temp_board[tail_index] = FOOD
        Snake_ai.same_board(self, temp_board)  # 重置
        v_food = temp_snake[-1]
        # 食物看作蛇身(重复赋值了)
        food_index = self.food_location['x'] + self.food_location['y'] * BLOCK_W
        temp_board[food_index] = BODY_PLACE
        # 求得每个位置到蛇尾的路径长度
        Snake_ai.same_board(self, temp_board)
        Snake_ai.same_snake(self, temp_snake)  #############
        Snake_ai.same_food_location(self, v_food)
        result, refresh_tboard = Snake_ai.BFS(self, temp_snake, v_food, temp_board)#广搜
        temp_board = refresh_tboard
        Snake_ai.same_board(self, temp_board)  # 重置
        for move_direction in ['left', 'right', 'up', 'down']:
            index = temp_snake[HEAD]['x'] + temp_snake[HEAD]['y'] * BLOCK_W#头坐标
            tail_index = temp_snake[-1]['x'] + temp_snake[-1]['y'] * BLOCK_W#尾坐标
            Snake_ai.same_index(self, index)
            Snake_ai.same_move_directionss(self, move_direction)
            # print(index,self.index)########################################
            if Snake_ai.check_move(self, index, move_direction) and (index + move_directions[move_direction] == tail_index) and (len(temp_snake) >= 3):
                result = False
        return result

    # 找尾巴的最长路径函数
    def longest_way(self, snake, board):
        best_move = ERR
        max_distance = -1
        for move_direction in ['left', 'right', 'up', 'down']:
            index = self.snake[HEAD]['x'] + self.snake[HEAD]['y'] * BLOCK_W
            Snake_ai.same_index(self, index)
            Snake_ai.same_move_directionss(self, move_direction)#重置
            if Snake_ai.check_move(self, index, move_direction) and (
                    self.board[index + move_directions[move_direction]] > max_distance) and (
                    self.board[index + move_directions[move_direction]] < FREE_PLACE):#可以走
                max_distance = self.board[index + move_directions[move_direction]]#蛇头走
                best_move = move_direction
                # print(best_move)
        return best_move#就是一个不停更新找路径的过程

    # 让蛇头朝着蛇尾运行一步
    def move_to_tail(self, snake, board, food_location):
        temp_snake = self.snake[:]
        Snake_ai.same_snake(self, temp_snake)  # 重置
        temp_board = Snake_ai.board_reset(self, temp_snake, self.board, self.food_location)
        # 将蛇尾看作食物
        tail_index = temp_snake[-1]['x'] + temp_snake[-1]['y'] * BLOCK_W
        temp_board[tail_index] = FOOD
        v_food = temp_snake[-1]
        # 食物看作蛇身
        food_index = self.food_location['x'] + self.food_location['y'] * BLOCK_W
        temp_board[food_index] = BODY_PLACE
        # 求得每个位置到蛇尾的路径长度
        Snake_ai.same_board(self, temp_board)
        Snake_ai.same_snake(self, temp_snake)
        Snake_ai.same_food_location(self, v_food)
        result, refresh_tboard = Snake_ai.BFS(self, temp_snake, v_food, temp_board)  # 广搜走最小
        temp_board = refresh_tboard
        Snake_ai.same_snake(self, temp_snake)
        # 重置
        #temp_board[tail_index] = BODY_PLACE
        Snake_ai.same_board(self, temp_board)
        return Snake_ai.longest_way(self, temp_snake, temp_board)

    # 如果蛇和食物间有路径
    # 则需要找一条安全的路径到食物
    def safe_way(self, snake, board, food_location):
        safe_ways = ERR
        real_snake = self.snake[:]
        real_board = self.board[:]
        real_food_location = self.food_location
        v_snake, v_board = Snake_ai.vis_snake(self, self.snake, self.board, self.food_location)
        Snake_ai.same_snake(self, v_snake)
        Snake_ai.same_board(self, v_board)
        if Snake_ai.tail_find(self, v_snake, v_board, self.food_location):
            #####断点find
            #print("?????")
            Snake_ai.same_food_location(self,real_food_location)
            Snake_ai.same_snake(self, real_snake)
            Snake_ai.same_board(self,real_board)
            safe_ways = Snake_ai.shortest_way(self, real_snake, real_board)  # 如果可以找到路径就走最小路径
        else:
            #####
            #####
            #print("!!!!!")
            Snake_ai.same_snake(self,real_snake)
            Snake_ai.same_board(self,real_board)
            Snake_ai.same_food_location(self, real_food_location)
            safe_ways = Snake_ai.move_to_tail(self, real_snake, real_board, self.food_location)  # 没有就朝着尾巴走
            Snake_ai.same_food_location(self, real_food_location)
            Snake_ai.same_board(self, real_board)
            Snake_ai.same_snake(self, real_snake)
        return safe_ways

    # 蛇陷入“死路”的时候走几步，看是不是真的走死了
    def wander(self, snake, board, food_location):
        best_move = ERR
        reset_board = Snake_ai.board_reset(self, self.snake, self.board, self.food_location)
        board = reset_board
        Snake_ai.same_board(self, board)
        result, refresh_board = Snake_ai.BFS(self, self.snake, self.food_location, self.board)  # 广搜一次
        Snake_ai.same_board(self, refresh_board)
        min_way = BODY_PLACE
        for move_direction in ['left', 'right', 'up', 'down']:
            index = self.snake[HEAD]['x'] + self.snake[HEAD]['y'] * BLOCK_W
            Snake_ai.same_index(self, index)
            Snake_ai.same_move_directionss(self, move_direction)
            if Snake_ai.check_move(self, index, move_direction) and (
                    self.board[index + move_directions[move_direction]] < min_way):
                min_way = self.board[index + move_directions[move_direction]]
                best_move = move_direction
                # print(best_move)
        Snake_ai.same_board(self, board)
        return best_move
#######################################################################################################################class结束
