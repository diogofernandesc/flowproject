import pygame
import Main


def click_detection(GridCircle):
    ''' Check whether the user is clicking within the area of the circle by taking the x and y centre coordinates
    and subtracting the radius - the user can click up to the last point on the circle'''
    if ((GridCircle.ctr_x - GridCircle.radius) <= Main.x) and ((GridCircle.ctr_x + GridCircle.radius) >= Main.x):
        if ((GridCircle.ctr_y - GridCircle.radius) <= Main.y) and ((GridCircle.ctr_y + GridCircle.radius) >= Main.y):
            return True
    else:
        return False