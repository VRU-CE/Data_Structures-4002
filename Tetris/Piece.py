import pygame
import numpy as np


class Piece:
    def __init__(self):
        # a piece stores an array or matrix
        # it also has probably a position to store its position in tetris grid 
    
        pass
    

    def move(self,direction,grid):
        # tetris piece can move in 3 directions / hint: direction is a touple like this -> [1,0]
        # BUT you cant just move the piece everywhere you sould probably check it it fits the tetris grid and if it can then actualy move it  

        pass

    def rotate(self,grid):
        # tetris pieces can rotate so implement this 
        # you sould also check here whether the piece after rotation fits the grid or not
    
        pass

    def does_fit_grid(self,grid_matrix,new_piece_data:np.matrix,new_position)->bool:
        # as you can see this method takes the matrix of grid and new piece data and its position and returns bool and says whether it fits the grid or not
        
        pass