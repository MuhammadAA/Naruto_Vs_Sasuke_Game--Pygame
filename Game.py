#Importing Modules and other running initialization 
import random
import time
import pygame
from pygame.locals import*
pygame.init()
pygame.mixer.init()

#setting up font
Font = pygame.font.SysFont(None,35)

#Setting up window
WINDOWHEIGHT = 400
WINDOWWIDTH = 700
wSurface = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT),0,32)
wSurface.fill((0,0,0))
pygame.display.set_caption('Naruto VS Sasuke')
Map = pygame.image.load("Konoha.png")
Map_Window = pygame.transform.scale(Map,(700,400))
Map_rect = (0,0,700,400)
position = (WINDOWHEIGHT/2, WINDOWWIDTH/1.5)


#Setting Player1 Images, rects, etc.
Player1Image = pygame.image.load("Naruto.png")
Player1_rect = pygame.Rect(400,325,70,70)
Player1Window = pygame.transform.scale(Player1Image,(65,65))
Player1Power = 0
Player1_PowerUp = pygame.image.load("Bijuu_Mode.png")
Player1Window_powerup = pygame.transform.scale(Player1_PowerUp,(65,65))
Player1_Speed = 10
Player1_Spawn = True


#Setting Player2 Images, rects, etc.
Player2Image = pygame.image.load("Sasuke.png")
Player2_rect = pygame.Rect(0,325,70,70) #Player2Image.get_rect() 
Player2Window = pygame.transform.scale(Player2Image,(60,60))
Player2Power = 0
Player2_PowerUp = pygame.image.load("Sasuke Susano.png")
Player2Window_powerup = pygame.transform.scale(Player2_PowerUp,(80,80))
Player2_Speed = 10
Player2_Spawn = True


#Setting up Blue Orbs to spawn around the map
Chakra = pygame.image.load("Blue_orb.png")
chakras = []
for i in range(20):
    chakras.append(pygame.Rect(random.randint(0, WINDOWWIDTH - 10), random.randint(0, WINDOWHEIGHT - 10), 10, 10))
Spawn = False




clock = pygame.time.Clock()

#Player Movement Fluidity
Player1_moveUP = False
Player1_moveDOWN = False
Player1_moveLEFT = False
Player1_moveRIGHT = False


Player2_moveUP = False
Player2_moveDOWN = False
Player2_moveLEFT = False
Player2_moveRIGHT = False





#Creating a Menu at the begining of the Game
def Main_Menu(wSurface):
    pygame.mixer.music.load("Naruto Theme.mp3")
    pygame.mixer.music.play()
    count = 4
    Font = pygame.font.SysFont(None,35)
    FontTWO = pygame.font.SysFont(None,50)
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_s:
                    for i in range(count):
                        wSurface.fill((51,51,51))
                        count -= 1 
                        Timer = str(count)
                        Timer_Text = FontTWO.render(Timer, False,(255,255,255))
                        Timer_TextR = Timer_Text.get_rect()
                        Timer_TextR.centerx = wSurface.get_rect().centerx
                        Timer_TextR.centery = wSurface.get_rect().centery
                        
                        wSurface.blit(Timer_Text,Timer_TextR)
                        time.sleep(1)
                        pygame.display.update()
                    return

        StartGame_str = "Press S to Start Game."
        StartGame_str_text = Font.render(StartGame_str, False, (255,255,255))
        StartGame_str_text_rect = StartGame_str_text.get_rect()
        StartGame_str_text_rect.centerx = wSurface.get_rect().centerx
        StartGame_str_text_rect.centery = wSurface.get_rect().centery
        wSurface.fill((51,51,51))
        wSurface.blit(StartGame_str_text,StartGame_str_text_rect)
        pygame.display.update()

#Running Main Menu before game loop  
Main_Menu(wSurface)

#Creating a menu for pausing
def Paused_Menu(wSurface):
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    return
                if event.key == K_q:
                    pygame.quit()
                    Sys.exit()
        Font = pygame.font.SysFont(None,35)
        Continue_str = "Press Space to Continue the Game."
        Continue_str_text = Font.render(Continue_str, False, (255,255,255))
        Continue_str_text_rect = Continue_str_text.get_rect()
        Continue_str_text_rect.centerx = wSurface.get_rect().centerx
        Continue_str_text_rect.centery = wSurface.get_rect().centery

        quit_str = "Press Q to quit."
        quit_str_text = Font.render(quit_str, False, (255,255,255))
        quit_str_text_rect = quit_str_text.get_rect()
        quit_str_text_rect.centerx = wSurface.get_rect().centerx
        quit_str_text_rect.bottom = +175

        wSurface.fill((51,51,51)) 
        wSurface.blit(quit_str_text, quit_str_text_rect)
        wSurface.blit(Continue_str_text,Continue_str_text_rect)
        pygame.display.update()

    
#creating a screen that pops up when the game ends
def End_Game(wSurface,Player1_Spawn, Player2_Spawn):
    Font = pygame.font.SysFont(None,35)
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    pygame.quit()
                    Sys.quit()

        if Player1_Spawn == False:
            End_str = "Naruto has been killed by Sasuke."
            End_str_text = Font.render(End_str, False, (255,255,255))
            End_str_text_rect = End_str_text.get_rect()
            End_str_text_rect.centerx = wSurface.get_rect().centerx
            End_str_text_rect.centery = wSurface.get_rect().centery

        elif Player2_Spawn == False:
            End_str = "Sasuke has been killed by Naruto."
            End_str_text = Font.render(End_str, False, (255,255,255))
            End_str_text_rect = End_str_text.get_rect()
            End_str_text_rect.centerx = wSurface.get_rect().centerx
            End_str_text_rect.centery = wSurface.get_rect().centery
    
        wSurface.fill((51,51,51))
        wSurface.blit(End_str_text,End_str_text_rect)
        pygame.display.update()
        


#Game Loop
keep_going = True	
while keep_going == True:	
    clock.tick(30)		
    for ev in pygame.event.get():	
        if ev.type==QUIT:		
            keep_going= False
            pygame.quit()
            sys.exit()

        
        if ev.type == KEYDOWN:
            if ev.key == K_ESCAPE:
                Paused_Menu(wSurface)
    
        
        # Player Moving
        if ev.type == KEYDOWN:
            if ev.key == K_UP:
                Player1_moveUP = True

            if ev.key == K_LEFT:
                Player1_moveLEFT = True

            if ev.key == K_DOWN:
                Player1_moveDOWN = True

            if ev.key == K_RIGHT:
                Player1_moveRIGHT = True

            if ev.key == K_w:
                Player2_moveUP = True

            if ev.key == K_a:
                Player2_moveLEFT = True

            if ev.key == K_s:
                Player2_moveDOWN = True
            
            if ev.key == K_d:
                Player2_moveRIGHT = True

            
                
        if ev.type == KEYUP:
            if ev.key == K_UP:
                Player1_moveUP = False
            elif ev.key == K_LEFT:
                Player1_moveLEFT = False
            elif ev.key == K_DOWN:
                Player1_moveDOWN = False
            elif ev.key == K_RIGHT:
                Player1_moveRIGHT = False

        if ev.type == KEYUP:
            if ev.key == K_w:
                Player2_moveUP = False

            elif ev.key == K_a:
                Player2_moveLEFT = False

            elif ev.key == K_s:
                Player2_moveDOWN = False

            elif ev.key == K_d:
                Player2_moveRIGHT = False



    if Player1_moveUP == True and Player1_rect.top >0:
        Player1_rect.top-= Player1_Speed

    elif Player1_moveLEFT == True and Player1_rect.left>0:
        Player1_rect.left-= Player1_Speed

    elif Player1_moveDOWN == True and Player1_rect.top < WINDOWHEIGHT - 65:
        Player1_rect.top+= Player1_Speed

    elif Player1_moveRIGHT == True and Player1_rect.left < WINDOWWIDTH - 60:
        Player1_rect.left += Player1_Speed


    if Player2_moveUP == True and Player2_rect.top >0:
        Player2_rect.top -= Player2_Speed

    elif Player2_moveLEFT == True and Player2_rect.left >0:
        Player2_rect.left -= Player2_Speed

    elif Player2_moveDOWN == True and Player2_rect.top < WINDOWHEIGHT - 70: 
        Player2_rect.top += Player2_Speed

    elif Player2_moveRIGHT == True and Player2_rect.left < WINDOWWIDTH - 60:
        Player2_rect.left += Player2_Speed
    
    
#Drawing map, Blitting Characters, and Blue Orbs
    wSurface.fill((0,0,0))
    
    wSurface.blit(Map_Window,Map_rect)
    if Spawn == False:
        wSurface.blit(Player1Window,Player1_rect)
        wSurface.blit(Player2Window,Player2_rect)
        
    if Spawn == True:
        if Player1Power == 75:
            Player1_Speed = 8
            wSurface.blit(Player1Window_powerup,Player1_rect)
            if Player2_Spawn == True:
                wSurface.blit(Player2Window,Player2_rect)
                

        if Player2Power == 75:
            Player2_Speed = 8
            wSurface.blit(Player2Window_powerup,Player2_rect)
            if Player1_Spawn == True:
                wSurface.blit(Player1Window,Player1_rect)





    #Draws Blue Orbs
    for C in chakras:
        ChakraWindow = pygame.transform.scale(Chakra,(10,10))
        wSurface.blit(ChakraWindow,C)


    #If one Player has 75 points it makes Spawn True
    if Player1Power >= 75 or Player2Power >= 75:
        Spawn = True



    #Checks if characters collide after sprite change
    if Player1Power >= 75:
        if Player1_rect.colliderect(Player2_rect):
            Player2_Spawn = False
            End_Game(wSurface,Player1_Spawn, Player2_Spawn)

    if Player2Power >= 75:
        if Player2_rect.colliderect(Player1_rect):
            Player1_Spawn = False
            End_Game(wSurface,Player1_Spawn, Player2_Spawn)



    #If Spawn is true it removes blue orbs
    for items in chakras[:]:
        if Spawn == True:
            for items in chakras:
                chakras.remove(items)
                break


    #Dectects Collision between player and Blue orb, and it adds it to their power
        if Player1_rect.colliderect(items):
            chakras.remove(items)
            Player1Power += 1
            print Player1Power
           
        elif Player2_rect.colliderect(items):
            chakras.remove(items)
            Player2Power += 1
            print Player2Power




    #spawns Blue orbs if there are less than 20 blue orbs on the screen
    if Spawn == False:
        if len(chakras) < 20:
            chakras.append(pygame.Rect(random.randint(0, WINDOWWIDTH - 10), random.randint(0, WINDOWHEIGHT - 10), 10, 10))
        

            
        
             


   


    pygame.display.update()



pygame.quit()