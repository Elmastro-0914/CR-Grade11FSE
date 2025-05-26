from pygame import*

width,height=1400,700
screen=display.set_mode((width,height))
RED=(255,0,0)
GREY=(127,127,127)
BLACK=(0,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)
YELLOW=(255,255,0)
WHITE=(255,255,255)
myClock=time.Clock()
running=True
grid1 = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [1, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]

grid2 = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]

def moveInGrid(dir, w, h, player):
    if player == 1:
        if dir == "right":
            for i in range(h):
                for j in range(w):
                    if grid1[i][j] == 1:
                        grid1[i][j] = 0
                        if j == w-1:
                            grid1[i][0] = 1
                        else:
                            grid1[i][j+1] = 1
                        return
        if dir == "left":
            for i in range(h):
                for j in range(w):
                    if grid1[i][j] == 1:
                        grid1[i][j] = 0
                        if j == 0:
                            grid1[i][w-1] = 1
                        else:
                            grid1[i][j-1] = 1
                        return
        if dir == "down":
            for i in range(h):
                for j in range(w):
                    if grid1[i][j] == 1:
                        grid1[i][j] = 0
                        if i == h-1:
                            grid1[0][j] = 1
                        else:
                            grid1[i+1][j] = 1
                        return
        if dir == "up":
            for i in range(h):
                for j in range(w):
                    if grid1[i][j] == 1:
                        grid1[i][j] = 0
                        print(i)
                        if i == 0:
                            grid1[h-1][j] = 1
                        else:
                            grid1[i-1][j] = 1
                        return
    elif player == 2:
        if dir == "right":
            for i in range(h):
                for j in range(w):
                    if grid2[i][j] == 1:
                        grid2[i][j] = 0
                        if j == w-1:
                            grid2[i][0] = 1
                        else:
                            grid2[i][j+1] = 1
                        return
        if dir == "left":
            for i in range(h):
                for j in range(w):
                    if grid2[i][j] == 1:
                        grid2[i][j] = 0
                        if j == 0:
                            grid2[i][w-1] = 1
                        else:
                            grid2[i][j-1] = 1
                        return
        if dir == "down":
            for i in range(h):
                for j in range(w):
                    if grid2[i][j] == 1:
                        grid2[i][j] = 0
                        if i == h-1:
                            grid2[0][j] = 1
                        else:
                            grid2[i+1][j] = 1
                        return
        if dir == "up":
            for i in range(h):
                for j in range(w):
                    if grid2[i][j] == 1:
                        grid2[i][j] = 0
                        print(i)
                        if i == 0:
                            grid2[h-1][j] = 1
                        else:
                            grid2[i-1][j] = 1
                        return

while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
        if evt.type == KEYDOWN:
            if evt.key == K_d:
                moveInGrid("right", 4, 8, 1)
            if evt.key == K_a:
                moveInGrid("left", 4, 8, 1)
            if evt.key == K_s:
                moveInGrid("down", 4, 8, 1)
            if evt.key == K_w:
                moveInGrid("up", 4, 8, 1)
            if evt.key == K_l:
                moveInGrid("right", 4, 8, 2)
            if evt.key == K_j:
                moveInGrid("left", 4, 8, 2)
            if evt.key == K_k:
                moveInGrid("down", 4, 8, 2)
            if evt.key == K_i:
                moveInGrid("up", 4, 8, 2)
                          
                          
                          
                          
                          
                            
        
                
                     
            
        
        
        
        
    
                    
    
    screen.fill(BLACK)
    for i in range(9):
        draw.line(screen, GREEN, (360, i*70+70), (640, i*70+70), 2)
    for i in range(5):
        draw.line(screen, GREEN, (i*70+360, 70), (i*70+360, 630), 2)
    for i in range(9):
        draw.line(screen, GREEN, (745, i*70+70), (1025, i*70+70), 2)
    for i in range(5):
        draw.line(screen, GREEN, (i*70+745, 70), (i*70+745, 630), 2)
    
    for i in range(8):
        for j in range(4):
            if grid1[i][j] == 1:
                # print(i, j)
                draw.rect(screen, BLUE, (j*70+360, i*70+70, 70, 70))
               
    for i in range(8):
        for j in range(4):
            if grid2[i][j] == 1:
                # print(i, j)
                draw.rect(screen, RED, (j*70+745, i*70+70, 70, 70)) 
                    
    
                       
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()
      
    myClock.tick(60)
    display.flip()
            
quit()
