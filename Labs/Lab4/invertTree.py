from collections import deque

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


def printLevelOrder(root):
    if not root:
        return

    queue = deque([root])

    while queue:
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.popleft()
            print(node.val, end=" ")

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print()

# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(8)
# root.left.left = TreeNode(3)
# root.left.right = TreeNode(4)
# root.right.left = TreeNode(5)
# root.right.right = TreeNode(6)
        
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(-1)
root.left.left = TreeNode(8)
root.left.left.left = TreeNode(3)
root.left.left.left.left = TreeNode(4)

printLevelOrder(root.invertTree(root))

