import queue
import time
from player import player
import sys, pygame
import random

SIZE = WIDTH,HEIGHT = 800,800
BLACK = (0,0,0)
WHITE = (255,255,255)
greed_surface = pygame.image.load("assets/pics/background.jpeg")
greed_surface = pygame.transform.scale(greed_surface, (WIDTH ,HEIGHT))
FPS = 60
pygame.mixer.init()
pygame.mixer.stop()
fly = pygame.mixer.Sound("assets/sound/fly.mp3")
won = pygame.mixer.Sound("assets/sound/won.mp3")


def initialize_grid(m,n):
    # here m,n Indicate the dimension of the m X n grid
    cell_width = WIDTH/n
    cell_height = HEIGHT/m
    grid = []
    for y in range(0,m):
        for x in range(0,n):
            temp_rect = pygame.Rect(x*cell_width,y*cell_height,cell_width,cell_height)
            grid.append(temp_rect)
    return grid
            
def select_random_movement(cell_width):
    c = random.randrange(0,4) 
    x = 0 
    y = 0
    # right
    if (c==0):
        x+= cell_width
    # left
    elif(c==1):
        x-=cell_width
    # down
    elif(c==2):
        y+=cell_width
    # up
    elif(c==3):
        y-=cell_width
    return x,y

def check(p1,p2):
    return (p1 == p2)
def play_random():
    pygame.init()
    SCREEN = pygame.display.set_mode(SIZE)
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)
    run = True
    p1= player(0,0,"red.png",80)
    p2= player(WIDTH - 80,HEIGHT - 80,"purple.png",80)
    trail_p1 = []
    trail_p2 = []
    red = (255,0,0)
    purple  = (128,0,128)
    ellipse_size = (0,0,10,10)
    while run:
        dt = CLOCK.tick(10)
        SCREEN.blit(greed_surface,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # drawing all rects 
        grid = initialize_grid(10,10)
        for cell in grid:
            pygame.draw.rect(SCREEN,WHITE,cell,1)
        
        x1,y1 = select_random_movement(80)
        x2,y2 = select_random_movement(80)
        p1.move(x1,y1,600,600,dt)
        p2.move(x2,y2,600,600,dt)
        pygame.mixer.Sound.play(fly)
        SCREEN.blit(p1.image,p1.image_loc)
        SCREEN.blit(p2.image,p2.image_loc)
        trail_p1.append((p1.image_loc.centerx,p1.image_loc.centery))
        trail_p2.append((p2.image_loc.centerx,p2.image_loc.centery))
        for trail in trail_p1:
            pygame.draw.ellipse(greed_surface,red,(trail[0]-2,trail[1]-2,10,10))
        for trail in trail_p2:
            pygame.draw.ellipse(greed_surface,purple,(trail[0]+2,trail[1]+2,10,10))   
        pygame.display.update()
        if(check(p1.image_loc.center,p2.image_loc.center)):
            pygame.mixer.Sound.play(won)
            time.sleep(2)
            run = False

def initialized_visited(n):
    res =[]
    for i in range(0,n):
        row = []
        for j in range(0,n):
            row.append(0)
        res.append(row)
    return res
        

def play_dfs():
    # MARK CURRENT NODE AS VISITED AND ENQUEUE IT INTO QUEUE
    pygame.init()
    
    SCREEN = pygame.display.set_mode(SIZE)
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)
    run = True
    p1= player(0,0,"red.png",80)
    p2= player(WIDTH - 80,HEIGHT - 80,"purple.png",80)
    trail_p1 = []
    trail_p1.append((p1.image_loc.centerx,p1.image_loc.centery))
    trail_p2 = []
    trail_p2.append((p2.image_loc.centerx,p2.image_loc.centery))
    visited_p1 = initialized_visited(10)
    visited_p1[0][0] = 1
    queue_p1 = [[0,0]]
    visited_p2 = initialize_grid(10)
    queue_p2 = [[9,9]]
    visited_p2[9][9] = 1
    red = (255,0,0)
    purple  = (128,0,128)
    ellipse_size = (0,0,10,10)
    while run:
        dt = CLOCK.tick(10)
        SCREEN.blit(greed_surface,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # drawing all rects 
        grid = initialize_grid(10,10)
        for cell in grid:
            pygame.draw.rect(SCREEN,WHITE,cell,1)
        p1_cords = queue_p1.pop(0)
        p2_cords = queue_p2.pop(0)
        if(p1_cords == p2_cords):
            run = False
            time.sleep(2)
        # visit all neighbours of cell 
        x1,y1 = select_random_movement(80)
        x2,y2 = select_random_movement(80)
        p1.move(x1,y1,600,600,dt)
        p2.move(x2,y2,600,600,dt)
        
        SCREEN.blit(p1.image,p1.image_loc)
        SCREEN.blit(p2.image,p2.image_loc)
        trail_p1.append((p1.image_loc.centerx,p1.image_loc.centery))
        trail_p2.append((p2.image_loc.centerx,p2.image_loc.centery))
        for trail in trail_p1:
            pygame.draw.ellipse(greed_surface,red,(trail[0]-2,trail[1]-2,10,10))
        for trail in trail_p2:
            pygame.draw.ellipse(greed_surface,purple,(trail[0]+2,trail[1]+2,10,10))   
        pygame.display.update()
        if(check(p1.image_loc.center,p2.image_loc.center)):
            time.sleep(2)
            run = False
    # DEQUE THE CELL
    # VISIT ALL NEIGHBOURS CELL 
    # REPEAT UNTILL REACH GOAL NODE
    
def play_bfs():
    # MARK CURRENT NODE AS VISITED AND ENQUEUE IT INTO QUEUE
    pygame.init()
    SCREEN = pygame.display.set_mode(SIZE)
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)
    run = True
    p1= player(0,0,"red.png",80)
    p2= player(WIDTH - 80,HEIGHT - 80,"purple.png",80)
    trail_p1 = []
    trail_p1.append((p1.image_loc.centerx,p1.image_loc.centery))
    trail_p2 = []
    trail_p2.append((p2.image_loc.centerx,p2.image_loc.centery))
    visited_p1 = initialized_visited(10)
    visited_p1[0][0] = 1
    queue_p1 = [[0,0]]
    visited_p2 = initialize_grid(10)
    queue_p2 = [[9,9]]
    visited_p2[9][9] = 1
    red = (255,0,0)
    purple  = (128,0,128)
    ellipse_size = (0,0,10,10)
    while run:
        dt = CLOCK.tick(10)
        SCREEN.blit(greed_surface,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # drawing all rects 
        grid = initialize_grid(10,10)
        for cell in grid:
            pygame.draw.rect(SCREEN,WHITE,cell,1)
        p1_cords = queue_p1.pop(0)
        p2_cords = queue_p2.pop(0)
        if(p1_cords == p2_cords):
            run = False
            time.sleep(2)
        # visit all neighbours of cell 
        x1,y1 = select_random_movement(80)
        x2,y2 = select_random_movement(80)
        p1.move(x1,y1,600,600,dt)
        p2.move(x2,y2,600,600,dt)
        SCREEN.blit(p1.image,p1.image_loc)
        SCREEN.blit(p2.image,p2.image_loc)
        trail_p1.append((p1.image_loc.centerx,p1.image_loc.centery))
        trail_p2.append((p2.image_loc.centerx,p2.image_loc.centery))
        for trail in trail_p1:
            pygame.draw.ellipse(greed_surface,red,(trail[0]-2,trail[1]-2,10,10))
        for trail in trail_p2:
            pygame.draw.ellipse(greed_surface,purple,(trail[0]+2,trail[1]+2,10,10))   
        pygame.display.update()
        if(check(p1.image_loc.center,p2.image_loc.center)):
            time.sleep(2)
            run = False
    # DEQUE THE CELL
    # VISIT ALL NEIGHBOURS CELL 
    # REPEAT UNTILL REACH GOAL NODE
    
def play_k2_random(*args,**kwargs):
    
    if(args[0][0]== 'RANDOM'):
        play_random() 
    elif(args[0][0]== 'DFS'):
        play_dfs() 
    elif(args[0][0]== 'DFS'):
        play_bfs() 
        
    return
