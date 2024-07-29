class Node:
    def __init__(self, value):
        self.value = value
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            n = self.head
            while n is not None:
                print(n.value)
                n = n.ref
l1 = LinkedList()
print(l1.print_LL())