from background import *
from colorama import Fore,Back,Style



class player:
    
    def __init__(self,a,b,c,d,e):
        self._x=a
        self._y=b
        self._horizontal_velocity=c
        self._inair_horizontalvel=d
        self._vertical_velocity=e

class MC(player):
    __jumpcount=0
    __maxheight=2+board.roofhight
    __score=0
    __HP=3
    __shield=False
    __shieldischarged=True
    __count_activeshield=30
    __count_rechargeshield=60

    __lengthofcharacter=2
    __heightofcharacter=3

    def __init__(self):
        player.__init__(self,2,board.y-board.groundheight-1,2,3,2)
        
    def get_x(self):
        return self._x
    def set_x(self,x):
        self._x=x
    x=property(get_x,set_x)
    
    def get_y(self):
        return self._y
    def set_y(self,y):
        self._y=y
    y=property(get_y,set_y)

    def get_score(self):
        return self.__score
    def set_score(self,score):
        self.__score=score
    score=property(get_score,set_score)

    def get_jumpcount(self):
        return self.__jumpcount
    def set_jumpcount(self,jumpcount):
        self.__jumpcount=jumpcount
    jumpcount=property(get_jumpcount,set_jumpcount)

    def get_HP(self):
        return self.__HP
    def set_HP(self,HP):
        self.__HP=HP
    HP=property(get_HP,set_HP)

    def get_shieldischarged(self):
        return self.__shieldischarged
    def set_shieldischarged(self,shieldischarged):
        self.__shieldischarged=shieldischarged                      
    shieldischarged=property(get_shieldischarged,set_shieldischarged)

    def get_count_activeshield(self):
        return self.__count_activeshield
    def set_count_activeshield(self,count_activeshield):
        self.__count_activeshield=count_activeshield
    count_activeshield=property(get_count_activeshield,set_count_activeshield)

    def get_count_rechargeshield(self):
        return self.__count_rechargeshield
    def set_count_rechargeshield(self,count_rechargeshield):
        self.__count_rechargeshield=count_rechargeshield
    count_rechargeshield=property(get_count_rechargeshield,set_count_rechargeshield)

    def get_shield(self):
        return self.__shield
    def set_shield(self,shield):
        self.__shield=shield 
    shield=property(get_shield,set_shield)                    

    def get_heightofcharacter(self):
        return self.__heightofcharacter
    def set_heightofcharacter(self,heightofcharacter):
        self.__heightofcharacter=heightofcharacter
    heightofcharacter=property(get_heightofcharacter,set_heightofcharacter)

    def get_maxheight(self):
        return self.__maxheight
    def set_maxheight(self,maxheight):
        self.__maxheight=maxheight
    maxheight=property(get_maxheight,set_maxheight)    

    def buildcharacter(self):
        self._x+=board.pointertomygame()
        if self._y==board.y-board.groundheight-1:
            board.matrix[self._y][self._x]="_"
            board.matrix[self._y][self._x+1]="_"
        else:
            board.matrix[self._y][self._x]="|"
            board.matrix[self._y][self._x+1]="|"
        board.matrix[self._y-1][self._x]="|"
        board.matrix[self._y-1][self._x+1]="|"
        board.matrix[self._y-2][self._x]="("
        board.matrix[self._y-2][self._x+1]=")"    
        self._x-=board.pointertomygame()
    def reset(self):
        
        self._x+=board.pointertomygame()
      
        board.matrix[self._y][self._x]=" "
        board.matrix[self._y][self._x+1]=" "
        board.matrix[self._y-1][self._x]=" "
        board.matrix[self._y-1][self._x+1]=" "
        board.matrix[self._y-2][self._x]=" "
        board.matrix[self._y-2][self._x+1]=" "
        self._x-=board.pointertomygame()
    def move_right(self):
        self._x+=board.pointertomygame()
        if(self._x<board.pointertomygame()+board.size-2):
            # board.matrix[self.y][self.x]=" "
            # if self.y<board.y-board.groundheight-1:
            #     self.x+=self.inair_horizontalvel
            # else:    
            #     self.x+=self.horizontal_velocity
            self._x+=1
            if(self._x>board.pointertomygame()+board.size-2):
                self._x=board.pointertomygame()+board.size-2
        self._x-=board.pointertomygame()        
    def move_left(self):
        self._x+=board.pointertomygame()
        if(self._x>board.pointertomygame()):
            # board.matrix[self.y][self.x]=" "
            # if self.y<board.y-board.groundheight-1:
            #     self.x-=self.inair_horizontalvel
            # else:    
            #     self.x-=self.horizontal_velocity
            # if self.x<board.pointertomygame():
            #     self.x=board.pointertomygame() 
            self._x-=1
        self._x-=board.pointertomygame()           
    def jetpack(self):
        self.__jumpcount=0
        if self._y>self.__maxheight:
            # board.matrix[self.y][self.x]=" "
            self._y-=self._vertical_velocity
            if self._y<self.__maxheight:
                self._y=self.__maxheight
    def gravity(self):
        # board.matrix[self.y][self.x]=" "
        if self._y is 0:
            return 0
        height=int((self.__jumpcount**2)*0.02)
        return height
        
   
    def move_down(self):
        self._y+=1
        if (self._y>(board.y-board.groundheight-1)):
            self._y=board.y-board.groundheight-1

    def activateshield(self):
        if self.__shieldischarged is True:
            self.__shield=True
            self.__shieldischarged=False  
    def deactivateshield(self):
        self.__shield=False           
    def chargetheshield(self):
        self.__shieldischarged=True
    def x_velocity(self):
        
        if self._y<board.y-board.groundheight-1:
            return self._inair_horizontalvel
        else:    
            return self._horizontal_velocity

din=MC()

class boss:
    def __init__(self):
        self.__length=40
        self.__x=board.lengthofmygame()-self.__length
        self.__y=din.y
        self.__width=15
        self.__life=100
        f=open('/home/swastik/Desktop/DASS/Assignment1/dragon.txt','r')
        self.__bossarray=[]
        
        for line in f:
            self.__bossarray.append(line.split('\n'))
        for i in range(len(self.__bossarray)):
            self.__bossarray[i]=[e for e in self.__bossarray[i] if e]

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

    def get_length(self):
        return self.__length
    def set_length(self,length):
        self.__length=length
    length=property(get_length,set_length)

    def get_width(self):
        return self.__width
    def set_width(self,width):
        self.__width=width
    width=property(get_width,set_width)

    def get_life(self):
        return self.__life
    def set_life(self,life):
        self.__life=life
    life=property(get_life,set_life)

    def get_bossarray(self):
        return self.__bossarray                                
    def set_bossarray(self,bossarray):
        self.__bossarray=bossarray
    bossarray=property(get_bossarray,set_bossarray)

    def draw(self):
        if board.pointertomygame()==(board.lengthofmygame()-board.size):
            self.__y=din.y-2
            if self.__y>(board.y-board.groundheight-self.__width):
                self.__y=board.y-board.groundheight-self.__width
            for i in range(len(self.__bossarray)):
                for j in range(len(self.__bossarray[i][0])):
                    board.matrix[self.__y+i][self.__x+j]=self.__bossarray[i][0][j]

    def reset(self):
        if self.__y>(board.y-board.groundheight-self.__width):
                self.__y=board.y-board.groundheight-self.__width
        if  board.pointertomygame()==(board.lengthofmygame()-board.size):
            for i in range(len(self.__bossarray)):
                for j in range(len(self.__bossarray[i][0])):
                    board.matrix[self.__y+i][self.__x+j]=" "

    
    
  

dragon=boss()
    
def printmatrix():
    din.x+=board.pointertomygame()
    positions=[[din.y,din.x],[din.y,din.x+1],[din.y-1,din.x],[din.y-1,din.x+1],[din.y-2,din.x],[din.y-2,din.x+1]]
    shape=["|","-","/"]
    powerup_structure=["2","x"]

    for i in range(board.y):
        for j in range(board.pointertomygame(),board.pointertomygame()+board.size):
            if i<board.groundheight or i>board.y-board.roofhight-1:
                print(Back.LIGHTBLACK_EX,end="")
                 
            else:
                
                print(Back.WHITE    ,end="")
                 
                if board.matrix[i][j]=="$":
                    print(Fore.YELLOW+Back.WHITE,end="")
                     
                elif board.matrix[i][j]=="#":
                    print(Fore.RED+Back.WHITE,end="")
                
                elif board.matrix[i][j]=="o":
                    print(Fore.MAGENTA+Back.WHITE,end="")

                elif [i,j] in positions:
                    if din.shield is True:
                        print(Fore.BLUE+Back.WHITE,end="")
                         
                    else:
                        print(Fore.BLACK+Back.WHITE,end="")    
               
                elif j>=board.pointertomygame()-dragon.length or (i>=dragon.y and i<=dragon.y+dragon.width-1):
                    print(Fore.GREEN+Back.WHITE,end="")

                elif board.matrix[i][j] in shape:
                    print(Fore.RED+Back.WHITE,end="")

                elif board.matrix[i][j] in powerup_structure:
                    print(Fore.MAGENTA+Back.WHITE,end="")

                         
            print(board.matrix[i][j],end="")
            print(Style.RESET_ALL,end="")
        print()
    din.x-=board.pointertomygame()



