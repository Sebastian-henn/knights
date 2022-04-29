'''

beaconSim.py - beacon simulation, knights move to the beacon when lit
               and run away when it goes out

'''

import matplotlib.pyplot as plt
import numpy as np
import random
from grailCast import*


MAXROWS = 40
MAXCOLS = 60



def plot_feature_scatter(itemlist, colour, limits):
    xlist = []
    ylist = []
    slist = []
    for r,c in itemlist:
        ylist.append(limits[0] - r - 1)  
        xlist.append(c)
        slist.append(100)
    plt.scatter(xlist,ylist,color=colour, marker='s', s=slist)
    
def plot_knight_scatter(knights, limits):
    xlist = []
    ylist = []
    slist = []
    clist = []
    for k in range(len(knights)):
        ylist.append(knights[k].getRow())  
        xlist.append(knights[k].getCol())
        slist.append(40)
        clist.append(k)
        plt.scatter(xlist,ylist,s=slist,c=clist)
  

def main():

    knightNames = ["Sir Galahad", "Sir Robin","Sir Terry","Sir Arthur","Sir James","Sir Richard"]
    beacons = [(20,30)] 
    beaconLit = 25 
    limits = [MAXROWS, MAXCOLS]
    # Starting population
    numKnights = 6
    knightList = []
    ax = plt.axis()


    for i in range(numKnights):  # add knight objects to grid
        knightList.append(Knight(limits, knightNames[i], 3))


    # Simulation
    
    for t in range(10):
        print("### Timestep ", t, "###")
        for i in range(numKnights):
            knightList[i].lure(beacons, limits)
        
        plot_knight_scatter(knightList, limits)
        plot_feature_scatter(beacons, "yellow", limits)
        plt.title("Beacon Simulation - Luring")
        plt.xlabel("Columns")
        plt.ylabel("Rows")
        plt.xlim(-1,MAXCOLS)
        plt.ylim(-1,MAXROWS)
        plt.pause(1)
        plt.clf()

    for t in range(10):
        print("### Timestep ", t + 10, "###")
        for i in range(numKnights):
            knightList[i].runaway(beacons, limits)
        
        plot_knight_scatter(knightList, limits)
        plot_feature_scatter(beacons, "yellow", limits)
        plt.title("Beacon Simulation - Luring")
        plt.xlabel("Columns")
        plt.ylabel("Rows")
        plt.xlim(-1,MAXCOLS)
        plt.ylim(-1,MAXROWS)
        plt.pause(1)
        plt.clf()
        

if __name__ == "__main__":
    main()
