class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class DoubleLinkedList():
    def __init__(self):
        self.head = None

    def insert(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def display(self):
        current = self.head
        while current:
            print(current.data)
            if current.prev is None:
                print(' -> None')
            else:
                print("Previos Value : ", current.prev.data)
            current = current.next

l1 = DoubleLinkedList()
l1.insert(1)
l1.insert(2)
l1.insert(3)
l1.insert(4)

l1.display()