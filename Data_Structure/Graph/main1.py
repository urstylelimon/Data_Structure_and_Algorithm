class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self,node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self,node1,node2):
        if node1 not in self.graph:
            self.graph[node1] = []
        if node2 not in self.graph:
            self.graph[node2] = []

        self.graph[node1].append(node2)



    def main(self):
        flag = True
        while flag:
            node1 = str(input("Enter the first node: "))
            node2 = str(input("Enter the second node: "))

            if flag:
                self.add_node(node1)
                print(self.graph)
            if node1 == "quit":
                flag = False

p = Graph()
p.main()