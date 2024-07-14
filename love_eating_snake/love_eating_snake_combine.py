import pygame
from pygame.locals import *
import sys
WINDOW_HEIGHT=600
WINDOW_WIDTH=600
class Snake:
    def __init__(self,name):
        self.name=name

    def snake_choose(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    pygame.quit()
                    import love_eating_snake_not_ai

                elif event.key == pygame.K_2:
                    pygame.quit()
                    import love_eating_snake_ai

                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

pygame.init()
start=Snake('user')
Main_Display=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
Main_Font=pygame.font.Font(None,20)
pygame.display.set_caption('love_eating_snake_startal')
title_Font=pygame.font.Font(None,45)
title_content=title_Font.render('love_eating_snake', True, (255, 255, 255), (0, 0, 0))#黑底白字
while True:
    Main_Display.fill((0,0,0))
    rect1=pygame.Rect(50,50,100,100)
    rect1.center=((WINDOW_WIDTH/2)-120,WINDOW_HEIGHT/2)
    Main_Display.blit(title_content,rect1)
    press_start=Main_Font.render('1 for not_ai,2 for ai,q for quit',True, (255, 255, 255))#白字黑底
    press_Rect=press_start.get_rect()
    press_Rect.topleft=(WINDOW_WIDTH-300,WINDOW_HEIGHT-30)
    Main_Display.blit(press_start,press_Rect)
    if start.snake_choose():
        pass
    pygame.display.update()
