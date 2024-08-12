class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
        print(self.next)

class linklist():
    def __init__(self):
        self.head = None
    def append(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next






l1 = linklist()
l1.append(1)
l1.display()