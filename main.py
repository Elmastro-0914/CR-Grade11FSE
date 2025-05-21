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
grid = [[1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]
def moveInGrid(dir, w, h):
    if dir == "right":
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if j == w-1:
                        grid[i][0] = 1
                    else:
                        grid[i][j+1] = 1
                    return
    if dir == "left":
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if j == 0:
                        grid[i][w-1] = 1
                    else:
                        grid[i][j-1] = 1
                    return
    if dir == "down":
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if i == h-1:
                        grid[0][j] = 1
                    else:
                        grid[i+1][j] = 1
                    return
    if dir == "up":
        for i in range(h):
            for j in range(h):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if i == 0:
                        grid[h-1][j] = 1
                    else:
                        grid[i-1][j] = 1
                    return
        

while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
        if evt.type == KEYDOWN:
            if evt.key == K_d:
                moveInGrid("right", 8, 8)
            if evt.key == K_a:
                moveInGrid("left", 8, 8)
            if evt.key == K_s:
                moveInGrid("down", 8, 8)
            if evt.key == K_w:
                moveInGrid("up", 8, 8)
                          
                          
                          
                          
                          
                            
        
                
                     
            
        
        
        
        
    
                    
    
    screen.fill(BLACK)
    for i in range(9):
        draw.line(screen, GREEN, (150, i*100), (665, i*100), 2)
    for i in range(9):
        draw.line(screen, GREEN, (i*65+150, 0), (i*65+150, 700), 2)
    
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 1:
                draw.rect(screen, BLUE, (j*65+150, i*100+150, 50, 50))
                    
    
                       
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()
      
    myClock.tick(60)
    display.flip()
            
quit()
