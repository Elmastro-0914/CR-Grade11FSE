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

# Main screen boxes
PlayBox = Rect(500, 330, 400, 100)
HowToPlayBox = Rect(500, 455, 400, 100)
SettingsBox = Rect(500, 580, 400, 100)
draw.rect(screen, GREEN, PlayBox)
draw.rect(screen, BLUE, HowToPlayBox)
draw.rect(screen, GREY, SettingsBox)

# Card Shown
continueBox = Rect(1175, 575, 200, 100)
screenNum = 1

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
    
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()
    
    if screenNum == 1:
        screen.fill(BLACK)
        draw.rect(screen, GREEN, PlayBox)
        draw.rect(screen, BLUE, HowToPlayBox)
        draw.rect(screen, GREY, SettingsBox)
        if PlayBox.collidepoint(mx, my) and mb[0]:
            screenNum = 2
    elif screenNum == 2:
        screen.fill(BLACK)
        draw.line(screen, RED, (695, 0), (695, 695), 10)
        draw.rect(screen, GREEN, continueBox)
        if continueBox.collidepoint(mx, my) and mb[0]:
            screenNum = 3
    elif screenNum == 3:
        screen.fill(BLACK)
        #Left Grid 
        for i in range(9):
            draw.line(screen, GREEN, (360, i*70+70), (640, i*70+70), 2)
        for i in range(5):
            draw.line(screen, GREEN, (i*70+360, 70), (i*70+360, 630), 2)

        #Right Grid
        for i in range(9):
            draw.line(screen, GREEN, (745, i*70+70), (1025, i*70+70), 2)
        for i in range(5):
            draw.line(screen, GREEN, (i*70+745, 70), (i*70+745, 630), 2)
        
        #Blue player
        for i in range(8):
            for j in range(4):
                if grid1[i][j] == 1:
                    # print(i, j)
                    draw.rect(screen, BLUE, (j*70+360, i*70+70, 70, 70))

        #Red Player       
        for i in range(8):
            for j in range(4):
                if grid2[i][j] == 1:
                    # print(i, j)
                    draw.rect(screen, RED, (j*70+745, i*70+70, 70, 70)) 
                        
        #Blue cards area
        draw.rect(screen,BLUE,(0,147,183,406),2)
        draw.line(screen,WHITE,(40,150),(40,550))
        for i in range(10):
            draw.rect(screen,WHITE,(0,150,40,i*40+40),2)
        for i in range(4):
            draw.rect(screen,WHITE,(40,150,140,i*100+100),2)

        #Red cards area
        draw.rect(screen,RED,(1217,147,183,406),2)
        draw.line(screen,WHITE,(1360,150),(1360,550))
        for i in range(10):
            draw.rect(screen,WHITE,(1360,150,1360,i*40+40),2)
        for i in range(4):
            draw.rect(screen,WHITE,(1220,150,140,i*100+100),2)




    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()
      
    myClock.tick(60)
    display.flip()
            
quit()
