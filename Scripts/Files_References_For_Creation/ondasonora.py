import pygame
import time
import math
import random

canvas_width=1308
canvas_height=720
canvas_s=1004

rojo=pygame.Color(255,0,0)
verde=pygame.Color(0,255,0)
azul=pygame.Color(0,0,255)
amarillo=pygame.Color(255,255,0,0)
#marron=pygame.Color(85,65,0)
##morado=pygame.Color(255,0,255)
naranja=pygame.Color(255,128,0)
lin=pygame.Color(255,255,255)
background_color=pygame.Color(0,0,0)

pygame.init()
# initialization of font module and creating a font to draw with
pygame.font.init()
fontdir=pygame.font.match_font('TimesNewRoman',False,False)
myfont = pygame.font.Font(fontdir,60)
pygame.display.set_caption("Monitor Signos Vitales")

screen=pygame.display.set_mode((canvas_width,canvas_height))
screen.fill(background_color)

surface=pygame.Surface((canvas_width,canvas_s))
surface.fill(background_color)

# creating the random list and their corresponding surfaces
random_list=[random.randrange(0,1000) for x in range(5)]
text_list=[myfont.render(str(x),True,lin) for x in random_list]

running=True
while running:
    pos=(1150,0)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    surface.fill(background_color)

    for text in text_list:
        surface.blit(text,pos)
        pos=(pos[0],pos[1]+180)

    pygame.draw.line(surface, lin, (0, 90), (1004, 90))
    pygame.draw.line(surface, lin, (0, 180), (1004, 180))
    pygame.draw.line(surface, lin, (0, 270), (1004, 270))
    pygame.draw.line(surface, lin, (0, 360), (1004, 360))
    pygame.draw.line(surface, lin, (0, 450), (1004, 450))
##    pygame.draw.line(surface, lin, (0, 540), (1004, 540))
##    pygame.draw.line(surface, lin, (0, 630), (1004, 630))
    pygame.draw.line(surface, lin, (1004, 0), (1004, 720))
    pygame.draw.line(surface, lin, (1004, 180), (1308, 180))
    pygame.draw.line(surface, lin, (1004, 360), (1308, 360))
##    pygame.draw.line(surface, lin, (1004, 540), (1308, 540))

    frecuency=13;frecuencyi=26;frecuency0=8;frecuency1=13;frecuency2=4;frecuency3=7.9;frecuency4=1.3;frecuency5=3
    amplitude=30
    speed=1.8
    for x0 in range(0,canvas_s):
        y0=int((canvas_height/2)+amplitude*math.sin(frecuency*((float(x0)/canvas_s)*(2*math.pi)+(speed*time.time()))+270)-270)
        surface.set_at((x0,y0),amarillo)
    for x0 in range(0,canvas_s):
        y0=int((canvas_height/2)+amplitude*math.sin(frecuencyi*((float(x0)/canvas_s)*(2*math.pi)+(speed*time.time()))+270)-270)
        surface.set_at((x0,y0),amarillo)
    for x1 in range(0,canvas_s):
        y1=int((canvas_height/2)+amplitude*math.sin(frecuency0*((float(x1)/canvas_s)*(2*math.pi)+(speed*time.time()))+180)-180)
        surface.set_at((x1,y1),verde)
    for x1 in range(0,canvas_s):
        y1=int((canvas_height/2)+amplitude*math.sin(frecuency1*((float(x1)/canvas_s)*(2*math.pi)+(speed*time.time()))+180)-180)
        surface.set_at((x1,y1),verde)
##    for x2 in range(0,canvas_s):
##        y2=int((canvas_height/2)+amplitude*math.sin(frecuency2*((float(x2)/canvas_s)*(2*math.pi)+(speed*time.time()))+90)-90)
##        surface.set_at((x2,y2),naranja)
    for x3 in range(0,canvas_s):
        y3=int((canvas_height/2)+amplitude*math.sin(frecuency2*((float(x3)/canvas_s)*(2*math.pi)+(speed*time.time()))))
        surface.set_at((x3,y3),azul)
    for x3 in range(0,canvas_s):
        y3=int((canvas_height/2)+amplitude*math.sin(frecuency3*((float(x3)/canvas_s)*(2*math.pi)+(speed*time.time()))))
        surface.set_at((x3,y3),azul)
    for x4 in range(0,canvas_s):
        y4=int((canvas_height/2)+amplitude*math.sin(frecuency4*((float(x4)/canvas_s)*(2*math.pi)+(speed*time.time()))-90)+90)
        surface.set_at((x4,y4),rojo)
    for x4 in range(0,canvas_s):
        y4=int((canvas_height/2)+amplitude*math.sin(frecuency5*((float(x4)/canvas_s)*(2*math.pi)+(speed*time.time()))-90)+90)
        surface.set_at((x4,y4),rojo)
##    for x5 in range(0,canvas_s):
##        y5=int((canvas_height/2)+amplitude*math.sin(frecuency4*((float(x5)/canvas_s)*(2*math.pi)+(speed*time.time()))-180)+180)
##        surface.set_at((x5,y5),marron)
##    for x6 in range(0,canvas_s):
##        y6=int((canvas_height/2)+amplitude*math.sin(frecuency5*((float(x6)/canvas_s)*(2*math.pi)+(speed*time.time()))-270)+270)
##        surface.set_at((x6,y6),morado)

    screen.blit(surface,(0,0))
    pygame.display.flip()
