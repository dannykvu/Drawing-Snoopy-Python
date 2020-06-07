#Danny Vu
#3/11/16

title = "Danny Vu: Snoopy"

import sys #this allows us to use the sys library
import pygame # this allows us to use the pygame library
import pygame.gfxdraw
from pygame.locals import * #this allows us to use local events like Key presses or mouse clicks


pygame.init() # this initializes pygame, you have to have this or the rest of the code won't run
window = pygame.display.set_mode((800,600)) #this is the game window (width, height)
pygame.display.set_caption(title)

def CreatedBy(window):
    #change font size below
   basicFont = pygame.font.SysFont("Comic Sans MS", 32)
   #edit the text below
   text = basicFont.render('Created by: Danny Vu ', True, (255,255,255))
   textRect = text.get_rect()
   textRect.x = 800 - textRect.width
   textRect.y = 600 - textRect.height
   window.blit(text,textRect)
   

def drawCharacter(window):
    window.fill((255,153,0)) #this will change the background color
# This will be the house(roof)
    roof = [(140,600),(170,390),(640,390),(690,600)]
    pygame.draw.polygon(window,(255,102,0),roof,0)
    
# This will be the line in the roof
    pygame.draw.line(window,(0,0,0),(210,510),(640,510),5)
    
#Colors for snoopy's bottom half'
    bottomColor = [(350,263),(340,274),(330,286),(320,300),(310,314),(300,338),(300,370),(310,382),(320,390),(330,392),(340,390),(350,390),(360,391),(370,392),(380,389),(390,388),(400,390),(421,400),(430,406),(440,400),(450,388),(460,390),(470,390),(480,390),(480,340),(472,330),(460,351),(462,329),(450,326),(430,328),(426,330),(418,310),(437,310),(455,297),(454,283),(446,259),(420,265),(409,279),(397,263),(350,363)]
    pygame.draw.polygon(window,(255,255,255),bottomColor,0)
    pygame.draw.rect(window,(255,255,255),(350,264,47,96),0)
    
# Color for snoops nose
    noseColor = [(375,126),(367,144),(365,165),(375,207),(390,230),(410,222),(430,226),(480,226),(490,223),(500,216),(510,209),(522,189),(524,169),(505,135),(488,117),(470,104),(460,100),(450,96),(440,93),(424,91),(413,116),(390,129),(375,126)]
    pygame.draw.polygon(window,(255,255,255),noseColor,0)

# Color for snoopys hat
    hatColor = [(366,51),(350,52),(340,54),(330,57),(320,60),(310,65),(300,71),(290,79),(280,88),(270,103),(260,137),(270,180),(280,190),(290,200),(300,208),(310,213),(320,217),(330,222),(340,226),(350,226),(360,227),(380,227),(390,229),(374,203),(367,181),(364,158),(368,141),(373,127),(360,121),(348,106),((345,98),(345,82),(353,63),(366,51))]
    pygame.draw.polygon(window,(46, 184, 46),hatColor,0)
    
# Color pokadots
    spot1 = [(306,323),(313,329),(317,338),(317,353),(312,358),(304,354),(296,356),(299,350),(300,344),(306,323)]
    pygame.draw.polygon(window,(0,0,0),spot1,0)
    spot2 = [(298,363),(290,373),(302,373),(301,371),(298,363)]
    pygame.draw.polygon(window,(0,0,0),spot2,0)
# this will color snoops band on the goggles
    bandColor = [(346,99),(325,117),(319,110),(308,126),(302,143),(304,136),(304,149),(313,153),(325,151),(345,145),(340,139),(360,121),(350,111),(346,99)]
    pygame.draw.polygon(window,(102,51,0),bandColor,0)
    pygame.draw.rect(window,(102,51,0),(345,109,10,10),0)

# this will color snoop's scarf
    scarColor = [(350,233),(343,228),(300,231),(266,230),(255,232),(242,237),(216,249),(214,251),(207,252),(204,254),(185,257),(162,257),(140,251),(127,245),(142,262),(113,262),(140,271),(122,281),(157,282),(192,284),(237,281),(278,271),(350,264),(350,233)]
    scar2Color = [(298,232),(294,228),(250,209),(236,201),(215,197),(169,199),(149,190),(128,200),(150,201),(122,220),(140,230),(122,241),(300,241)]
    pygame.draw.polygon(window,(204,0,0),scarColor,0)
    pygame.draw.polygon(window,(204,0,0),scar2Color,0)
    
# this will color snoopys tail
    tailColor = [(298,363),(288,374),(276,375),(270,370),(250,370),(234,378),(223,387),(220,391),(221,398),(223,397),(254,385),(272,386),(282,391),(306,392),(321,388),(309,381),(302,374),(275,375)]
    pygame.draw.polygon(window,(255,255,255),tailColor,0)
    
# This will create the bottom half of snoopy
    curve = [(320,300),(300,330),(275,385),(315,400),(380,390)]
    Legs1 = [(380,390),(410,385),(425,405)]
    legs2 = [(425,405),(435,410),(450,390)]
    legs3 = [(460,340),(470,320),(430,330)]
    legs4 = [(415,360),(395,350),(370,370)]
    legs5 = [(480,340),(475,315),(465,340)]
    pygame.gfxdraw.bezier(window,curve,50,(0,0,0))
    pygame.draw.line(window,(0,0,0),(320,300),(350,260),2)
    pygame.gfxdraw.bezier(window,Legs1,50,(0,0,0))
    pygame.gfxdraw.bezier(window,legs2,50,(0,0,0))
    pygame.draw.line(window,(0,0,0),(450,390),(460,340),2)
    pygame.gfxdraw.bezier(window,legs3,50,(0,0,0))
    #pygame.draw.line(window,(0,0,0),(455,325),(435,245),2)
    pygame.draw.line(window,(0,0,0),(430,330),(415,360),2)
    pygame.gfxdraw.bezier(window,legs4,50,(0,0,0))
    pygame.draw.line(window,(0,0,0),(455,325),(435,355),2)# lines on legs
    pygame.draw.line(window,(0,0,0),(455,350),(435,375),2)#lines on legs
    pygame.draw.line(window,(0,0,0),(480,390),(480,338),1)# 2nd leg
    pygame.gfxdraw.bezier(window,legs5,50,(0,0,0))
    pygame.draw.line(window,(0,0,0),(465,340),(450,370),2)
    pygame.draw.line(window,(0,0,0),(395,260),(400,270),2)
    pygame.draw.line(window,(0,0,0),(480,390),(445,390),2)
    belly = [(415,310),(435,315),(420,350)]
    pygame.gfxdraw.bezier(window,belly,50,(0,0,0))
    
# This will create snoopy's arms (1)
    pygame.draw.line(window,(0,0,0),(380,270),(410,280),1)
    finger1 = [(410,280),(425,250),(430,280)]
    pygame.gfxdraw.bezier(window,finger1,50,(0,0,0))
    finger2 = [(430,280),(460,285),(430,295)]
    pygame.gfxdraw.bezier(window,finger2,50,(0,0,0))
    finger3 = [(430,295),(445,320),(420,310)]
    pygame.gfxdraw.bezier(window,finger3,50,(0,0,0))
    bottomArm = [(420,310),(410,315),(340,310)]
    pygame.gfxdraw.bezier(window,bottomArm,50,(0,0,0))
    
# this will create snoopy's second arm(2)
    finger4 = [(440,260),(460,265),(430,280)]
    pygame.gfxdraw.bezier(window,finger4,50,(0,0,0))
    finger5 = [(430,280),(470,280),(445,290)]
    pygame.gfxdraw.bezier(window,finger5,50,(0,0,0))
    finger6 = [(448,290),(470,300),(435,310)]
    pygame.gfxdraw.bezier(window,finger6,50,(0,0,0))
    pygame.draw.line(window,(0,0,0),(425,265),(439,260),1)
# googles of snoopy
    band = [(320,110),(275,170),(345,145)]
    #google1 = [(400,50),(360,58),(350,85),(360,120),(385,130),(420,90)]
    pygame.draw.circle(window,(102,51,0),(385,90),40,0)
    pygame.draw.circle(window,(102,51,0),(387,86),40,0)
    pygame.draw.circle(window,(102,51,0),(412,67),30,0)
    pygame.draw.circle(window,(0,0,0),(385,88),30,0)
    pygame.draw.circle(window,(0,0,0),(428,58),15,0)
    pygame.draw.circle(window,(0,0,0),(428,68),15,0)
    pygame.draw.circle(window,(0,0,0),(422,55),15,0)
    pygame.draw.line(window,(0,0,0),(325,115),(350,95),2)
    pygame.draw.line(window,(0,0,0),(340,140),(362,118),2)
    pygame.draw.line(window,(0,0,0),(320,110),(345,145),2)
    #pygame.draw.arc(window,(0,0,0),()
    pygame.gfxdraw.bezier(window,band,50,(0,0,0))
    #pygame.gfxdraw.bezier(window,google1,50,(0,0,0))
    pygame.draw.arc(window,(102,51,0),(350,45,75,85),1.4,6.28,2)
    pygame.draw.arc(window,(102,51,0),(385,40,50,55),5.233,8.5,2)
    goggle2 = [(420,40),(405,75),(435,80)]
    pygame.gfxdraw.bezier(window,goggle2,50,(0,0,0))
# extra cirlce for snoopy's goggle
    pygame.draw.circle(window,(0,0,0),(422,60),18,0)
    pygame.draw.circle(window,(0,0,0),(424,65),18,0)
# snoopys helmet
    pygame.draw.arc(window,(0,0,0),(260,50,230,180),1.60,4.71,2)
# snoopys mouth
    pygame.draw.arc(window,(0,0,0),(300,320,20,40),3.925,6.48,3)
    
#snoopy's nose
    nose = [(420,90),(500,100),(525,170)]
    bottomNose = [(525,185),(510,220),(480,225)]
    throat = [(430,225),(410,220),(390,230)]
    hat = [(390,230),(350,175),(375,125)]
    pygame.gfxdraw.bezier(window,nose,50,(0,0,0))
    pygame.gfxdraw.bezier(window,bottomNose,50,(0,0,0))
    pygame.draw.line(window,(0,0,0),(480,225),(430,225),2)
    pygame.draw.circle(window,(0,0,0),(525,180),10,0)
    pygame.gfxdraw.bezier(window,throat,50,(0,0,0))
    pygame.gfxdraw.bezier(window,hat,50,(0,0,0))
    
# This will be the scarf on snoopys neck
    pygame.draw.rect(window,(204,0,0),(350,230,45,35),0)
    pygame.draw.line(window,(204,0,0),(360,230),(300,230),2)
    scar1 = [(300,230),(255,225),(235,240)]
    scarPart2 = [(235,240),(180,270),(140,250)]
    pygame.gfxdraw.bezier(window,scar1,50,(204,0,0))
    pygame.gfxdraw.bezier(window,scarPart2,50,(204,0,0))
#trianglees at the end of the scarf
    pygame.draw.line(window,(204,0,0),(140,250),(120,240),2)
    pygame.draw.line(window,(204,0,0),(120,240),(140,260),2)
    pygame.draw.line(window,(204,0,0),(140,260),(110,260),2)
    pygame.draw.line(window,(204,0,0),(110,260),(140,270),2)
    pygame.draw.line(window,(204,0,0),(140,270),(120,280),2)
    pygame.draw.line(window,(204,0,0),(120,280),(150,280),2)
    scarPart3 = [(150,280),(220,290),(280,270)]
    pygame.gfxdraw.bezier(window,scarPart3,50,(204,0,0))
    pygame.draw.line(window,(204,0,0),(280,270),(345,265),1)
# 2nd scarf
    pygame.draw.line(window,(204,0,0),(300,230),(250,210),1)
    scar2 = [(250,210),(230,190),(170,200)]
    pygame.gfxdraw.bezier(window,scar2,50,(204,0,0))
    pygame.draw.line(window,(204,0,0),(170,200),(150,190),1)
# 2nd triangle 
    pygame.draw.line(window,(204,0,0),(150,190),(125,200),1) #fix
    pygame.draw.line(window,(204,0,0),(125,200),(150,200),1)
    pygame.draw.line(window,(204,0,0),(150,200),(120,220),1)
    pygame.draw.line(window,(204,0,0),(120,220),(140,230),1)
    pygame.draw.line(window,(204,0,0),(140,230),(120,240),1)
    pygame.draw.line(window,(204,0,0),(120,240),(150,240),1)
# line that separates the scarf
    pygame.draw.line(window,(204,0,0),(150,240),(235,240),1)
      

# will create snoopy's tail
    tail = [(298,362),(285,385),(270,370)]
    pygame.gfxdraw.bezier(window,tail,50,(0,0,0))
    tail2 = [(270,370),(245,365),(220,390)]
    pygame.gfxdraw.bezier(window,tail2,50,(0,0,0))
    tail3 = [(220,390),(215,405),(240,390)]
    pygame.gfxdraw.bezier(window,tail3,50,(0,0,0))
    tail4 = [(240,390),(265,380),(280,390)]
    pygame.gfxdraw.bezier(window,tail4,50,(0,0,0))
    tail5 = [(280,390),(298,395),(323,389)]
    pygame.gfxdraw.bezier(window,tail5,50,(0,0,0))
    
#football
    pygame.draw.ellipse(window,(102,51,0),(442,246,40,61),0)
    pygame.draw.line(window,(255,255,255),(461,261),(461,292),2)
    pygame.draw.line(window,(255,255,255),(453,261),(472,261),2)
    pygame.draw.line(window,(255,255,255),(453,292),(472,292),2)
    pygame.draw.line(window,(255,255,255),(453,276),(472,276),2)    
    
    """
   1 pygame.draw.line(window,(r,g,b),(x1,y1),(x2,y2),wt)
    
   2 pygame.draw.circle(window,(r,g,b),(cX,cY),rad,wt/fill)
    
   3 pygame.draw.rect(window,(r,g,b),(tlX,tlY,width,height),wt/fill)
    
   4 pygame.draw.ellipse(window,(r,g,b),(tlX,tlY,width,height),wt/fill)
    
   5 PtsList = [(x1,y1),(x2,y2),(x3,y3)]
    pygame.draw.polygon(window,(r,g,b),PtsList,wt/fill)
    
   6 #you cannot fill lines, if you want to fill use the polygon method
    PtsList = [(x1,y1),(x2,y2),(x3,y3),(x4,y4),(x5,y5)]
    pygame.draw.lines(window,(r,g,b),True/False,PtsList,wt)
    
    #pygame.draw.arc(window,(102,51,0),(395,50,50,50),5.233,8.373,2)
    
   7 pygame.draw.arc(window,(r,g,b),(tlX,tlY,width,height),sA,eA,wt) #sA < eA, sA & eA have to be between 0-6.28
    """
    
 


#---Game Loop---#
done = False
while not done: 
    for event in pygame.event.get(): #a loop that continually goes through all of the events
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE): #close if I press escape or click the X
            done = True #this tells the loop to stop!
   
  
    drawCharacter(window)
    CreatedBy(window)
    pygame.display.flip() #this is to update the whole screen
    
pygame.quit() #this quits pygame, it is the exact opposite of init()
sys.exit() #this closes everything



