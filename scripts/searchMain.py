# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 10:38:12 2017

@author: patrickgavigan
"""

# Main file for the search implementation.

from RouteSearcher import RouteSearcher

searcher = RouteSearcher()
solution = searcher.astar('E','B')
print(', '.join(solution))

nextPath = solution[1]
print(nextPath)