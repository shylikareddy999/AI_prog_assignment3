import csv
import heapq
from collections import defaultdict

def load_graph(filename):
    graph = defaultdict(list)
    
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            src = row['source']
            dest = row['destination']
            dist = int(row['distance'])
            
            # Undirected graph (roads go both ways)
            graph[src].append((dest, dist))
            graph[dest].append((src, dist))
    
    return graph

def dijkstra(graph, start):
    priority_queue = [(0, start)]  # (cost, node)
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    while priority_queue:
        current_cost, current_node = heapq.heappop(priority_queue)

        if current_cost > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            cost = current_cost + weight

            if cost < distances[neighbor]:
                distances[neighbor] = cost
                heapq.heappush(priority_queue, (cost, neighbor))

    return distances


if __name__ == "__main__":
    graph = load_graph("india_roads.csv")
    
    start_city = input("Enter starting city: ")
    
    if start_city not in graph:
        print("City not found in dataset.")
    else:
        distances = dijkstra(graph, start_city)
        
        print(f"\nShortest distances from {start_city}:\n")
        for city, dist in sorted(distances.items()):
            print(f"{city:15} : {dist}")