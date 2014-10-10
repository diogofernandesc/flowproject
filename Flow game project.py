import pygame

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


# ---- Main program loop ------

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True # Closes the game and exits the loop
            
    # --- Game logic -----
    
    
    
    
    
    # ---------------------
    
    # ----Drawing code + grid built here
    
    screen.fill(Black)
    
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
    class circle():
        colour = ()
        ctr_x = ()
        ctr_y = ()
     
    # Red Circle - changing the called values from array 'grid' will change the position on the screen for the grid
    RedCircle = circle()
    RedCircle.colour = Red
    RedCircle.ctr_x = grid[0][0]
    RedCircle.ctr_y = grid[1][0]
    
    # Blue Circle
    BlueCircle = circle()
    BlueCircle.colour = Blue
    BlueCircle.ctr_x = grid[0][3]
    BlueCircle.ctr_y = grid[1][4]
    
    # Yellow Circle
    YellowCircle = circle()
    YellowCircle.colour = Yellow
    YellowCircle.ctr_x = grid[0][4]
    YellowCircle.ctr_y = grid[1][1]
    
    # Orange Circle
    OrangeCircle = circle()
    OrangeCircle.colour = Orange
    OrangeCircle.ctr_x = grid[0][0]
    OrangeCircle.ctr_y = grid[1][2]
    
    # Green Circle
    GreenCircle = circle()
    GreenCircle.colour = Green
    GreenCircle.ctr_x = grid[0][4]
    GreenCircle.ctr_y = grid[1][0]
    
    
    
    
    # Draws circle(s) on screen
 
    def draw_circle(circle):
            # Functions draws circle with chosen colour and centre co-ordinates of circle
            pygame.draw.circle(screen, circle.colour, (circle.ctr_x, circle.ctr_y), 40 , 40)
            
    
    draw_circle(RedCircle)
    draw_circle(BlueCircle)
    draw_circle(YellowCircle)
    draw_circle(OrangeCircle)
    draw_circle(GreenCircle)
        
    # Creating circles 
    
  
    
   
    
    # Update screen with changes
    pygame.display.flip()
        
    # Define frame rate of game - default at 60
    clock.tick(60)
        
#Quit game
pygame.quit()
screen.fill(Black)
    
        
        
        
        
    
    
    
    
    
    
    




