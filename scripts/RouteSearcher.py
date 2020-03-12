#!/usr/bin/env python

# Definitions for the search functionality

# @author: Patrick Gavigan

from astar import AStar
import math

class RouteSearcher(AStar):

    # Define the map
    def __init__(self):
        
        # Distances between neighbouring nodes as a graph
        self.nodeGraph = {'A': [('B',5), ('D',5)],
                          'B': [('A',5), ('C',5)],
                          'C': [('B',5), ('D',5), ('E',5)],
                          'D': [('A',5), ('C',5)],
                          'E': [('C',5)]}
        
        # Absolute locations of each node
        self.nodeLocations = {'A': (0,0),
                              'B': (0,5),
                              'C': (5,5),
                              'D': (5,0),
                              'E': (5,10)}        

     # Compute the distance between two (x,y) tuples
    def heuristic_cost_estimate(self, n1, n2):      
        (x1,y1) = self.nodeLocations[n1]
        (x2,y2) = self.nodeLocations[n2]
        return math.hypot(x2 - x1, y2 - y1)

    # Return the distance between two neighbouring nodes  
    def distance_between(self, n1, n2):
        return [item for item in self.nodeGraph[n1] if item[0] == n2][0][1]

    # Return list of neighbours
    def neighbors(self, node):
        neighbourNodes = self.nodeGraph[node]
        neighbourNames = [a_tuple[0] for a_tuple in neighbourNodes]
        return neighbourNames