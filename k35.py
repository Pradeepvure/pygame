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

def play_random(player_identifier):
    pygame.init()
    SCREEN = pygame.display.set_mode(SIZE)
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)
    sprites = []
    np=2     
    p1= player(0,0,"red.png",80)
    p2= player(WIDTH - 80,HEIGHT - 80,"purple.png",80)
    p1_not_won = 1 
    p2_not_one = 1
    sprites.append(p1)
    sprites.append(p2)
    trail_p1 = []
    trail_p1.append((p1.image_loc.centerx,p1.image_loc.centery))
    trail_p2 = []
    trail_p1.append((p2.image_loc.centerx,p2.image_loc.centery))
    trail_p3=[]
    trail_p4=[]
    points = []
    if(player_identifier == '3P' or player_identifier=='4P'):
        np =3
        p3= player(WIDTH - 80 ,0,"yellow.png",80)
        sprites.append(p3)
        p3_not_one = 1
        trail_p3.append((p3.image_loc.centerx,p3.image_loc.centery))
        
    if(player_identifier == '4P'):
        np = 4
        p4 = player(0,HEIGHT-80, "marine.png",80)
        p4_not_one=1
        trail_p4.append((p4.image_loc.centerx,p4.image_loc.centery))
    run = True
    red = (255,0,0)
    purple  = (128,0,128)
    yellow = (0,255,255)
    marine = (50,50,255)
    colors = [red,purple,yellow,marine]
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
        p1.move(x1,y1,600,600,dt,p1_not_won)
        p2.move(x2,y2,600,600,dt,p2_not_one)
        SCREEN.blit(p1.image,p1.image_loc)
        SCREEN.blit(p2.image,p2.image_loc)
        trail_p1.append((p1.image_loc.centerx,p1.image_loc.centery))
        trail_p2.append((p2.image_loc.centerx,p2.image_loc.centery))
        for trail in trail_p1:
            pygame.draw.ellipse(greed_surface,red,(trail[0]-5,trail[1]-5,10,10))
        for trail in trail_p2:
            pygame.draw.ellipse(greed_surface,purple,(trail[0]+5,trail[1]+5,10,10))  
        
        if(np==3 or np ==4):
            x3,y3 = select_random_movement(80)
            p3.move(x3,y3,600,600,dt,p3_not_one)
            SCREEN.blit(p3.image,p3.image_loc)
            trail_p3.append((p3.image_loc.centerx,p3.image_loc.centery))
            for trail in trail_p3:
                pygame.draw.ellipse(greed_surface,yellow,(trail[0]-5,trail[1]+5,10,10))  
        
        if(np==4):
            x4,y4 = select_random_movement(80)
            p4.move(x4,y4,600,600,dt,p4_not_one)
            SCREEN.blit(p4.image,p4.image_loc)
            trail_p4.append((p4.image_loc.centerx,p4.image_loc.centery))
            for trail in trail_p4:
                pygame.draw.ellipse(greed_surface,marine,(trail[0]+5,trail[1]-5,10,10))  
        
        
        pygame.display.update()
            
        if(check(p1.image_loc.center,p2.image_loc.center)):
            p1_not_won = 0
            p2_not_one = 0
        if(np==3 or np ==4):
            if(check(p1.image_loc.center,p3.image_loc.center)):
                p1_not_won = 0
                p3_not_one = 0
            if(check(p2.image_loc.center,p3.image_loc.center)):
                p3_not_one = 0
                p2_not_one = 0
        if(np==4):
            if(check(p1.image_loc.center,p4.image_loc.center)):
                p1_not_won = 0
                p4_not_one = 0
            if(check(p2.image_loc.center,p4.image_loc.center)):
                p4_not_one = 0
                p2_not_one = 0
            if(check(p4.image_loc.center,p3.image_loc.center)):
                p3_not_one = 0
                p4_not_one = 0
        if(np<3):
            if(p1_not_won  + p2_not_one == 0):
                time.sleep(2)
                run = False
        elif(np==3):
            if(p1_not_won  + p2_not_one + p3_not_one  == 0):
                time.sleep(2)
                run = False
        else: 
            if(p1_not_won  + p2_not_one + p3_not_one + p4_not_one == 0):
                time.sleep(2)
                run = False
          
def play_k35_random(*args,**kwargs):
    print(args)
    if(args[1][0]== 'RANDOM'):
        play_random(args[0][0]) 
    elif(args[1][0]== 'BFS'):
        play_random(args[0][0])    
    else:
        play_random(args[0][0])   
    return