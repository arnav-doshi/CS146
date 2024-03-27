class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


    def invertTree(self, root):
        if root is not None:
            temp = root.left
            root.left = self.invertTree(root.right)
            root.right = self.invertTree(temp)
            return root
        return None


# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(8)
# root.left.left = TreeNode(3)
# root.left.right = TreeNode(4)
# root.right.left = TreeNode(5)
# root.right.right = TreeNode(6)
        
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(8)
# root.left.left = TreeNode(3)
# root.left.right = TreeNode(4)
# root.right.left = TreeNode(5)
# root.right.right = TreeNode(6)

# root.invertTree(root)

