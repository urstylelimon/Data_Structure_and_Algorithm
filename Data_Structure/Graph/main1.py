class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self,node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self,node1,node2):
        if node1 not in self.graph:
            print(f"{node1} not in graph, please create first")
        if node2 not in self.graph:
            print(f"{node2} not in graph, please create first")
        if node1 and node2 in self.graph:
            if node2 in self.graph[node1]:
                print(f"{node1} already connected with {node2}")
            elif node2 not in self.graph[node1]:
                self.graph[node1].append(node2)

    def display(self):
        for node in self.graph:
            print(f"{node} is connectd with {self.graph[node]}")



    def main(self):


        while True:

            user = str(input("For add new node pres 1\nConnect between two nood press 2\nFor display all press 3\nquit application type quit\n"))
            if user == "1":
                node = str(input("Enter the node:\n"))
                self.add_node(node)
                print("Successfully added ndoe ", node)

            if user == "2":
                node1 = str(input("Enter the node:\n"))
                node2 = str(input("Enter the node:\n"))
                self.add_edge(node1,node2)

                self.display()
            if user == "3":
                self.display()

            if user == "quit" :
                break
p = Graph()
p.main()