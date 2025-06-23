class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

# Create tree nodes

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

#Traversal

def inorder(node):
    if node:
        inorder(node.left)
        print(node.data)
        inorder(node.right)

print("Inorder Traversal:")
inorder(root)