import math
import pygame

from Main import CircleRender, Grid, MovementChecker, ClickDetection


# Defining colours for the circles, paths(lines) and grid background
Black = (0 , 0, 0)
White = (255, 255, 255)
Blue = (0 , 0, 255)
Red = (255, 0, 0)
Yellow = (255, 255, 0)
Orange = (255, 100, 0)
Green = (0, 255, 0)

# Defining grid positions for circles
''' Two dimension array so that the first group would represent possible coordinates of x 
and the second possible ones for y - easier to understand'''
grid = [[75, 225, 375, 525, 675], [75, 225, 375, 525, 675]]


pygame.init()



# Sprite groups for the circle objects
circle_grid_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()



# Setting the grid size through width and height of game window

scr_size = (750, 750)
screen = pygame.display.set_mode(scr_size)

# Naming the caption of the window opened for the Game

pygame.display.set_caption("Flow")

# Loops until the user clicks the close Button
done = False

# Change how fast the screen updates
clock = pygame.time.Clock()

# Fill Screen in Black
screen.fill(Black)


#--------------------------

class grid_circle(pygame.sprite.Sprite):
    # Stationary circles class you need a pair of each colour
    def __init__(self, ctr_x, ctr_y, colour):
        pygame.sprite.Sprite.__init__(self)
        self.ctr_x = ctr_x
        self.ctr_y = ctr_y
        self.radius = 40
        self.colour = colour
        
    def render(self):
        # Render method draws circles at the stated position and colour given by the parameters
        pygame.draw.circle(screen, self.colour, (self.ctr_x, self.ctr_y), self.radius, 40)

# Initiate x and y variables for coordinates used by click detection and circle_line class for mouse coordinates 
global x
global y
x = 0
y = 0

    

class circle_line_mouse():
    '''Class for the moving line "circle_line" because the line is made up of individual circles'''
    def Move(self):
        ''' Move method takes the coordinates of where the mouse is pointing and its own coordinates
        and draws a circle at that position'''
        pos = pygame.mouse.get_pos()
        self.x = pos[0]
        self.y = pos[1]
        pygame.draw.circle(screen, colour, (pos[0], pos[1]), 10, 10)
        pygame.display.flip()
        
        
global moving_line_mouse
moving_line_mouse = circle_line_mouse()


# Sprite groups for the circle objects
circle_grid_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

''' The objects take the x and y coordinates as indexes of the grid array which has a list of values for the possible circle centres
as created by a 5x5 grid'''
    
# Red Circle Pair
        
RedCircle1 = CircleRender.grid_circle(grid[0][3], grid[1][0], Red)
RedCircle2 = CircleRender.grid_circle(grid[0][0], grid[1][2], Red)
RedCircle1.render()
RedCircle2.render()
        
# Blue Circle Pair
        
BlueCircle1 = CircleRender.grid_circle(grid[0][2], grid[1][1], Blue)
BlueCircle2 = CircleRender.grid_circle(grid[0][1], grid[1][3], Blue)
BlueCircle1.render()
BlueCircle2.render()
        
# Green Circle Pair
        
GreenCircle1 = CircleRender.grid_circle(grid[0][4], grid[1][0], Green)
GreenCircle2 = CircleRender.grid_circle(grid[0][3], grid[1][1], Green)
GreenCircle1.render()
GreenCircle2.render()
        
# Orange Circle Pair
        
OrangeCircle1 = CircleRender.grid_circle(grid[0][4], grid[1][3], Orange)
OrangeCircle2 = CircleRender.grid_circle(grid[0][0], grid[1][3], Orange)
OrangeCircle1.render()
OrangeCircle2.render()
        
# Yellow Circle Pair
        
YellowCircle1 = CircleRender.grid_circle(grid[0][3], grid[1][3], Yellow)
YellowCircle2 = CircleRender.grid_circle(grid[0][4], grid[1][4], Yellow)
YellowCircle1.render()
YellowCircle2.render()
        
circle_grid_list.add(RedCircle1, RedCircle2, BlueCircle1, BlueCircle2, GreenCircle1, GreenCircle2, OrangeCircle1, OrangeCircle2, YellowCircle1, YellowCircle2)
all_sprites_list.add(RedCircle1, RedCircle2, BlueCircle1, BlueCircle2, GreenCircle1, GreenCircle2, OrangeCircle1, OrangeCircle2, YellowCircle1, YellowCircle2)





# --- grid built here
        
Grid.build_grid()

''' *** IN PROGRESS *** '''
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True  # Closes the game and exits the loop
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            x_kspeed, y_kspeed = event.pos
            pygame.mouse.set_visible(False)
            ''' If the user clicks down on the left button the mouse coordinates at that point are assigned to variables 
            x and y which are used to check the condition of the click_detection function'''
            
        elif event.type == pygame.MOUSEBUTTONUP:
            pygame.mouse.set_visible(True)
            # Makes the cursor visible to choose a new circle easily
          
        elif event.type == pygame.MOUSEMOTION:
            
            ''' State is assigned to an array for each of three mouse buttons
            at state[0] it checks the left mouse button'''
            state = pygame.mouse.get_pressed()
            
            for circle in circle_grid_list:
                # Checks following conditions for every circle in that Sprite group
                
                if ClickDetection.click_detection(circle) == True:
                    ''' Checks whether a circle is being clicked
                    - If so then variable colour is assigned to the colour of the clicked circle
                    - This is used so that the move method from circle_line class can be called using the colour of the clicked circle'''
                    colour = circle.colour
                    
                    # *** WORK IN PROGRESS ***
                    if MovementChecker.check() != False:
                        print("can draw")
                        if state[0] == 1:
                            # Checking the left mouse button state, if 1 then button is being clicked or held down
                            moving_line_mouse.Move()
                            
                    elif MovementChecker.check() == False:
                        # Used to stop the move method for the moving_line object from being called if movement checker is false
                        print("Can't draw")
                            
                            
    # Update screen with changes
    pygame.display.flip()
        
    # Define frame rate of game - default at 60
    clock.tick(60)
        
# Quit game
pygame.quit()