from  background import *
from  character import *
import random,os

class mapcoins:
    
    def __init__(self):
        len=9
        x=board.size
        for i in range(int(board.lengthofmygame()/board.size)-2):
            y=x+board.size*i
            X_axis=random.randint(y,y+board.size-5)
            Y_axis=random.randint(board.roofhight,board.y-board.groundheight-1)
            for j in range(len):
                board.matrix[Y_axis][X_axis+j]="$"
    def checkcollison(self):
        # os.system('clear')
        
        din.x+=board.pointertomygame()
        if board.matrix[din.y][din.x] == "$":
            din.score+=5
            board.matrix[din.y][din.x]=" "
        if board.matrix[din.y][din.x+1] == "$":
            din.score+=5
            board.matrix[din.y][din.x+1]=" "
        if board.matrix[din.y-1][din.x] == "$":
            din.score+=5
            board.matrix[din.y-1][din.x]=" "
        if board.matrix[din.y-1][din.x+1] == "$":
            din.score+=5
            board.matrix[din.y-1][din.x+1]=" "
        if board.matrix[din.y-2][din.x] == "$":
            din.score+=5
            board.matrix[din.y-2][din.x]=" "
        if board.matrix[din.y-2][din.x+1] == "$":
            din.score+=5
            board.matrix[din.y-2][din.x+1]=" "
        din.x-=board.pointertomygame()

coins=mapcoins()        