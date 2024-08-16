class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

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
            current.next = new_node
    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.nextn

    def delete_head(self):
        if self.head is not None:
            self.head = self.head.next
    def delete_node(self,data):
        if self.head is not None:
            if self.head.data == data:
                self.head = self.head.next
            else:
                current = self.head
                while current:
                    if current.next.data == data:
                        current.next = current.next.next
                        print("successfully Removed")
                        break
                    current = current.next




l1 = linklist()
l1.append(1)
l1.append(2)
l1.append(3)
l1.append(4)



print("Delete node")

l1.delete_node(4)

l1.display()