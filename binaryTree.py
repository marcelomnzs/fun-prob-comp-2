# Class that represents a node
class Node:
    # Initializes the tree with the given data and the pointers
    def __init__(self, data):
        self.data = data
        self.father = None
        self.leftSon = None
        self.rightSon = None

# Main program

node = Node(10)
print("Data:", node.data)
print("Left:", node.leftSon)
print("Right:", node.rightSon)