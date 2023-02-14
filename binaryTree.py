# Class that represents a node
class Node:
    # Initializes the tree with the given data and the pointers
    def __init__(self, data):
        self.data = data
        self.father = None
        self.leftSon = None
        self.rightSon = None

    # Returns the data of a given node
    def getData(self):
        return self.data
    
    # Returns the left son of a given node
    def getLeft(self):
        return self.leftSon
    
    # Returns the right son of a given node
    def getRight(self):
        return self.rightSon
    
    # Returns the father of a given node
    def getFather(self):
        return self.father
    
    # Returns the brother of a given not, if it exists
    def getBrother(self):
        # Verifies if the father exists
        if self.getFather() == None:
            return False
        
        # Verifies if the given node is on the left side, if it is, then its brother is in the other side
        if self.isLeft():
            return self.getFather().getRight()
        
        # If the given node isn't on the left side, by inference the brother is
        return self.getFather().getLeft()

    # Verifies if the given node is the left son of its father
    def isLeft(node):
        # Gets the father of the given node
        pointer = node.getFather()

        # If there's no father, then the node is pointing at the root 
        if pointer == None:
            return False
        
        # If the left son of the pointer is equal to the node, than he's the left son
        if pointer.getLeft() == node:
            return True
        
        # If none of the conditions are true, than the given node isn't the left son
        return False
    
    # Verifies if the given node is the right son of its father
    def isRight(node):
        # Gets the father of the given node
        pointer = node.getFather()

        # If there's no father, then the node is pointing at the root 
        if pointer == None:
            return False
        
        # If the right son of the pointer is equal to the node, than he's the right son
        if pointer.getRight() == node:
            return True
        
        # If none of the conditions are true, than the given node isn't the right son
        return False