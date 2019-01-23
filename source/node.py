from point import *




class Node:
    '''
        Class used to compute the A* algorithm
    '''
    
    def __init__(self, parent, position, target):
        '''
            Constructor
            parent -> Parent node
            position -> Point
            target -> is the target node.
        '''
        self.parent = parent
        if target is None:
            target = self
        parent_g = None
        parent_position = None

        if parent != None:
            parent_g = self.parent.g
            parent_position = self.parent.position
        else:
            parent_g = 0
            parent_position = Point(0,0)

        self.position = position
        #Estimated cost of the route
        self.g = parent_g + position.manhattanDistance(parent_position)
        #Distance to the target
        self.h = position.manhattanDistance(target.position)
        #Cost of the route
        self.f = self.g + self.h

    def equals(self, node):
        '''
            Compare two nodes
            node -> The nothe to compare with
        '''
        return self.position.equals(node.position)

    def __eq__(self,node):
        '''
            Overload operator
        '''
        if node == None:
            return False
        return self.equals(node)


    def __hash__(self):
        return hash((self.position.x, self.position.y))



    

