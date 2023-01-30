class Node:
    left = None
    right = None
    val = 0

    def __init__(self, val):
        self.val = val
    
class BST:
    root = Node(0)

    def insert(self, key):
        node = Node(key)
        if (self.root.left == None and self.root.right == None and self.root.val == 0):
            self.root = node
            return
        
        temp = self.root
        prev = None
        while (temp != None):
            if (temp.val > key):
                prev = temp
                temp = temp.left
            elif (temp.val < key):
                prev = temp
                temp = temp.right
        
        if (prev.val > key):
            prev.left = node
        else:
            prev.right = node
    
    def search(root, key):
        if

tree = BST()
k = [60, 34, 54, 1, 84, 9, 62]
for i in k:
    tree.insert(i)

    tree.search(9)