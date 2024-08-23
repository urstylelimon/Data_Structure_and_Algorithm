class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Single_Ciruler_LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.head.next = new_node
        else:
            current =self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
            if current == self.head:
                break


l1 = Single_Ciruler_LinkedList()
l1.append(1)
l1.append(2)
l1.append(3)
l1.append(4)
l1.append(5)
l1.display()