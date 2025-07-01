class Graph:
    def __init__(self):
        self.graph = {}  # adjacency list

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, node1, node2):
        # Make sure both nodes exist
        if node1 not in self.graph:
            self.add_node(node1)
        if node2 not in self.graph:
            self.add_node(node2)

        # For undirected graph, add both ways
        self.graph[node1].append(node2)
        self.graph[node2].append(node1)

    def show_graph(self):
        for node in self.graph:
            print(f"{node} is connected to {self.graph[node]}")


g = Graph()

g.add_node('A')
g.add_node('B')

g.add_edge('A', 'B')


g.show_graph()