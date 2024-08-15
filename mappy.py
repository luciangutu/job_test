#!/bin/python3

# https://www.boot.dev/signup-flow

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph.keys():
            self.graph[u].add(v)
        else:
            self.graph[u] = {v}
        if v in self.graph.keys():
            self.graph[v].add(u)
        else:
            self.graph[v] = {u}
        # don't touch below this line


def main():
    graph = Graph()
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 4)
    graph.add_edge(4, 3)
    graph.add_edge(1, 3)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)

    print(f"graph vertex: 0 connects to: {graph.graph[0]}")
    print(f"graph vertex: 1 connects to: {graph.graph[1]}")
    print(f"graph vertex: 2 connects to: {graph.graph[2]}")
    print(f"graph vertex: 3 connects to: {graph.graph[3]}")
    print(f"graph vertex: 4 connects to: {graph.graph[4]}")


main()
