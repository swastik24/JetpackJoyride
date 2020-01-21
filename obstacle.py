from background import *
from  character import *
from coin import *
import random

class obstacle:
    _shape=["|","-","/"]
    _powerup_structure=["2","x"]
    def removeobstacle(self):
        for i in range(board.y):
            for j in range(board.pointertomygame(),board.pointertomygame()+board.size):
                if board.matrix[i][j] in self._shape or self._powerup_structure:
                    board.matrix[i][j]=" "
            


class firebeam(obstacle):
    def __init__(self):
    
        self.__size=20
        for i in range(int((board.lengthofmygame()-2*board.size)/self.__size)):
            x=board.size+i*self.__size
            length=random.randint(5,15)
            y=random.randint(board.roofhight+16,board.y-board.groundheight-1) 
            t=random.randint(0,2)
            if t is 0:
                
                for j in range(length):
                    board.matrix[y][x]=self._shape[t]
                    y-=1
                    
            elif t  is 1:
                
                for j in range(length):
                    board.matrix[y][x]=self._shape[t]
                    x+=1
                
            else:
                
                for j in range(length):
                    board.matrix[y][x]=self._shape[t]
                    
                    x+=1
                    y-=1
                
    def get_shape(self):
        return self._shape
    def set_shape(self,shape):
        self._shape=shape
    shape=property(get_shape,set_shape)

    def get_powerup_structure(self):
        return self._powerup_structure
    def set_powerup_structure(self,powerup_structure):
        self._powerup_structure=powerup_structure
    powerup_structure=property(get_powerup_structure,set_powerup_structure)

    def get_size(self):
        return self.__size
    def set_size(self,size):
        self.__size=size
    size=property(get_size,set_size)



    def beamcollison(self):


        if din.shield is False:
            
            din.x+=board.pointertomygame()
            positions={board.matrix[din.y][din.x],board.matrix[din.y][din.x+1],board.matrix[din.y-1][din.x],board.matrix[din.y-1][din.x+1],board.matrix[din.y-2][din.x],board.matrix[din.y-2][din.x+1]}
            collison=False
            for z in positions:
                if z in self._shape:
                    collison=True
                    break
            if collison is True:
                self.removeobstacle()        
                din.HP-=1
            din.x-=board.pointertomygame()
        else:
            din.x+=board.pointertomygame()
            positions=[[din.y,din.x],[din.y,din.x+1],[din.y-1,din.x],[din.y-1,din.x+1],[din.y-2,din.x],[din.y-2,din.x+1]]
            
            for i in positions:
                if board.matrix[i[0]][i[1]] in self._shape:
                    if  board.matrix[i[0]][i[1]]=="|":
                        j=i[0]
                        while True:
                            if  board.matrix[j][i[1]]=="|":
                                board.matrix[j][i[1]]=" "
                                j-=1
                            else: 
                                break
                        j=i[0]+1
                        while True:
                            if  board.matrix[j][i[1]]=="|":
                                board.matrix[j][i[1]]=" "
                                j+=1
                            else: 
                                break
                    elif  board.matrix[i[0]][i[1]]=="-":
                        j=i[1]
                        while True:
                            if  board.matrix[i[0]][j]=="-":
                                board.matrix[i[0]][j]=" "
                                j-=1
                            else: 
                                break
                        j=i[1]+1
                        while True:
                            if  board.matrix[i[0]][j]=="-":
                                board.matrix[i[0]][j]=" "
                                j+=1
                            else: 
                                break    
                    else:
                        x=i[1]
                        y=i[0]
                        while True:
                            if board.matrix[y][x]=="/":
                                board.matrix[y][x]=" "
                                x+=1
                                y-=1   
                            else:
                                break
                        x=i[1]-1
                        y=i[0]+1
                        while True:
                            if board.matrix[y][x]=="/":
                                board.matrix[y][x]=" "
                                x-=1
                                y+=1   
                            else:
                                break
 
            din.x-=board.pointertomygame()

    def bulletcollison(self,bullet):
        positions=bullet.bulletarray
        for i in positions:
                if board.matrix[i[0]][i[1]] in self._shape:
                    if  board.matrix[i[0]][i[1]]=="|":
                        j=i[0]
                        while True:
                            if  board.matrix[j][i[1]]=="|":
                                board.matrix[j][i[1]]=" "
                                j-=1
                            else: 
                                break
                        j=i[0]+1
                        while True:
                            if  board.matrix[j][i[1]]=="|":
                                board.matrix[j][i[1]]=" "
                                j+=1
                            else: 
                                break
                    elif  board.matrix[i[0]][i[1]]=="-":
                        j=i[1]
                        while True:
                            if  board.matrix[i[0]][j]=="-":
                                board.matrix[i[0]][j]=" "
                                j-=1
                            else: 
                                break
                        j=i[1]+1
                        while True:
                            if  board.matrix[i[0]][j]=="-":
                                board.matrix[i[0]][j]=" "
                                j+=1
                            else: 
                                break    
                    elif board.matrix[i[0]][i[1]]=="/":
                        x=i[1]
                        y=i[0]
                        while True:
                            if board.matrix[y][x]=="/":
                                board.matrix[y][x]=" "
                                x+=1
                                y-=1   
                            else:
                                break
                        x=i[1]-1
                        y=i[0]+1
                        while True:
                            if board.matrix[y][x]=="/":
                                board.matrix[y][x]=" "
                                x-=1
                                y+=1   
                            else:
                              break

          
    def removeobstacle(self):
        
        for i in range(board.y):
            for j in range(board.pointertomygame(),board.pointertomygame()+board.size):
                if board.matrix[i][j] in self._shape:
                    board.matrix[i][j]=" "
        
class Magnet:
    __shape=[["*","*"],["*","*"]]
    def __init__(self):
        self.__x=105 #random.randint(board.size,board.lengthofmygame()-board.size-1-len(self.shape[0]))
        self.__y=random.randint(board.roofhight,board.y-board.groundheight-1-len(self.__shape))
        board.matrix[self.__y:self.__y+len(self.__shape),self.__x:self.__x+len(self.__shape[0])]=self.__shape
    
    def get_shape(self):
        return self.__shape
    def set_shape(self,shape):
        self.__shape=shape
    shape=property(get_shape,set_shape)

    def get_x(self):
        return self.__x
    def set_x(self,x):
        self.__x=x
    x=property(get_x,set_x)

    def get_y(self):
        return self.__y 
    def set_y(self,y):
        self.__y=y
    y=property(get_y,set_y)       
    
    def draw(self):
        board.matrix[self.__y:self.__y+len(self.__shape),self.__x:self.__x+len(self.__shape[0])]=self.__shape

    def magneteffect(self):
        if self.__x>board.pointertomygame() and self.__x<board.pointertomygame()+board.size:
            din.reset()
            din.x+=board.pointertomygame()
            if din.x<self.__x:
                
                
                din.x-=board.pointertomygame()
                
                for i in range(2):
                    din.move_right()
                    coins.checkcollison()
                    beam.beamcollison()
                    speedup.powerup_collison()
                    
                
                din.x+=board.pointertomygame()
            elif din.x>self.__x:
                din.x-=board.pointertomygame()

                for i in range(2):
                    din.move_left()
                    coins.checkcollison()
                    beam.beamcollison()
                    speedup.powerup_collison()
             
                din.x+=board.pointertomygame()                
            din.x-=board.pointertomygame()   
            if din.y<self.__y:
                
                din.y+=1
                coins.checkcollison()
                beam.beamcollison()
                speedup.powerup_collison()
                if din.y>board.y-board.groundheight-1:
                    din.y=board.y-board.groundheight-1
                    
            elif  din.y>self.__y:
                din.y-=1  
                coins.checkcollison()
                beam.beamcollison()
                speedup.powerup_collison()
                if din.y<din.maxheight:
                    din.y=  din.maxheight
            din.jumpcount=0 
            din.reset()
     



class powerup(obstacle):
    def __init__(self):
        self.__maxno=3
        for i in range(self.__maxno):
            y=random.randint(board.roofhight,board.y-board.groundheight-1)
            x=random.randint(board.size,board.lengthofmygame()-2-2*board.size)
            board.matrix[y][x]=self._powerup_structure[0]
            board.matrix[y][x+1]=self._powerup_structure[1]
    
    def get_maxno(self):
        return self.__maxno
    def set_maxno(self,maxno):
        self.__maxno=maxno
    maxno=property(get_maxno,set_maxno)

    def get_powerup_structure(self):
        return self._powerup_structure
    def set_powerup_structure(self,powerup_structure):
        self._powerup_structure=powerup_structure
    powerup_structure=property(get_powerup_structure,set_powerup_structure)

    def powerup_collison(self):
        din.x+=board.pointertomygame()
        positions=[[din.y,din.x],[din.y,din.x+1],[din.y-1,din.x],[din.y-1,din.x+1],[din.y-2,din.x],[din.y-2,din.x+1]]
        for i in positions:
            if board.matrix[i[0]][i[1]] in self._powerup_structure:
                
                if board.matrix[i[0]][i[1]]=="2":
                    # board.matrix[i[0]][i[1]]=" "
                    # board.matrix[i[0]][i[1]+1]=" "
                    self.removeobstacle(i[0],i[1])
                else:
                    # board.matrix[i[0]][i[1]]=" "
                    # board.matrix[i[0]][i[1]-1]=" " 
                    self.removeobstacle(i[0],i[1]-1)   
                board.gamefaster()
        din.x-=board.pointertomygame()        
    def removeobstacle(self,y,x):
        board.matrix[y][x]=" "
        board.matrix[y][x+1]=" "

magnet=Magnet()
beam=firebeam()      
speedup=powerup()