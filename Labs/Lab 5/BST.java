import java.util.ArrayList;

public class BST {

    public static boolean isValidBST(TreeNode root) {
        ArrayList<Integer> inOrder = new ArrayList<Integer>();
        inOrder = inOrder(root);

        for (int i  = 1; i < inOrder.size(); i++) {
            if (inOrder.get(i-1) > inOrder.get(i)) {
                return false;
            }
        }
        return true;

    }

    public static ArrayList<Integer> inOrder(TreeNode node) {
        ArrayList<Integer> order = new ArrayList<Integer>();
        if (node == null) {
            return order;
        }

        order.addAll(inOrder(node.left));
        order.add(node.val);
        order.addAll(inOrder(node.right));
        return order;
    }

    public static void main(String[] args) {
        TreeNode root;
        root = new TreeNode(3);
        root.left = new TreeNode(2);
        root.right = new TreeNode(4);
        root.left.left = new TreeNode(1);
        root.right.right = new TreeNode(5);

        System.out.println(isValidBST(root));
    }
}