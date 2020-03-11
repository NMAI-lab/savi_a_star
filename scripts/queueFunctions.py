# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 10:38:02 2017

@author: patrickgavigan
"""
from queue import PriorityQueue, LifoQueue, Queue

"""
Search queue - to support the search algorythms.
"""
class SearchQueue:

    """
    Constructor for the queue. default is a fifo.
    """
    def __init__(self, queueType = 'fifo'):
        # Validate queueType (should be fifo, lifo, or priority)
        # Build the queue
        if queueType == 'priority':
            self.q = PriorityQueue()
        elif queueType == 'lifo':
            self.q = LifoQueue()
        else:       # make it a fifo in this case
            self.q = Queue()
    
    """
    Insert data in the queue. Default priority is 0 for non priority queues.
    """
    def insert(self, data, priority = 0):
        self.q.put_nowait((priority, data))
    
    """
    Retrieve data from the queue
    """
    def get(self):
        data = self.q.get_nowait()
        return data[1]
    
    def __str__(self):
        return str(self.q.queue)
    
    """
    Check if the queue is empty
    """
    def empty(self):
        return self.q.empty()