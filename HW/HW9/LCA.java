import java.util.ArrayList;

public class LCA {

    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        ArrayList<TreeNode> pAncestor = traverse(p, root);
        ArrayList<TreeNode> qAncestor = traverse(q, root);
        return findCommonFromEnd(pAncestor, qAncestor);
    }

    public static ArrayList<TreeNode> traverse(TreeNode node, TreeNode root) {
        if (node == null) {
            return new ArrayList<>(); 
        }

        ArrayList<TreeNode> arr = new ArrayList<>();
        arr.add(root);
        while (node != root) {
            if (node.val > root.val) {
                root = root.right;
            } else if (node.val < root.val) {
                root = root.left;
            }
            arr.add(root);
        }
        return arr;
    }

    public TreeNode findCommonFromEnd(ArrayList<TreeNode> pAncestor, ArrayList<TreeNode> qAncestor) {
        TreeNode common = null;
        int sizeP = pAncestor.size();
        int sizeQ = qAncestor.size();
        int minLength = Math.min(sizeP, sizeQ);

        for (int i = 0; i < minLength; i++) {
            if (pAncestor.get(i).val == qAncestor.get(i).val) {
                common = pAncestor.get(i);
            } else {
                break;
            }
        }
        return common;
    }

    public static void main(String[] args) {
    //     TreeNode root = new TreeNode(4);
    //     root.left = new TreeNode(3);
    //     root.right = new TreeNode(8);
    //     root.left.left = new TreeNode(1);
    //     root.right.left = new TreeNode(5);
    //     root.right.right = new TreeNode(9);

    //     TreeNode p = root.right.right;
    //     TreeNode q = root.right.left;

    //     LCA classLca = new LCA();
    //     TreeNode treeNode = classLca.lowestCommonAncestor(root, p, q);
    //     System.out.println("Lowest Common Ancestor: " + treeNode.val);
    }
}