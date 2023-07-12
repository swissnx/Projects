
import sys
from heapq import heappop, heappush


class Dijkstra:
    def __init__(self):
        self.__graph = None
        self.__source = None
        self.__distances = None
        self.__previous_nodes = None

    def __dijkstra(self):
        queue = [(0, self.__source)]
        while queue:
            current_distance, current_node = heappop(queue)
            if current_distance > self.__distances[current_node]:
                continue
            for neighbor, weight in self.__graph[current_node].items():
                distance = current_distance + weight
                if distance < self.__distances[neighbor]:
                    self.__distances[neighbor] = distance
                    self.__previous_nodes[neighbor] = current_node
                    heappush(queue, (distance, neighbor))

    def __get_input(self):
        num_nodes, num_edges = map(int, input("Enter the number of nodes and edges: ").split())
        self.__graph = [{} for _ in range(num_nodes)]
        for _ in range(num_edges):
            u, v, w = map(int, input("Enter an edge (u v w): ").split())
            self.__graph[u][v] = w
        self.__source = int(input("Enter the source node: "))
        self.__distances = [sys.maxsize] * num_nodes
        self.__distances[self.__source] = 0
        self.__previous_nodes = [None] * num_nodes

    def __print_output(self):
        for node in range(len(self.__graph)):
            path = []
            if node != self.__source:
                current_node = node
                while current_node is not None:
                    path.append(current_node)
                    current_node = self.__previous_nodes[current_node]
                path.reverse()
            print(f"Shortest path from node {self.__source} to node {node}: {' -> '.join(map(str, path))} (distance: {self.__distances[node]})")

    def __run(self):
        try:
            self.__get_input()
            self.__dijkstra()
            self.__print_output()

        except Exception as e:
            print(f"\n\u001b[3m** An error occurred: \u001b[38;5;200m{e}\u001b[0m")

    def run(self):
        return self.__run()


if __name__ == "__main__":
    d = Dijkstra()
    d.run()


""" EXAMPLES
Enter the number of nodes and edges: 4 4
Enter an edge (u v w): 0 1 1
Enter an edge (u v w): 0 2 4
Enter an edge (u v w): 1 2 2
Enter an edge (u v w): 1 3 6
Enter the source node: 0

Enter the number of nodes and edges: 5 6
Enter an edge (u v w): 0 1 2
Enter an edge (u v w): 0 3 1
Enter an edge (u v w): 1 2 3
Enter an edge (u v w): 2 4 5
Enter an edge (u v w): 3 1 4
Enter an edge (u v w): 3 4 6
Enter the source node: 0 """



# ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ DOCUMENTATION ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ #
# This program helps you find the shortest path between a starting point and all other points in a map. Imagine you have a map with cities
# connected by roads of different lengths. This program can tell you the shortest route to take from one city to all other cities on the map.
# It does this using an algorithm called Dijkstra’s algorithm.

# Dijkstra’s algorithm works by exploring the map step by step, always choosing the closest unexplored city to visit next.
# It keeps track of the shortest distance to each city it has visited so far and updates these distances as it finds shorter routes.
# Eventually, it finds the shortest route to all cities on the map.