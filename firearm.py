from character import *
from background import *
from obstacle import *

class fireshot:
    
    def __init__(self,velocity,max_noofbullet):
        self.__velocity=velocity
        self.__max_noofbullet=max_noofbullet
        self.__bulletarray=[]

    def get_velocity(self):
        return self.__velocity
    def set_velocity(self,velocity):
        self.__velocity=velocity
    velocity=property(get_velocity,set_velocity)

    def get_max_noofbullet(self):
        return self.__max_noofbullet
    def set_max_noofbullet(self,max_noofbullet):
        self.__max_noofbullet=max_noofbullet
    max_noofbullet=property(get_max_noofbullet,set_max_noofbullet)

    def get_bulletarray(self):
        return self.__bulletarray
    def set_bulletarray(self,bulletarray):
        self.__bulletarray=bulletarray
    bulletarray=property(get_bulletarray,set_bulletarray)                    

    def clear(self):
        for x in self.__bulletarray:
            if  x[1]>=board.pointertomygame()+board.size:
                board.matrix[x[0]][x[1]]=" "
                self.__bulletarray.remove(x)

    def fire(self):
        
        if len(self.__bulletarray)<self.__max_noofbullet:
            
            i=[din.y-din.heightofcharacter+2,din.x+board.pointertomygame()]
            self.__bulletarray.append(i)

    def move(self):
        for x in self.__bulletarray:
            for i in range(self.__velocity):
                x[1]+=1
                if(x[1])>=board.lengthofmygame():
                    self.__bulletarray.remove(x)
                    break
                beam.bulletcollison(bullet)
                if board.pointertomygame()==board.lengthofmygame()-board.size:
                    if x[0]>=dragon.y and x[0]<dragon.y+dragon.width:
                        if x[1]>=dragon.x:
                            dragon.life-=2
                            self.__bulletarray.remove(x)  
                            break
    def draw(self):
        for x in self.__bulletarray:
            if  board.matrix[x[0]][x[1]]!="$" and board.matrix[x[0]][x[1]]!="2" and board.matrix[x[0]][x[1]]!="x":
                board.matrix[x[0]][x[1]]="o"

    def reset(self):
        for x in self.__bulletarray:
            if board.matrix[x[0]][x[1]]!="$" and board.matrix[x[0]][x[1]]!="2" and board.matrix[x[0]][x[1]]!="x":
                board.matrix[x[0]][x[1]]=" "


class breathfire:
    def __init__(self):
        self.__fireattack=[["#","#","#"," "],
                         ["#","#","#","#"],
                         ["#","#","#","#"],
                         ["#","#","#"," "]]
        self.__interval=10
        self.__time=0
        self.__position=[]

    def get_fireattack(self):
        return self.__fireattack
    def set_fireattack(self,fireattack):
        self.__fireattack=fireattack
    fireattack=property(get_fireattack,set_fireattack)
    
    def get_time(self):
        return self.__time
    def set_time(self,time):
        self.__time=time
    time=property(get_time,set_time)

    def get_interval(self):
        return self.__interval
    def set_interval(self,interval):
        self.__interval=interval 
    interval=property(get_interval,set_interval)

    def get_position(self):
        return self.__position
    def set_position(self,position):
        self.__position=position
    position=property(get_position,set_position)               

    def breathattack(self):
        

        if board.pointertomygame()>=board.lengthofmygame()-board.size-2:
            
            x_cor=dragon.x-len(self.__fireattack)
            if din.y>board.y-board.groundheight-len(self.__fireattack)-1:
                y_cor=board.y-board.groundheight-len(self.__fireattack)-1
            else:
                y_cor=din.y

            for i in range(len(self.__fireattack)):
                for j in range(len(self.__fireattack[i])):
                    board.matrix[y_cor+i][x_cor+j]=self.__fireattack[i][j]    
            self.__position.append([y_cor,x_cor])
    
    def move(self):
        for x in self.__position:
            x[1]-=1
            if x[1]==board.pointertomygame():
                self.__position.remove(x)

    def draw(self):
        for x in self.__position:
            for i in range(len(self.__fireattack)):
                for j in range(len(self.__fireattack[i])):
                    board.matrix[x[0]+i][x[1]+j]=self.__fireattack[i][j]

    def reset(self):
        for x in self.__position:
            for i in range(len(self.__fireattack)):
                for j in range(len(self.__fireattack[i])):
                    board.matrix[x[0]+i][x[1]+j]=" "

    def collision(self):
        if din.shield is False:
            din.x+=board.pointertomygame()
            cordinates=[[din.y,din.x],[din.y,din.x+1],[din.y-1,din.x],[din.y-1,din.x+1],[din.y-2,din.x],[din.y-2,din.x+1]]
            for x in cordinates:
                if board.matrix[x[0]][x[1]]=="#":
                    din.HP-=1
                    
                    self.reset()
                    self.__position=[] 
                    break   
            din.x-=board.pointertomygame()


bullet=fireshot(10,5)
fireattack=breathfire()