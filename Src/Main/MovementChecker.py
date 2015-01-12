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
    
    
    if (0 <= pos[1] <= 10) or (590 <= pos[1] <= 600) or (0 <= pos[0] <= 10) or (590 <= pos[0] <= 600):
        # Can't draw on the outer side of the circles towards the window wall
        return False

    else:
        if (51 <= pos[0] <= 149):
            if (90 <= pos[1] <= 110) or (190 <= pos[1] <= 210) or (290 <= pos[1] <= 310) or (390 <= pos[1] <= 410) or (490 <= pos[1] <= 510) or (590 <= pos[1] <= 600) :
                print("can't draw")
                return False
            
        elif (151 <= pos[0] <= 249):
            if (90 <= pos[1] <= 110) or (190 <= pos[1] <= 210) or (290 <= pos[1] <= 310) or (390 <= pos[1] <= 410) or (490 <= pos[1] <= 510) or (590 <= pos[1] <= 600) :
                print("Can't draw")
                return False
            
        elif (251 <= pos[0] <= 349):
            if (90 <= pos[1] <= 110) or (190 <= pos[1] <= 210) or (290 <= pos[1] <= 310) or (390 <= pos[1] <= 410) or (490 <= pos[1] <= 510) or (590 <= pos[1] <= 600) :
                print("can't draw")
                return False
            
        elif (351 <= pos[0] <= 449):
            if (90 <= pos[1] <= 110) or (190 <= pos[1] <= 210) or (290 <= pos[1] <= 310) or (390 <= pos[1] <= 410) or (490 <= pos[1] <= 510) or (590 <= pos[1] <= 600) :                
                print("can't draw")
                return False   
            
        elif (451 <= pos[0] <= 549):
            if (90 <= pos[1] <= 110) or (190 <= pos[1] <= 210) or (290 <= pos[1] <= 310) or (390 <= pos[1] <= 410) or (490 <= pos[1] <= 510) or (590 <= pos[1] <= 600) :
                print("can't draw")
                return False