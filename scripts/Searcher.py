# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 11:50:08 2017

@author: patrickgavigan
"""

from queueFunctions import SearchQueue
from anytree import Node, RenderTree
from treeFunctions import getPathFromNode
from graphFunctions import SearchProblem

class Searcher:
    def __init__(self, givenProblem, searchType = 'breadthFirst'):
        self.problem = givenProblem
        self.exploredSet = [self.problem.start]
        self.searchTree = Node(self.problem.start)
        self.type = searchType
        
        self.fifoQueueSearches = ['beadthFirst']
        self.lifoQueueSearches = ['depthFirst']
        self.priorityQueueSearches = ['uniformCost', 'greedyBestFirst', 'aStar']
        
        self.searchType = searchType
        if searchType in self.fifoQueueSearches:
            self.frontierQueue = SearchQueue('fifo')
        elif searchType in self.priorityQueueSearches:
            self.frontierQueue = SearchQueue('priority')
        elif searchType in self.lifoQueueSearches:
            self.frontierQueue = SearchQueue('lifo')
        else:
            self.frontierQueue = SearchQueue('fifo')
            self.searchType = self.fifoQueueSearches[0]
   
        
    def solve(self):
        self.frontierQueue.insert(self.searchTree)
        while (self.problem.isSolved() == False):
            
            # Get next node to expand from the queue
            currentNode = self.frontierQueue.get()
            
            # Try logging the path to the current node as a solution
            self.checkNodeAsSolution(currentNode)
            if (self.problem.isSolved() == True):
                break
            
            # Expand next node in the queue if it isn't in the explored set
            # Will return a cost if a solution is found (for breadth first 
            # search), returns -1 otherwise
            self.expandNode(currentNode)
            if (self.problem.isSolved() == True):
                break

    def checkNodeAsSolution(self, node):
        path = getPathFromNode(node)
        self.problem.testAndLogNewSolution(path)
        

    def expandNode(self, node):
        # Get new destinations
        newNodeList = self.problem.getAvailableDestinations(node.name)
        
        # Generate new nodes
        for i in range(len(newNodeList)):
            # Get the list of the new nodes
            newNodeName = newNodeList[i][0]
            
            # It's not in the explored set, continue (otherwise we skip it)
            instances = self.exploredSet.count(newNodeName)
            if (instances == 0):
                # Add node to the explored set
                self.exploredSet.append(newNodeName)
                
                # Make the new node                
                newNode = Node(newNodeName, node)
                
                # Breadth first searches check the solution when the node is 
                # Generated
                if (self.searchType == 'breadthFirst'):
                    self.checkNodeAsSolution(newNode)
                    if self.problem.isSolved():
                        return
                    
                # Need to deal with the cost in the case where this is a 
                # priority queue
                if self.searchType in self.priorityQueueSearches:
                    # Need to change the next line to reflect the use of other 
                    # heuristics as the priority
                    path = getPathFromNode(node)
                    priority = self.calculatePriority(path, newNodeName)
                    self.frontierQueue.insert(newNode, priority)
                else:
                    self.frontierQueue.insert(newNode)
                
    def calculatePriority(self, path, newNodeName):
        # Initialize to deal with case where there is no priority
        priority = 1
        
        # Calculate cost based on the type of search being performed
        if self.searchType == 'greedyBestFirst':
            straightPathCost = self.problem.getStraightPathCost(newNodeName)
            priority = straightPathCost
        elif self.searchType == 'aStar':
            straightPathCost = self.problem.getStraightPathCost(newNodeName)
            currentPathCost = self.problem.getPathDistance(path)
            priority = straightPathCost + currentPathCost
        elif self.searchType == 'uniformCost':
            currentLocation = path[len(path)-1]
            distanceToNextNode = self.problem.getDistanceBetween(currentLocation, newNodeName)
            priority = distanceToNextNode
        
        return priority
    
    def printSolution(self):
        print('Search Type: ' + self.searchType)
        (solved, solution, cost) = self.problem.getSolution()
        if solved:
            print('Solution path is: ' + str(solution) + 
                  ' and solution cost is: ' + str(cost))
        else:
            print('No solution found')

    def printSearchStructures(self):
        print('Search Tree:')
        
        for pre, fill, node in RenderTree(self.searchTree): 
            print("%s%s" % (pre, node.name))
            
        print('Explored set: ' + str(self.exploredSet))
        print('Frontier queue: ' + str(self.frontierQueue))