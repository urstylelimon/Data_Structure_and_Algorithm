class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def set_left(self, node):
        self.left = node

    def set_right(self, node):
        self.right = node


# Create nodes
root = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)
node9 = Node(9)
node10 = Node(10)

# Build the tree
root.set_left(node2)
root.set_right(node3)

node2.set_left(node4)
node2.set_right(node5)

node3.set_left(node6)
node3.set_right(node7)

node4.set_left(node8)
node4.set_right(node9)

node5.set_left(node10)


# Postorder traversal
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data)


print("Postorder Traversal of Larger Tree:")
postorder(root)
