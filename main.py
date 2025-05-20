from pygame import*

width,height=800,600
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

while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
                       
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()
      
    myClock.tick(60)
    display.flip()
            
quit()
