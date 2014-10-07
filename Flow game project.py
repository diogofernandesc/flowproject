import pygame

import pygame.key


# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (750, 750)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Starting position of rectangle

circle_x = 50
circle_y = 50

# Speed and direction of rectangle

circle_change_x = 5
circle_change_y = 5

# Speed in pixels per frame

x_speed = 0
y_speed = 0



# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
 
        
        elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_speed += -150
                elif event.key == pygame.K_RIGHT:
                    x_speed += 150
                elif event.key == pygame.K_UP:
                    y_speed += -150
                elif event.key == pygame.K_DOWN:
                    y_speed += 150
                
                 
 
    # --- Game logic should go here
    
    
    ''' Movement with mouse
    global ctr_x
    global ctr_y
    pos = pygame.mouse.get_pos()'''
    ctr_x = 75
    ctr_y = 75
    # pygame.mouse.set_visible(False)
                
    # --- Drawing code should go here
 
    
    screen.fill(BLACK)
    
    i = 0
    xpos1 = [150, 0]
    xpos2 = [150, 750]
    ypos1 = [0, 150]
    ypos2 = [750, 150]
    
    while i != 4:
        pygame.draw.line(screen, WHITE,(xpos1[0], xpos1[1]), (xpos2[0], xpos2[1]))
        xpos1[0] += 150
        xpos2[0] += 150
        pygame.draw.line(screen, WHITE,(ypos1[0], ypos1[1]), (ypos2[0], ypos2[1]))
        ypos1[1] += 150
        ypos2[1] += 150
   
        i += 1

    # Introduce circles for motion
    ctr_x += x_speed
    ctr_y += y_speed
    if ctr_x < 40:
        ctr_x = 75
    
    # Creating 
    def draw_circle(colour, ctr_x, ctr_y):
        # Now I can use this function to create as many circles as I want, with the ability to change colour and position
        pygame.draw.circle(screen, colour, (ctr_x, ctr_y), 40, 40)
        
    draw_circle(RED, ctr_x, ctr_y)
    

    
    
    # Cause the ''colour'' rectangle to move:
    # pygame.draw.circle(screen, WHITE, (circle_x,circle_y), 15, 1)
    # circle_x += circle_change_x # rect_x = rect_x + 1 would do the same thing; just shorter version -
    # circle_y += circle_change_y

    # Bounce the rectangle

    if circle_y > 450 or circle_y < 0:
        circle_change_y = circle_change_y * -1
    if circle_x > 450 or circle_x < 0:
        circle_change_x = circle_change_x * -1

    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
screen.fill(BLACK)
