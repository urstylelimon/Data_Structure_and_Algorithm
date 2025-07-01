graph = {
    'A' : ['B','C'],
    'B' : ['A','D'],
    'C' : ['A'],
    'D' : ['B'],
    'E' : ['C'],
    'F' : ['D'],

}


for node in graph:
    print(f"{node} is connected with {graph[node]}")