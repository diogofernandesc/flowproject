import pygame
import Main

scr_size = (750, 750)
screen = pygame.display.set_mode(scr_size)
White = (255, 255, 255)
# --- grid built here
    
def build_grid():
    ''' You need two arrays to define the starting and end positions of the line:
    Because it draws lines, they take two pairs of x-coordinates; one for the start of the line and one for the end'''
    
    x_grid_pos1 = [150, 0]
    x_grid_pos2 = [150, 750]  
        
    y_grid_pos1 = [0 , 150]
    y_grid_pos2 = [750, 150]
        
    i = 0  # Initiating control variable for the loop
    while i != 4:
        ''' ***Very important***:
        - This while loop is used to control the intervals in which the lines are drawn for the grid
        - 750x750 grid so divided by 5 gives 150px intervals
        - So it will draw the initial line at the initial coordinates above
        - Then increments by 150 which is the amount of pixels in both directions that the lines will be separated by
        - i is looped 4 times because 4 lines are drawn in each direction'''
        
        pygame.draw.line(screen,White, (x_grid_pos1[0], x_grid_pos1[1]), (x_grid_pos2[0], x_grid_pos2[1]))
        x_grid_pos1[0] += 150
        x_grid_pos2[0] += 150 
            
        # The above code deals with vertical code - incrementing the x values of the coordinates of the lines
        # Means loop will draw a new line 150 pixels ahead of the previous
            
        pygame.draw.line(screen, White, (y_grid_pos1[0], y_grid_pos1[1]), (y_grid_pos2[0], y_grid_pos2[1]))
        y_grid_pos1[1] += 150
        y_grid_pos2[1] += 150
            
        i += 1  # increment control variable to continue looping
            

