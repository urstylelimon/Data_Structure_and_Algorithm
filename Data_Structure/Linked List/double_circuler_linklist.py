class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.prev = self.head
            new_node.next = self.head

        else:
            last_node = self.head.prev
            last_node.next = new_node
            new_node.prev = last_node
            new_node.next = self.head
            self.head.prev = new_node
    def display(self):
        current = self.head
        while current.next:
            value = current.data
            print(value)
            if current.next == self.head:
                break
            current = current.next

    def remove(self,data):
        current = self.head

        while current:
            if current.data == data:
                print('I am in Condition')
                prev_node = current.prev # 4
                next_node = current.next # 2
                prev_node.next = next_node
                next_node.prev = prev_node
                print('----------')
                print(current.data,'Remove Successfully')
                print('----------')
                if current == self.head:
                    self.head = next_node
                break
            current = current.next



l1 = LinkedList()
l1.append(1)
l1.append(2)
l1.append(3)
l1.append(4)

l1.display()

l1.remove(4)

l1.display()