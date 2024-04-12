class Node:
    def __init__(self, data):
        self.data = data
        self.color = 'RED'  # NEW NODES AS RED
        self.left = None
        self.right = None
        self.parent = None

class RBtree:
    def __init__(self):
        self.root = None

    def inOrderTraversal(self, node):
        if node is not None and node.data is not None:
            self.inOrderTraversal(node.left)
            print(str(node.data) + " ")
            self.inOrderTraversal(node.right)


    def leftRotation(self, node):
        right = node.right

        if not right:
            return node
        
        node.right = right.left

        if right.left:
            right.left.parent = node

        right.parent = node.parent

        if not node.parent:
            self.root = right
        elif node == node.parent.left:
            node.parent.left = right
        else:
            node.parent.right = right

        right.left = node
        node.parent = right

        return right

    def rightRotation(self, node):
        left = node.left

        if not left:
            return node
        
        node.left = left.right

        if left.right:
            left.right.parent = node

        left.parent = node.parent

        if not node.parent:
            self.root = left
        elif node == node.parent.right:
            node.parent.right = left
        else:
            node.parent.left = left

        left.right = node
        node.parent = left

        return left

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
            self.root.color = 'BLACK'
        else:
            self.root = self.insertionHelper(self.root, data)
            self.root.color = 'BLACK'  # THE ROOT IS ALWAYS BLACK

    def insertionHelper(self, root, data):
        if not root:
            return Node(data)

        if data < root.data:
            root.left = self.insertionHelper(root.left, data)
            root.left.parent = root

        elif data > root.data:
            root.right = self.insertionHelper(root.right, data)
            root.right.parent = root

        if self.redOrNot(root.right) and not self.redOrNot(root.left):
            root = self.leftRotation(root)

        if self.redOrNot(root.left) and self.redOrNot(root.left.left):
            root = self.rightRotation(root)

        if self.redOrNot(root.left) and self.redOrNot(root.right):
            self.switchColor(root)

        return root

    def redOrNot(self, node):
        if not node:
            return False
        return node.color == 'RED'

    def switchColor(self, node):
        node.color = 'RED'
        node.left.color = 'BLACK'
        node.right.color = 'BLACK'

    



    def deleteNode(self, node):
        if not node:
            return
        
        if node.left and node.right:
            successor = self.findSuccessor(node)
            node.data = successor.data
            self.deleteNode(successor)

        else:

            if node.right:
                child = node.right
            else:
                child = node.left

            if self.redOrNot(node):
                if not child:
                    child = Node(None)
                    child.color = 'BLACK'
                else:
                    child.color = 'BLACK'

            elif self.redOrNot(child):
                child.color = 'BLACK'

            else:
                doubleBlack = Node(None)
                doubleBlack.parent = node.parent

                if node == node.parent.left:
                    node.parent.left = doubleBlack
                else:
                    node.parent.right = doubleBlack
                self.fixDoubleBlack(doubleBlack)

            if node == node.parent.left:
                node.parent.left = child
            else:
                node.parent.right = child

            if child:
                child.parent = node.parent
    
    def findSuccessor(self, node):
        successor = node.right

        while successor.left:
            successor = successor.left
        return successor
    

    def getSibling(self, node):
        if node is self.root:
            return None
        
        if node is node.parent.left:
            return node.parent.right
        
        return node.parent.left
    

    def fixDoubleBlack(self, node):
        if node == self.root: #base case
            return
        
        sibling = self.getSibling(node)
        parent = node.parent

        if not sibling:
            self.fixDoubleBlack(parent)
        else:
            if self.redOrNot(sibling):
                parent.color = 'RED'
                sibling.color = 'BLACK'
                if sibling == parent.left:
                    self.rightRotation(parent)
                else:
                    self.leftRotation(parent)
                self.fixDoubleBlack(node)
            else:
                if self.redOrNot(sibling.left) or self.redOrNot(sibling.right):
                    if sibling.left and self.redOrNot(sibling.left):
                        if sibling == parent.left:
                            sibling.left.color = sibling.color
                            sibling.color = parent.color
                            self.rightRotation(parent)
                        else:
                            sibling.left.color = parent.color
                            self.rightRotation(sibling)
                            self.leftRotation(parent)
                    else:
                        if sibling == parent.left:
                            sibling.right.color = parent.color
                            self.leftRotation(sibling)
                            self.rightRotation(parent)
                        else:
                            sibling.right.color = sibling.color
                            sibling.color = parent.color
                            self.leftRotation(parent)
                    parent.color = 'BLACK'
                else:
                    sibling.color = 'RED'
                    if not self.redOrNot(parent):
                        self.fixDoubleBlack(parent)
                    else:
                        parent.color = 'BLACK'


    def search(self, data):
        return self.searchHelper(self.root, data)

    def searchHelper(self, node, data):
        if not node or node.data == data: #base case
            return node
        if data < node.data:
            return self.searchHelper(node.left, data)
        else:
            return self.searchHelper(node.right, data)
    
    
        
#testing

insertionArray = [99, 2, 5, 1, 6, 17, -4, 2555, 0]
tree = RBtree()

for i in range(len(insertionArray)):
    tree.insert(insertionArray[i])

x = tree.search(17)
if x:
    tree.deleteNode(x)
else:
    print("Node 17 not found")

tree.inOrderTraversal(tree.root)


# Used pseudocode from wikipedia