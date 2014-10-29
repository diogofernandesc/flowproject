import pygame
import math
from operator import pos
# Defining colours for the circles, paths(lines) and grid background

Black = (0 , 0, 0)
White = (255, 255, 255)
Blue = (0 , 0, 255)
Red = (255, 0, 0)
Yellow = (255, 255, 0)
Orange = (255, 100, 0)
Green = (0, 255, 0)

# Defining grid positions for circles
# Two dimension array so that the first group would represent possible coordinates of x and the second possible ones for y - easier to understand
grid = [[75,225,375,525,675],[75,225,375,525,675]]

  
pygame.init()

# Setting the grid size through width and height of game window

scr_size = (750, 750)
screen = pygame.display.set_mode(scr_size)

# Naming the caption of the window opened for the Game

pygame.display.set_caption("Flow")

# Loops until the user clicks the close Button
done = False

# Change how fast the screen updates
clock = pygame.time.Clock()

screen.fill(Black)

class grid_circle(pygame.sprite.Sprite): 
    def __init__(self, ctr_x, ctr_y, colour):
        pygame.sprite.Sprite.__init__(self)
        self.ctr_x = ctr_x
        self.ctr_y = ctr_y
        self.radius = 40
        self.colour = colour
        
    def render(self):
        pygame.draw.circle(screen, self.colour, (self.ctr_x, self.ctr_y), self.radius, 40)
        
global x
global y
global colour
colour = 0, 0, 0

x = 0 
y = 0

def click_detection(GridCircle):
    pos = pygame.mouse.get_pos()
    if ((GridCircle.ctr_x - GridCircle.radius) <= x) and ((GridCircle.ctr_x + GridCircle.radius) >= x):
        if ((GridCircle.ctr_y - GridCircle.radius) <= y) and ((GridCircle.ctr_y + GridCircle.radius) >= y):
            return True
    else:
        return False
    

class circle_line():
    def attributes(self):
        pos = pygame.mouse.get_pos()
        self.x = pos[0]
        self.y = pos[1]
        x = pos[0]
        y = pos[1]
    def Move(self):
        pos = pygame.mouse.get_pos()
        self.x = pos[0]
        self.y = pos[1]
        pygame.draw.circle(screen, colour,(pos[0],pos[1]), 10, 10)
        pygame.display.flip()
        ''' I draw extra circles because if the user draws the line very quickly there is large gaps between circles 
        so it doesn't look like a line, this sort of eliminates that problem, there is probably a better solution'''
        ''' I draw extra circles because if the user draws the line very quickly there is large gaps between circles 
        so it doesn't look like a line, this sort of eliminates that problem, there is probably a better solution'''
        


global moving_line
moving_line = circle_line()


def movement_checker():
    pos = pygame.mouse.get_pos()
    while (35 <= pos[1] <= 715):
        while (35 <= pos[0] <= 715):
            print("Yes")
            return True
   
        
# Creating circles for grid
    
circle_grid_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
    
# Red Circle Pair
    
RedCircle1 = grid_circle(grid[0][3], grid[1][0], Red)
RedCircle2 = grid_circle(grid[0][0], grid[1][2], Red)
RedCircle1.render()
RedCircle2.render()
    
# Blue Circle Pair
    
BlueCircle1 = grid_circle(grid[0][2], grid[1][1], Blue)
BlueCircle2 = grid_circle(grid[0][1], grid[1][3], Blue)
BlueCircle1.render()
BlueCircle2.render()
    
# Green Circle Pair
    
GreenCircle1 = grid_circle(grid[0][4], grid[1][0], Green)
GreenCircle2 = grid_circle(grid[0][3], grid[1][1], Green)
GreenCircle1.render()
GreenCircle2.render()
    
# Orange Circle Pair
    
OrangeCircle1 = grid_circle(grid[0][4], grid[1][3], Orange)
OrangeCircle2 = grid_circle(grid[0][0], grid[1][3], Orange)
OrangeCircle1.render()
OrangeCircle2.render()
    
 # Yellow Circle Pair
    
YellowCircle1 = grid_circle(grid[0][3], grid[1][3], Yellow)
YellowCircle2 = grid_circle(grid[0][4], grid[1][4], Yellow)
YellowCircle1.render()
YellowCircle2.render()
    
circle_grid_list.add(RedCircle1, RedCircle2, BlueCircle1, BlueCircle2, GreenCircle1, GreenCircle2, OrangeCircle1, OrangeCircle2, YellowCircle1, YellowCircle2)
all_sprites_list.add(RedCircle1, RedCircle2, BlueCircle1, BlueCircle2, GreenCircle1, GreenCircle2, OrangeCircle1, OrangeCircle2, YellowCircle1, YellowCircle2)



# ---- Main program loop ------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True # Closes the game and exits the loop
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            
            # This event is used to assign values to x and y to check the value of the function in the mouse motion event
            
            
                
        elif event.type == pygame.MOUSEMOTION:
            state = pygame.mouse.get_pressed()
            for circle in circle_grid_list:
                if click_detection(circle) == True:
                    colour = circle.colour
                    if state[0] == 1:
                        while movement_checker() == True:
                            moving_line.Move()
                        
                            
    # --- grid built here
    

    
    x_grid_pos1 = [150, 0]
    x_grid_pos2 = [150, 750] # You need two arrays to define the starting and end positions of the line
    
    y_grid_pos1 = [0 , 150]
    y_grid_pos2 = [750, 150]
    
    i = 0 # Initiating control variable for the loop
    while i != 4:
        pygame.draw.line(screen, White, (x_grid_pos1[0], x_grid_pos1[1]), (x_grid_pos2[0], x_grid_pos2[1]))
        x_grid_pos1[0] += 150
        x_grid_pos2[0] += 150 
        
        # The above code deals with vertical code - incrementing the x values of the coordinates of the lines
        # Means loop will draw a new line 150 pixels ahead of the previous
        
        pygame.draw.line(screen, White, (y_grid_pos1[0], y_grid_pos1[1]), (y_grid_pos2[0], y_grid_pos2[1]))
        y_grid_pos1[1] += 150
        y_grid_pos2[1] += 150
        
        i += 1 # increment control variable to continue looping
          
    # Update screen with changes
    pygame.display.flip()
        
    # Define frame rate of game - default at 60
    clock.tick(60)
        
#Quit game
pygame.quit()

    
        
        
        
        
    
    
    
    
    
    
    




