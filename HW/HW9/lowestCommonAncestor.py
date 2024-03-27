class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pAncestor = self.traverse(p, root)
        qAncestor = self.traverse(q, root)
        return self.find_common_from_end(pAncestor, qAncestor)
    
    def traverse(self, node, root):
        arr = []
        arr.append(root.val)
        while node != root:
            if node.val > root.val:
                root = root.right
            elif node.val < root.val:
                root = root.left
            arr.append(root.val)
        return arr

    def find_common_from_end(self, pAncestor, qAncestor):
        sizeP = len(pAncestor)
        sizeQ = len(qAncestor)
        common = None
        for i in range(min(sizeP, sizeQ)):
            if pAncestor[i] == qAncestor[i]:
                common = pAncestor[i]
            else:
                break
        return common

# root = TreeNode(4)
# root.left = TreeNode(3)
# root.right = TreeNode(8)
# root.left.left = TreeNode(1)
# root.right.left = TreeNode(5)
# root.right.right = TreeNode(9)

# p = root.left.left
# q = root.left

# print(root.lowestCommonAncestor(root, p, q))
