import os,sys,termios,time,random,tty
from takeinput import *
from background import *
from character import *
from coin import *
from obstacle import *
from firearm import *

from colorama import Fore,Back,Style




def draw():
    print("\033[0;0f",end="")
    
    global start

    #TO DECIDE WHEN TO MOVE THE SCREEN
    end=time.time()
    if end-start >= board.screenmovetime:
        start=time.time()
        board.shiftthescreen()
    
    #FOR CHECKING COLLISION    
    coins.checkcollison()
    beam.beamcollison()
    speedup.powerup_collison()
    beam.bulletcollison(bullet)
        
    #FOR PRINTING STAT OF GAME
    if board.pointertomygame()<board.lengthofmygame()-board.size:
        if  din.shieldischarged is True:
            print("SCORE: "+str(din.score)+20*" "+"SHEILD IS READY: Y"+20*" "+"LIVES: "+str(din.HP) )
        else:
            print("SCORE: "+str(din.score)+20*" "+"SHEILD IS READY: N"+20*" "+"LIVES: " +str(din.HP))
    else:
        if  din.shieldischarged is True:
            print("SCORE: "+str(din.score)+10*" "+"BOSS LIFE: " +str(dragon.life)+12*" "+"SHEILD IS READY: Y"+12*" "+"LIVES: "+str(din.HP)+12*" " )
        else:
            print("SCORE: "+str(din.score)+(10)*" "+"BOSS LIFE: " +str(dragon.life)+12*" "+"SHEILD IS READY: N"+12*" "+"LIVES: " +str(din.HP)+12*" ")

    #DRAW BULLETS
    bullet.draw()

    #DRAW MAGNET
    magnet.draw()

    #FIRE ATTACK 
    fireattack.reset()
    fireattack.move()
    fireattack.draw()
     #COLLISON
    fireattack.collision()
    
    #FOR BUILDING CHARACTER
    din.buildcharacter()
    
    #FOR DRAWING DRAGON
    dragon.reset()
    dragon.draw()
    
    printmatrix()


    

os.system('clear')
print("SCORE: "+str(din.score)+20*" "+"SHEILD IS READY: Y"+20*" "+"LIVES: " +str(din.HP))
din.buildcharacter()


for i in range(board.y):
    for j in range(board.x):
        print(board.matrix[i][j],end="")
    print()

start=0
activeperiod=0
rechargeperiod=0
while True:
    
    #INPUT
    key=user_input()
    
    
    

    #FIRE ATTACK BY DRAGON
    fireattack.time+=1
    if fireattack.time==fireattack.interval:
        fireattack.breathattack()
        fireattack.time=0


    #MAKE THE GAME SLOWER AFTER POWER UP
    board.gameslower()

    #FOR REMOVING BULLET WHICH MOVE OUT OF SCREEN
    bullet.clear()
    
    #REMOVING PREVIOUS BULLET AND MOVING THEM
    bullet.reset() 
    bullet.move()

    #FOR SHIELD PURPOSE
    if din.shield is True:
        activeperiod+=1
        if activeperiod==din.count_activeshield:
            din.deactivateshield()
            activeperiod=0
    if din.shield is False and din.shieldischarged is False:
        rechargeperiod+=1
        if rechargeperiod==din.count_rechargeshield:
            din.chargetheshield()
            rechargeperiod=0


    # FOR GRAVITY EFFECT
    if din.y==(board.y-board.groundheight-1):
        din.jumpcount=0
    else:
        din.jumpcount+=1 

    #FOR CHECKING EFFECT OF MAGNET   
    magnet.magneteffect()

    #CHECKING WHICH KEY WAS PRESSED
    if key=='d':
        din.reset()
        for i in range(din.x_velocity()):
            din.move_right()
            coins.checkcollison()
            beam.beamcollison()
            speedup.powerup_collison()
            fireattack.collision()
        
        for i in range(din.gravity()):
            din.move_down()
            coins.checkcollison()
            beam.beamcollison()
            fireattack.collision()
            speedup.powerup_collison()
        
        draw()
    
    elif key=='a':
        din.reset()
        for i in range(din.x_velocity()):
            din.move_left()
            coins.checkcollison()
            beam.beamcollison()
            speedup.powerup_collison()
            fireattack.collision()
        
        for i in range(din.gravity()):
            din.move_down()
            coins.checkcollison()
            beam.beamcollison()
            fireattack.collision()
            speedup.powerup_collison()

        draw()
    
    elif key=='w':
        din.reset()
        din.jetpack()
        coins.checkcollison()
        beam.beamcollison()
        fireattack.collision()
        speedup.powerup_collison()

        draw()    
    
    elif key=='q' or din.HP<=0 or dragon.life<=0:
        exit()
    
    elif key==' ':
        din.activateshield()
    
    elif key=='f':
        bullet.fire()   
    
    else:
        if din.y<(board.y-board.groundheight-1):
            
            din.reset()
            for i in range(din.gravity()):
                
                din.move_down()
                coins.checkcollison()
                beam.beamcollison()
                fireattack.collision()
                speedup.powerup_collison()
            draw()
        
        else:
        
            din.reset() 
            fireattack.collision()
            draw()

