from common import *
import character

class AI(character.Character):

    HUNT = 0
    FLEE = 1
    def __init__(self, position, world, sprite):
        super().__init__(position,world,sprite)

        self.state = AI.HUNT

    def update(self):
        
        if self.moving:
            return
        player_position = self.world.player.position
        map = self.world.current_map

        #distance, movement, path = aStar(self.position, player_position, map)
        dist, path = aStar(self.position, player_position, map)

        movement = NONE_DIRECTION
        if len(path) > 1:
            movement = direction(self.position, path[1].position)


        if self.state == AI.FLEE and movement is not NONE_DIRECTION:
            neighbours = map.getNeighboursPosition(self.position)
            directions = []
            for neighbour in neighbours:
                directions.append(direction(self.position, neighbour))
            directions.remove(movement)
            if directions:
                directions.sort(key=lambda d:  distance(self.position + d, player_position, map, max_i = 1000),reverse=True)
                movement = directions[0]

        self.changeDirection(movement)

        new_position = self.position + self.direction
        #If the character can move to the new position update the position and animation
        if self.world.canMove(new_position):
            map.swapWalkable(self.position)
            #self.position = new_position
            #self.moveTo(new_position)
            super().move(new_position)
            #map.swapWalkable(self.position)
            map.swapWalkable(new_position)
            #self.updateAnimation()

    #def move(self):
    #    self.world.current_map.swapWalkable(self.position)
    #    super().move()
        #self.world.current_map.swapWalkable(self.position)
    '''def move(self):
        #print('antes :', self.id,self.world.canMove(self.position))
        self.world.current_map.swapWalkable(self.position)
        print('despues :', self.id,self.world.canMove(self.position))
        super().move()

        self.world.current_map.swapWalkable(self.position)'''






