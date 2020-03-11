# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 10:38:12 2017

@author: patrickgavigan
"""

# Main file for the search implementation.

from Searcher import Searcher
from graphFunctions import SearchProblem

searchType = ['beadthFirst', 
              'depthFirst', 
              'uniformCost', 
              'greedyBestFirst', 
              'aStar']

for i in range(len(searchType)):
    problem = SearchProblem()
    searcher = Searcher(problem, searchType[i])
    searcher.solve()
    searcher.printSolution()
    searcher.printSearchStructures()