class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def addNode(self, val):
        newNode = Node(val)
        self.next = newNode
        
        return newNode