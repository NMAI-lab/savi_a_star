# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 10:10:14 2017

@author: patrickgavigan
"""
# https://www.python.org/doc/essays/graphs/

class SearchProblem:

    def __init__(self):
        self.graph = {'Arad': [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
                      'Zerind': [('Arad', 75), ('Oradea', 71)],
                      'Timisoara': [('Arad', 118), ('Lugoj', 111)],
                      'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
                      'Mehadia': [('Lugoj', 70), ('Drobeta', 75)],
                      'Drobeta': [('Mehadia', 75), ('Craiova', 120)],
                      'Craiova': [('Drobeta', 120), ('Rimnicu Vilcea', 146), ('Pitesti', 138)],
                      'Rimnicu Vilcea': [('Craiova', 146), ('Sibiu', 80), ('Pitesti', 97)],
                      'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fargaras', 99), ('Rimnicu Vilcea', 80)],
                      'Oradea': [('Sibiu', 115), ('Zerind', 71)],
                      'Fargaras': [('Sibiu', 99), ('Bucharest', 211)],
                      'Pitesti': [('Rimnicu Vilcea', 97), ('Craiova', 138), ('Bucharest', 101)],
                      'Bucharest': [('Pitesti', 101), ('Fargaras', 211), ('Giurgiu', 90), ('Urziceni', 85)],
                      'Giurgiu': [('Bucharest', 90)],
                      'Urziceni': [('Bucharest', 85), ('Vaslui', 142), ('Hirsova', 98)],
                      'Vaslui': [('Urziceni', 142), ('Iasi', 92)],
                      'Iasi': [('Vaslui', 92), ('Neamt', 87)],
                      'Neamt': [('Iasi', 87)],
                      'Hirsova': [('Urziceni', 98), ('Efori', 86)],
                      'Efori': [('Hirsova', 86)]}
        
        self.start = 'Arad'
        self.end = 'Bucharest'
        
        self.straightLineCost = {'Arad': 366,
                                 'Zerind': 374,
                                 'Timisoara': 329,
                                 'Lugoj': 244,
                                 'Mehadia': 241,
                                 'Drobeta': 242,
                                 'Craiova': 160,
                                 'Rimnicu Vilcea': 193,
                                 'Sibiu': 253,
                                 'Oradea': 380,
                                 'Fargaras': 176,
                                 'Pitesti': 100,
                                 'Bucharest': 0,
                                 'Giurgiu': 77,
                                 'Urziceni': 80,
                                 'Vaslui': 199,
                                 'Iasi': 226,
                                 'Neamt': 234,
                                 'Hirsova': 151,
                                 'Efori': 161}
        
        self.solved = False
        self.solution = []
        self.solutionCost = -1

    def getStraightPathCost(self, nodeName):
        return self.straightLineCost[nodeName]
    

    def getAvailableDestinations(self, location):
        return self.graph[location]

    # Returns 0 if the end is not and available destination, the distance otherwise
    def getDestinationOneHopDistance(self, location, destinations):
        for i in range(len(destinations)):
            if (destinations[i])[0] == location:
                return (destinations[i])[1]
        return 0
    
    def getDistanceBetween(self, locationA, locationB):
        destinationsFromA = self.getAvailableDestinations(locationA)
        return self.getDestinationOneHopDistance(locationB, destinationsFromA)

    def getSolution(self):
        return (self.solved, self.solution, self.solutionCost)
    
    def isSolved(self):
        return self.solved
    
    # Test a new solution and log it. Returns True if the problem is solved,
    # False otherwise
    def testAndLogNewSolution(self, path):
        newCost = self.solutionTest(path)
        if (newCost < 0):
            return False
        elif (self.solved == False):
            self.solved = True
            self.solution = path
            self.solutionCost = newCost
        else: # self.solved == True (check if the solution is better)
            if (self.solutionCost > newCost):
                self.solved = True
                self.solution = path
                self.solutionCost = newCost
        return self.solved
    
    def getPathDistance(self, path):
        distanceTravelled = 0
        invalidPath = -1
        
        # Initialize the path check loop
        # Get the start location out of the path and initialize the currentLocation
        currentLocation = path[0]
        
        # Deal with special case where there is either nothing in the path or 
        # the path is length 1
        if (len(path) == 1):
            return distanceTravelled
        elif len(path) < 1:
            return invalidPath
        
        # Measure the path cost
        for i in range(1, len(path)):
        
            # Get the next location from the path (will always be at location 0)
            nextLocation = path[i]
        
            # Is the next location in the path available from current location? Get
            # the available destinations from the current location and then get the
            # distance to the next location, if it's available
            availableDestinations = self.getAvailableDestinations(currentLocation)
            distanceToNextLocation = self.getDestinationOneHopDistance(nextLocation, 
                                                                       availableDestinations)
        
            # Is this location available?
            #    No - return -1
            if (distanceToNextLocation == 0):
                return invalidPath
            
            # Set the current location to the next location
            distanceTravelled = distanceTravelled + distanceToNextLocation
            currentLocation = nextLocation
            
        return distanceTravelled
    
    # Path format: list of location names.
    # Returns the total distance travelled, -1 if not a valid trip
    def solutionTest(self, path):
        # Initialize the distance travelled
        distanceTravelled = 0
        invalidPath = -1
    
        # Make sure the path starts at the start location and ends at the end 
        # location
        if ((path[0] != self.start) or (path[len(path)-1] != self.end)):
            return invalidPath

        # Deal with special case where start == end
        if ((path[0] == self.start) and (self.start == self.end) and 
            len(path) == 0):
            return distanceTravelled
    
        distanceTravelled = self.getPathDistance(path)
        return distanceTravelled
    
        # Test the proposed path
#        for i in range(1, len(path)):
#        
#            # Get the next location from the path (will always be at location 0)
#            nextLocation = path[i]
#        
#            # Is the next location in the path available from current location? Get
#            # the available destinations from the current location and then get the
#            # distance to the next location, if it's available
#            availableDestinations = self.getAvailableDestinations(currentLocation)
#            distanceToNextLocation = self.getDestinationOneHopDistance(nextLocation, 
#                                                                       availableDestinations)
#        
#            # Is this location available?
#            #    No - return -1
#            #    Yes - add distance
#            if (distanceToNextLocation == 0):
#                return invalidPath
#            else:
#                distanceTravelled = distanceTravelled + distanceToNextLocation
#        
#            # Is next location the destination?
#            #    Yes - return distance travelled
#            #    otherwise set the current location to the next location
#            if (nextLocation == self.end):
#                return distanceTravelled
#            else:
#                currentLocation = nextLocation
        
        
        # Out of the loop - didn't reach destination - return -1, something went 
        # wrong
        return invalidPath