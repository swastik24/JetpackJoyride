import numpy as np
import random
import os
class screen:
	def __init__(self,a,b,c,d,e,f,g):
		self.__size=a
		self.__x=a
		self.__y=b
		self.__gamelength=c
		self.__gamepointer=d
		self.__groundheight=e
		self.__roofhight=f
		self.__incfactor=g
		self.__matrix=np.ones((self.__y,self.__gamelength),str)
		
		#AFTER HOW MANY SECONDS SHOULD SCREEN MOVE
		self.__screenmovetime=.1
		#STORE INITIAL VALUE OF SCREENMOVETIME
		self.__storedmovetime=self.__screenmovetime
		self.__counter_to_initalspeed=0

	def get_size(self):
		return self.__size
	def set_size(self,size):
		self.__size=size
	size=property(get_size,set_size)

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

	def get_gamelength(self):
		return self.__gamelength
	def set_gamelength(self,gamelength):
		self.__gamelength=gamelength
	gamelength=property(get_gamelength,set_gamelength)

	def get_gamepointer(self):
		return self.__gamepointer
	def set_gamepointer(self,gamepointer):
		self.__gamepointer=gamepointer
	gamepointer=property(get_gamepointer,set_gamepointer)

	def get_groundheight(self):
		return self.__groundheight
	def set_groundheight(self,groundheight):
		self.__groundheight=groundheight
	groundheight=property(get_groundheight,set_groundheight)

	def get_roofhight(self):
		return self.__roofhight
	def set_roofhight(self,roofhight):
		self.__roofhight=roofhight
	roofhight=property(get_roofhight,set_roofhight)

	def get_incfactor(self):
		return self.__incfactor
	def set_incfactor(self,incfactor):
		self.__incfactor=incfactor
	incfactor=property(get_incfactor,set_incfactor)

	def get_matrix(self):
		return self.__matrix
	def set_matrix(self,matrix):
		self.__matrix=matrix
	matrix=property(get_matrix,set_matrix)

	def get_screenmovetime(self):
		return self.__screenmovetime
	def set_screenmovetime(self,screenmovetime):
		self.__screenmovetime=screenmovetime
	screenmovetime=property(get_screenmovetime,set_screenmovetime)

	def get_storedmovetime(self):
		return self.__storedmovetime
	def set_storedmovetime(self,storedmovetime):
		self.__storedmovetime=storedmovetime
	storedmovetime=property(get_storedmovetime,set_storedmovetime)

	def get_counter_to_initalspeed(self):
		return self.__counter_to_initalspeed
	def set_counter_to_initalspeed(self,counter_to_initalspeed):
		self.__counter_to_initalspeed=counter_to_initalspeed
	counter_to_initalspeed=property(get_counter_to_initalspeed,set_counter_to_initalspeed)

	def lengthofmygame(self):
		return self.__gamelength
	def pointertomygame(self):
		return self.__gamepointer	  
	def shiftthescreen(self):
		self.__gamepointer+=self.__incfactor
		if self.__gamepointer+self.__size>=self.__gamelength:
			self.__gamepointer=self.__gamelength-self.__size

	#MAKE GAME FASTER
	def gamefaster(self):
		if self.__screenmovetime==self.__storedmovetime:
			self.__incfactor*=2
			# self.__counter_to_initalspeed=0
		
	#TO REDUCE SPEED
	def gameslower(self):
		if self.__screenmovetime<self.__storedmovetime:
			
			self.__counter_to_initalspeed+=1
			if self.__counter_to_initalspeed>=100:
				self.__incfactor/=2
				self.__counter_to_initalspeed=0		
		
			  
board=screen(100,50,500,0,2,2,2)

for i in range(board.lengthofmygame()):
	for j in range(board.y):
	    board.matrix[j][i]=" "  
for i in range(board.lengthofmygame()):
    for j in range(board.groundheight):
        board.matrix[board.y-j-1][i]=" "

for i in range(board.lengthofmygame()):
    for j in range(board.roofhight):
        board.matrix[j][i]=" "#str(random.randint(0,9))    

	# f=open('/home/swastik/Desktop/DASS/Assignment1/dragon.txt','r')
	# l=[]
	# for line in f:
	# 	l.append(line.split('\n'))
	# for i in range(len(l)):
	#     l[i]=[e for e in l[i] if e]
	# for i in range(len(l)):
	# 	for j in range(len(l[i][0])):
	# 		board.matrix[3+i][10+j]=l[i][0][j]