import pygame
import sys

def Launch_game():
    pygame.init()
    global screen
    global shooter
    
    screen=pygame.display.set_mode((800,600))

    logo=pygame.image.load("logo.png")
    bg=pygame.image.load("bg.jpg")
    shooter=pygame.image.load("shooter.png")
    
    pygame.display.set_caption("Space Shooters")
    pygame.display.set_icon(logo)

    #Shooter movement
    x=370
    y=480
    nx=0
    ny=0

    #running
    run=True
    while run:
        screen.blit(bg,(0,0))#draw or update the background
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                pygame.quit()
                sys.exit(0)

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    nx=-1
                elif event.key==pygame.K_RIGHT:
                    nx=1
                elif event.key==pygame.K_UP:
                    ny=-1
                elif event.key==pygame.K_DOWN:
                    ny=1
                    
            if event.type==pygame.KEYUP:
                nx=0
                ny=0

        x+=nx
        y+=ny
        if x<=0:
            x=0
        elif x>=650:
            x=650
        if y<=0:
            y=0
        elif y>=500:
            y=500
        screen.blit(shooter,(x,y))

        pygame.display.update()
          
#
Launch_game()

