import pygame.font
import pygame
import random
# import pygame.gfxdraw
from Grid import *
from Piece import *

class Game:

    screen:pygame.Surface
    grid:Grid
    shapes_list:list = []

    def __init__(self,W=300,H=300,backgroundcolor="#A1B57D",hex=True):
        self.width = W
        self.height = H
        self.background = pygame.Color(backgroundcolor) if hex  else backgroundcolor
    
    def set_grid(self,x,y,e_col=(0,0,0),f_col=(1,1,1)):
        self.grid = Grid(x,y,e_col,f_col)


    def run(self,):
        #----------------Initialization---------------------
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen.fill(self.background)
        self.grid.font = pygame.font.SysFont('arial.ttf',20)
        #---------------------------------------------------



        #----------------Start-----------------------        
        #Setting up timer
        max_ticks_btw_move = 20 
        current_tick = 0
        tick=False

        current_piece = random.choice(self.shapes_list)

        # put things here if you want them to run only once
        
        #--------------------------------------------        



        
        
        #----------------Update-----------------------        
        running = True
        while running:
            direction=[0,0]
            pygame.time.delay(10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key  == pygame.K_r:
                        self.grid.clear()
                    if event.key == pygame.K_LEFT:
                        direction = [0,-1]
                        # current_piece.move(direction,self.grid.matrix)       *
                    if event.key == pygame.K_RIGHT:
                        direction = [0,1]
                        # current_piece.move(direction,self.grid.matrix)       *
                    if event.key == pygame.K_DOWN:
                        direction = [1,0]
                        # current_piece.move(direction,self.grid.matrix)       *
                    if event.key == pygame.K_UP:
                        # current_piece.rotate(self.grid.matrix)               *
                        tmp = 1

            self.grid.draw_grid(self.screen,current_piece)
            
            if tick:
                #current_piece.move([1,0],self.grid.matrix)                    *
                tmp=1
            
            if tick:
                #self.grid.check_filled_row_and_move_down()                    *
                tmp=1
            
            if tick:
                # res= self.grid.check_below_piece_and_insert(current_piece)          *
                res = False # remove this line when sterted implementing
                if res:
                    current_piece = random.choice(self.shapes_list)
                    current_piece.position = [0,0]


            
            if current_tick >= max_ticks_btw_move:
                current_tick = 0 
                tick = True
            else:
                current_tick+=1
                tick=False
            
            pygame.display.flip()
        #--------------------------------------------        

        pygame.quit()

if __name__ == "__main__":
    game = Game(300,600,"#203239")
    game.set_grid(20,10,e_col="#141E27",f_col="#E0DDAA")

    # make some pieces and append them to game list 
    p =  Piece()
    game.shapes_list.append(p)
    game.run()
