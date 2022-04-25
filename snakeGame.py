import pygame
import time
import random
pygame.init()
dis_width=800
dis_length=600
dis=pygame.display.set_mode((dis_width,dis_length))
pygame.display.set_caption("Snake Game")
white=(255,255,255)
green=(0,255,0)
blue=(0,0,255)
red=(255,0,0)
black=(0,0,0)
snake_block=10
snake_speed=10
font_style = pygame.font.SysFont(None, 30)
score_font = pygame.font.SysFont("comicsansms", 35)
clock = pygame.time.Clock()
def draw_snake(snake_list,snake_block):
    for head in snake_list:
        pygame.draw.rect(dis,blue, [head[0], head[1], snake_block, snake_block])
def show_score(score):
    mesg=score_font.render("Score:"+str(score),True,black)
    dis.blit(mesg,[20,40])
def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/3, dis_length/3])
def gameLoop():  # creating a function
    game_over = False
    game_close = False
    score=0
    snake_length=1
    snake_list=[]
    x1 = dis_width / 2
    y1 = dis_length / 2
    x1_change = 0
    y1_change = 0

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_length - snake_block) / 10.0) * 10.0

    while(not game_over):
        while game_close == True:
            dis.fill(white)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x1_change=-snake_block
                    y1_change=0
                elif event.key==pygame.K_RIGHT:
                    x1_change=snake_block
                    y1_change=0
                elif event.key==pygame.K_DOWN:
                    x1_change=0
                    y1_change=snake_block
                elif event.key==pygame.K_UP:
                    x1_change=0
                    y1_change=-snake_block
        if x1>=dis_width or x1<=0 or y1<=0 or y1>=dis_length:
            game_close=True
        x1=x1+x1_change
        y1=y1+y1_change
        dis.fill(white)
        pygame.draw.rect(dis,red, [foodx, foody, snake_block, snake_block])
        snake_head=[]
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True
        show_score(score)
        draw_snake(snake_list,snake_block)
        pygame.display.update()
        clock.tick(snake_speed)
        if x1==foodx and y1==foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_length - snake_block) / 10.0) * 10.0
            snake_length+=1
            score+=10
    pygame.quit()
    quit()
gameLoop()
