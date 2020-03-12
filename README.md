Welcome to SAVI A*

This is a ROS node that performs A* search on a map.

The user must provide the details of the map nodes in both json files in the scripts folder.
- nodeGraph.json: A representation of the map as a graph, showing what nodes connect to which and the distances between the.
- nodeLocations.jaon: Provides the absolute locations (x,y) for each node on the map

NOTE: There is no bullet proofing, it is assumed that these files will both be properly updated by the user to accurately reflect the map.

Two message formats are provided. These define the navigationRequests and navigationSolutions. 
navigationProblem: Used for specifying the start and finish locations for the desired journey
navigationSolution: The resulting navigation solution as determined by A* search

This application can be run using the following:
```rosrun savi_a_star searchMain.py```

Subscriber: This node listens for navigationProblem on the mapSearch/problems topic
Publisher: This node publishes navigationSolution on the  mapSearch/solutions topic
