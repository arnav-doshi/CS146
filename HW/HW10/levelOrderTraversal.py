class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root):
    if root is None:
        return []
    
    queue = []
    queue.append(root)
    finalList = []

    while queue:
        level = []
        size = len(queue)
        
        for count in range(size):
            curr = queue.pop(0)
            level.append(curr.val)
            
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        
        finalList.append(level)
    
    return finalList

# root = TreeNode(4)
# root.left = TreeNode(3)
# root.right = TreeNode(8)
# root.right.right = TreeNode(9)
# root.right.left = TreeNode(5)
# root.left.left = TreeNode(1)

# print(levelOrder(root))
