A* Algorithm for UGV Navigation with Dynamic Obstacles

Introduction
This program simulates the navigation of an Unmanned Ground Vehicle (UGV) in a grid environment using the A* search algorithm. The grid contains obstacles, and additional dynamic obstacles may appear during navigation, requiring the system to replan its path.

Problem Description
The objective is to move a UGV from a starting position to a goal position in a grid while avoiding obstacles. Since the environment can change dynamically, the algorithm must recompute paths when new obstacles block the current route.

Grid Representation
The environment is represented as a 2D grid of fixed size (70 x 70). Each cell in the grid can either be free (0) or blocked by an obstacle (1). The start position is at (0, 0) and the goal position is at (69, 69).

Obstacle Generation
Obstacles are randomly placed in the grid based on a chosen density level:

* Low density: 10% of the grid cells are obstacles
* Medium density: 20% of the grid cells are obstacles
* High density: 30% of the grid cells are obstacles

Dynamic obstacles are also introduced during execution to simulate a changing environment.

Algorithm Explanation
The program uses the A* search algorithm to find the shortest path from the current position to the goal. A heuristic function (Manhattan distance) is used to estimate the cost from the current node to the goal.

The algorithm:

* Uses a priority queue to select the next node with the lowest cost
* Maintains the cost of reaching each node
* Updates paths when a better route is found

If a path becomes blocked due to newly added obstacles, the algorithm replans from the current position.

Implementation Details
The program is written in Python.
The heapq module is used for the priority queue.
The random module is used to generate obstacles dynamically.

Program Flow

* The user selects an obstacle density level
* The grid is generated with random obstacles
* The UGV starts from the initial position
* A* algorithm computes the path to the goal
* Dynamic obstacles may appear during movement
* If the path is blocked, the system replans
* The process continues until the goal is reached or no path exists

Output
The program displays:

* Start and goal positions
* Whether the mission was successful
* Length of the path taken
* Total number of nodes expanded
* Number of times replanning occurred
* The full path traversed by the UGV

Sample Input
Choose obstacle density (low/medium/high): medium

Sample Output
Start: (0, 0)
Goal: (69, 69)
Mission Success: True
Path Length: 150
Nodes Expanded: 3200
Number of Replans: 5

Applications
This type of system is useful in robotics, autonomous vehicles, path planning in dynamic environments, and game AI.

Conclusion
This program demonstrates how the A* algorithm can be applied to dynamic environments where conditions change during execution, requiring adaptive path planning.