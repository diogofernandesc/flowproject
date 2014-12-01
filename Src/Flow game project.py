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
''' Two dimension array so that the first group would represent possible coordinates of x 
and the second possible ones for y - easier to understand'''
grid = [[75, 225, 375, 525, 675], [75, 225, 375, 525, 675]]

  
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

def click_detection(GridCircle):
    ''' Check whether the user is clicking within the area of the circle by taking the x and y centre coordinates
    and subtracting the radius - the user can click up to the last point on the circle'''
    if ((GridCircle.ctr_x - GridCircle.radius) <= x) and ((GridCircle.ctr_x + GridCircle.radius) >= x):
        if ((GridCircle.ctr_y - GridCircle.radius) <= y) and ((GridCircle.ctr_y + GridCircle.radius) >= y):
            return True
    else:
        return False
    

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
        
        
def draw_keyboard():
    pygame.draw.circle(screen, colour, (k_x, k_x), 10, 10)


global moving_line_mouse
moving_line_mouse = circle_line_mouse()


def movement_checker():
    pos = pygame.mouse.get_pos()
    ''' ***Work in progress***:
    Basic principle:
    - The first if statement checks whether or not the moving line is on the borders if so returns False
    - Otherwise it's true so it can draw and checks the rest
    - Following if statements:
        - It checks whether the mouse is within the range of x-coordinates where at specific y-axis values nothing can be drawn
        - So if the mouse is at this x-coordinates then the following if statement checks whether the y is at the invalid y values and returns false'''
    
    
    if (0 <= pos[1] <= 44) or (706 <= pos[1] <= 750) or (0 <= pos[0] <= 44) or (706 <= pos[0] <= 750):
        # Can't draw on the outer side of the circles towards the window wall
        return False

    else:
        if (116 <= pos[0] <= 184):
            if (86 <= pos[1] <= 184) or (236 <= pos[1] <= 334) or (386 <= pos[1] <= 484) or (536 <= pos[1] <= 634):
                print("can't draw")
                return False
        elif (266 <= pos[0] <= 334):
            if (86 <= pos[1] <= 184) or (236 <= pos[1] <= 334) or (386 <= pos[1] <= 484) or (536 <= pos[1] <= 634):
                print("Can't draw")
                return False
        elif (416 <= pos[0] <= 484):
            if (116 <= pos[1] <= 184) or (266 <= pos[1] <= 334) or (416 <= pos[1] <= 484) or (566 <= pos[1] <= 634):
                print("can't draw")
                return False
        elif (566 <= pos[0] <= 634):
            if (116 <= pos[1] <= 184) or (266 <= pos[1] <= 334) or (416 <= pos[1] <= 484) or (566 <= pos[1] <= 634):
                print("Can't draw")
                return False   
        
# ---Creating circles for grid---

# Sprite groups for the circle objects
circle_grid_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

''' The objects take the x and y coordinates as indexes of the grid array which has a list of values for the possible circle centres
as created by a 5x5 grid'''

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
        
        pygame.draw.line(screen, White, (x_grid_pos1[0], x_grid_pos1[1]), (x_grid_pos2[0], x_grid_pos2[1]))
        x_grid_pos1[0] += 150
        x_grid_pos2[0] += 150 
            
        # The above code deals with vertical code - incrementing the x values of the coordinates of the lines
        # Means loop will draw a new line 150 pixels ahead of the previous
            
        pygame.draw.line(screen, White, (y_grid_pos1[0], y_grid_pos1[1]), (y_grid_pos2[0], y_grid_pos2[1]))
        y_grid_pos1[1] += 150
        y_grid_pos2[1] += 150
            
        i += 1  # increment control variable to continue looping
            
build_grid()


# ---- Main program loop ------
''' *** IN PROGRESS *** '''
while not done:
    pressed = pygame.key.get_pressed()
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
                
                if click_detection(circle) == True:
                    ''' Checks whether a circle is being clicked
                    - If so then variable colour is assigned to the colour of the clicked circle
                    - This is used so that the move method from circle_line class can be called using the colour of the clicked circle'''
                    colour = circle.colour
                    
                    # *** WORK IN PROGRESS ***
                    if movement_checker() != False:
                        print("can draw")
                        if state[0] == 1:
                            # Checking the left mouse button state, if 1 then button is being clicked or held down
                            moving_line_mouse.Move()
                            
                    elif movement_checker() == False:
                        # Used to stop the move method for the moving_line object from being called if movement checker is false
                        print("Can't draw")
                            
    
                            
    # Update screen with changes
    pygame.display.flip()
        
    # Define frame rate of game - default at 60
    clock.tick(60)
        
# Quit game
pygame.quit()
