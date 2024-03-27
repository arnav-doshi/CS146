import java.util.LinkedList;
import java.util.Queue;

public class invert {
    
    public static TreeNode invertTree(TreeNode root) {
        if (root == null)
        return null;

        TreeNode temp = root.left;
        root.left = invertTree(root.right);
        root.right = invertTree(temp);

        return root;
    }

    public static void main(String[] args) {
        // TreeNode root = new TreeNode(4);
        // root.left = new TreeNode(2);
        // root.right = new TreeNode(7);
        // root.left.left = new TreeNode(1);
        // root.left.right = new TreeNode(3);
        // root.right.left = new TreeNode(6);
        // root.right.right = new TreeNode(9);

        // TreeNode root = new TreeNode(1);
        // root.left = new TreeNode(2);
        // root.right = new TreeNode(8);
        // root.left.left = new TreeNode(3);
        // root.left.right = new TreeNode(4);
        // root.right.left = new TreeNode(5);
        // root.right.right = new TreeNode(6);
        // invertTree(root);
    }

}