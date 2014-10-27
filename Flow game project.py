import pygame
import math
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
global GridCircle
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
    def Move(self):
        
        pos = pygame.mouse.get_pos()
        self.x = pos[0]
        self.y = pos[1]
        pygame.draw.circle(screen, grid_circle.colour,(pos[0],pos[1]), 20, 20)
        
        
moving_line = circle_line()

        
RedCircle1 = grid_circle(grid[0][3], grid[1][0], Red)
RedCircle1.render() 

# ---- Main program loop ------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True # Closes the game and exits the loop
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            click_detection(RedCircle1)
                
        elif event.type == pygame.MOUSEMOTION:
            state = pygame.mouse.get_pressed()
            if click_detection(RedCircle1) == True: 
                if state[0] == 1:
                    moving_line.Move()
                            
        
   
    # --- Game logic -----
    
    
    
    
    
    # ---------------------
    
    # ----Drawing code + grid built here
    

    
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
    
            
          
    # Update screen with changes
    pygame.display.flip()
        
    # Define frame rate of game - default at 60
    clock.tick(60)
        
#Quit game
pygame.quit()

    
        
        
        
        
    
    
    
    
    
    
    




