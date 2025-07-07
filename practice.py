class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class linklist():
    def __init__(self):
        self.head = None
    def insert(self,data):
        if self.head is None:
            self.head = Node(data)
        elif self.head is not None:

            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(data)

            print(self.head.next.data)


j = linklist()
j.insert(1)
j.insert(2)