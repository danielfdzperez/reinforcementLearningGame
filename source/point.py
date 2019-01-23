from common import *

class Point:
    '''
        Class Point

        Represents a point in two dimensional space
    '''   
    def __init__(self, x,y=None):
        '''
            Constructor
            y -> y coordinate
            x -> x coordinate
            Default value of y is the value of x.
        '''
        if y is None:
            y = x
        self.x = x
        self.y = y
    
    def distance(self, target):
        '''
            TODO
            Return the distance between two points using A* algorithm.

            target -> Is the target point
        '''
        return 0

    def manhattanDistance(self, target):
        '''
            Calculate the manhatan distance between two points
            target -> Point

            return the manhatan distance
        '''
        return abs(self.x - target.x) + abs(self.y - target.y)

    def equals(self, point):
        '''
            Compare two points
            point -> The point to compare
        '''
        return self.x == point.x and self.y == point.y
    def __eq__(self, point):
        return self.equals(point)

    def __add__(self, point):
        '''
            Overload operator +

            return new point
        '''

        return Point(self.x + point.x, self.y + point.y)

    def __str__(self):
        '''
            Overload string operator

            returns string with the x and y
        '''
        return 'x:' + str(self.x) + ' y:' + str(self.y)

    def __mul__(self, point):
        if type(point) is int:
            return Point(self.x*point, self.y*point)
        return Point(self.x*point.x, self.y*point.y)

