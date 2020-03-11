# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 09:53:29 2017

@author: patrickgavigan
"""

from anytree import Node, RenderTree
#from anytree.exporter import DotExporter

# Basic tree from the online tutorial
# https://pypi.python.org/pypi/anytree

#class searchTree(self):
#    def __init__(self, start):
#        self.root = Node(start)

def buildBasicTree():
    udo = Node("Udo")
    marc = Node("Marc", parent=udo)
    lian = Node("Lian", parent=marc)
    dan = Node("Dan", parent=udo)
    jet = Node("Jet", parent=dan)
    jan = Node("Jan", parent=dan)
    joe = Node("Joe", parent=dan)
        
    for pre, fill, node in RenderTree(udo): 
        print("%s%s" % (pre, node.name))
        
    returnPath = []
    for i in range (len(joe.path)):
        returnPath.append(joe.path[i].name)
    print(returnPath)
    
    # Gets the path from an end node.
def getPathFromNode(node):
    returnPath = []
    for i in range (len(node.path)):
        returnPath.append(node.path[i].name)
    return returnPath