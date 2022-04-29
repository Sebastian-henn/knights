'''
grailCast.py - characters based on The Holy Grail, by Monty Python

Cast:
    Knight - the knights of the round table, lured by a beacon

'''
from math import atan2, cos, pi, sin, sqrt
import random

class Knight():
    myclass = "knights"
    '''
    Knight - has a row,col position and a name

    __init__ arguments:
        row : within MAXROWS
        col : within MAXCOLS
        name : a string
        speed : distance a knight can move in one iteration
    '''
    def __init__(self, limits, name, speed):
        self.row = random.randint(0, limits[0]-1)
        self.col = random.randint(0, limits[1]-1)
        self.speed = speed
        self.name = name
        self.captured = False
        self.felloff = False


       
    
    # Accessor methods

    def getRow(self):      # you *could* access these directly
        return self.row    # but showing how we can protect the data

    def getCol(self):
        return self.col

    def getName(self):
        return self.name

    # Mutator methods

    def lure(self, beacons, limits):
        '''
        lure - moves the individual knight towards the beacon(s)

        beacons - a list of beacon tuples (round bracket lists)
        limits - the boundaries of the "world"
        '''
        chosenBeacon = beacons[0] # could have multiple beacons...
        beaconRow = chosenBeacon[0]
        beaconCol = chosenBeacon[1]
        
        dy = self.row - beaconRow
        dx = self.col - beaconCol
        distanceToBeacon = sqrt(dy*dy + dx*dx)
        angleToBeacon = atan2(dy, dx)
        speed = min(self.speed, distanceToBeacon)

        self.row -= speed * sin(angleToBeacon)
        self.col -= speed * cos(angleToBeacon)

    def runaway(self, beacons, limits):
        '''
        runaway - moves the individual knight away from the beacon(s)

        beacons - a list of beacon tuples (round bracket lists)
        limits - the boundaries of the "world"
        '''
        chosenBeacon = beacons[0]
        beaconRow = chosenBeacon[0]
        beaconCol = chosenBeacon[1]

        dy = self.row - beaconRow
        dx = self.col - beaconCol
        distanceToBeacon = sqrt(dy*dy + dx*dx)
        angleToBeacon = atan2(dy, dx)
        speed = self.speed

        if (distanceToBeacon > speed):
            angleToRun = angleToBeacon
        else:
            angleToRun = random.randint(0, 359) * pi / 180

        self.row += speed * sin(angleToRun)
        self.col += speed * cos(angleToRun)
        self.row = max(min(self.row, limits[0]), 0)
        self.col = max(min(self.col, limits[1]), 0)


