import numpy as np
import pygame.font
from Piece import *

class Grid:
    
    def __init__(self,x,y,empty_col,fill_col,hex=True):
        # initializing the matrix and colors
        self.empty_col = pygame.Color(empty_col) if hex  else empty_col
        self.fill_col = pygame.Color(fill_col) if hex  else fill_col

        self.matrix = np.zeros(shape=(x,y)) 
        # print(self.matrix)

    def clear(self,):
        self.matrix.fill(0)

    def check_filled_row_and_move_down(self):
        # as the name of method first check if a row in grid is filled
        # second move everything above it 
        
        pass 

    def move_down_rows(self,i):
        # this will be used in method above

        pass


    def insert_piece(self,piece:Piece):
        # insert the piece which takes from argument and changes the self grid
        
        pass

    def check_piece_in_bound(self,piece:Piece,i,j) -> bool:
        # a piece must be inside the grid. this method take are of that.but insted of checking the whole piece every time
        # you can send i,j to this method and just ckeck whether the piece is in i,j position or not
        
        return False # delete this line when you stated implementing this method
        pass

            
    def check_below_piece_and_insert(self,piece:Piece) ->bool:
        # this one take the piece and ckecks if it hits the ground OR a filled place in grid
        # also if it does you can just innsert it bcause why not
        
        pass

    def draw_grid(self,screen:pygame.Surface,piece:Piece):

        cell_x = int(screen.get_width()/self.matrix.shape[1])
        cell_y = int(screen.get_height() /self.matrix.shape[0])
        
        i= 0
        for y_cord in range(0, screen.get_height(), cell_y):
            j=0
            for x_cord in range(0, screen.get_width(),cell_x):
                rect = pygame.Rect(x_cord, y_cord, cell_x-1, cell_y-1)
                rect_color = self.fill_col if self.matrix[i,j] == 1 or self.check_piece_in_bound(piece,i,j) else self.empty_col
                pygame.draw.rect(screen, rect_color, rect, 0,2,2,2,2)
                
                self.print_index_number(screen,x_cord,y_cord,f"{i},{j}")

                j+=1
            i+=1
   
    def print_index_number(self,screen,x,y,txt):
        img = self.font.render(txt, True, (255,0,0))
        screen.blit(img, (x, y))