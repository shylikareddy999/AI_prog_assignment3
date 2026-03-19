A* Algorithm for UGV Path Planning with Static Obstacles

Introduction
This program implements the A* search algorithm to find a path for an Unmanned Ground Vehicle (UGV) in a grid environment with static obstacles. The objective is to move from a starting position to a goal position while avoiding blocked cells.

Problem Description
The task is to determine a valid path in a grid where some cells are blocked by obstacles. The algorithm must find the shortest path from the start to the goal while navigating around these obstacles. Since the environment is static, obstacles do not change during execution.

Grid Representation
The environment is represented as a 2D grid of size 70 x 70. Each cell in the grid is either free (0) or an obstacle (1). The starting position is fixed at (0, 0) and the goal position is at (69, 69).

Obstacle Generation
Obstacles are randomly generated based on a selected density level:

* Low density: 10% of cells are obstacles
* Medium density: 20% of cells are obstacles
* High density: 30% of cells are obstacles

Algorithm Explanation
The A* algorithm is used to find the shortest path efficiently. It combines the actual cost from the start node and a heuristic estimate to the goal.

The heuristic used is Manhattan distance, which calculates the distance between two grid points based on horizontal and vertical movement.

The algorithm:

* Uses a priority queue to select the next node with the lowest estimated cost
* Keeps track of visited nodes and path costs
* Updates paths when a better route is found
* Stops when the goal is reached

Implementation Details
The program is written in Python.
The heapq module is used for implementing the priority queue.
The random module is used to generate obstacle positions.

Program Flow

* The user selects the obstacle density level
* A grid is generated with random obstacles
* The A* algorithm computes a path from start to goal
* The program prints the results

Output
The program displays:

* Start and goal positions
* Length of the path found
* Number of nodes expanded
* The complete path from start to goal

Sample Input
Choose obstacle density (low/medium/high): low

Sample Output
Start: (0, 0)
Goal: (69, 69)
Path Length: 140
Nodes Expanded: 2500
Path: [(0,0), (0,1), ..., (69,69)]

Applications
This implementation can be used in robotics, game development, autonomous navigation, and pathfinding problems in grid-based environments.

Conclusion
This program demonstrates how the A* algorithm can efficiently compute paths in a static environment with obstacles using a heuristic-based approach.