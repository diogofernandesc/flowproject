import pygame
import Main



def check():
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