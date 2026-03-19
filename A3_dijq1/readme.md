Dijkstra’s Algorithm on Indian Cities using CSV Data

Introduction-
This program implements Dijkstra’s Algorithm (also known as Uniform Cost Search) to calculate the shortest distance from a selected starting city to all other cities. The graph is created using road distance data stored in a CSV file.

Problem Description-
In a graph where each connection has a different cost (distance), the objective is to find the minimum distance from one node to all other nodes. Dijkstra’s Algorithm is used because it efficiently solves shortest path problems for graphs with non-negative weights.

Data Handling-
The program reads input from a CSV file named "india_roads.csv". Each row contains a source city, a destination city, and the distance between them. The graph is treated as undirected, meaning travel is possible in both directions.

Graph Representation-
The graph is stored as an adjacency list using a dictionary. Each city maps to a list of neighboring cities along with their respective distances.

Algorithm Explanation-
The algorithm uses a priority queue to always select the city with the smallest current distance. It initializes all distances to infinity except the starting city, which is set to zero. It then updates the distances of neighboring cities whenever a shorter path is found. This process continues until all reachable cities have been processed.

Implementation Details-
The program is written in Python.
The csv module is used to read the dataset.
The heapq module is used to implement the priority queue.
The collections module is used to build the graph efficiently using defaultdict.

How to Run-

1. Make sure Python is installed on your system.
2. Place the file "india_roads.csv" in the same directory as the program.
3. Run the program using:
   python filename.py

Program Flow-

* The program loads the graph from the CSV file
* It asks the user to enter a starting city
* It checks whether the city exists in the dataset
* It computes the shortest distances to all other cities
* It prints the distances in sorted order

Sample Input
Enter starting city: Delhi

Sample Output
Shortest distances from Delhi:

Delhi           : 0
Agra            : 233
Chandigarh      : 244
Jaipur          : 281
Lucknow         : 555
Mumbai          : 1420

Applications-
This implementation can be used in navigation systems, route planning, logistics optimization, and network routing.

Conclusion-
This program demonstrates how Dijkstra’s Algorithm can be applied to real-world datasets to compute shortest distances efficiently from a single source to all other nodes in a graph.
