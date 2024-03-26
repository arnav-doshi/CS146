
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


def isValidBST(root):
    y = inOrder(root)
    for i in range(1, len(y)):
        if y[i] < y[i-1]:
            return False
    return True


def inOrder(root):
    x = []
    if root is None:
        return x
    x.extend(inOrder(root.left))
    x.append(root.val)
    x.extend(inOrder(root.right))
    return x



# root = TreeNode(4)
# root.left = TreeNode(4)
# root.left.left = TreeNode(4)
# root.left.left.left = TreeNode(3)
# root.left.left.left.left = TreeNode(1)

# root.right = TreeNode(8)
# root.right.left = TreeNode(5)
# root.right.right = TreeNode(9)

root = TreeNode(3)
root.left = TreeNode(2)
root.right = TreeNode(4)
root.left.left = TreeNode(1)
root.right.right = TreeNode(5)

print(isValidBST(root))
    