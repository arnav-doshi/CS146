import java.util.*;

public class LevelOrderTraversal {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> finalList = new ArrayList<>();
        if (root == null) {
            return finalList;
        }
        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        queue.add(root);

        while (!queue.isEmpty()) {    
            List<Integer> level = new ArrayList<Integer>();
            int size = queue.size();

            for (int i = 0; i < size; i++) {
                TreeNode curr = queue.poll();
                level.add(curr.val);

                if (curr.left != null)
                    queue.add(curr.left);
                if (curr.right != null)
                    queue.add(curr.right);
            }
            finalList.add(level);
        }
        return finalList;
     }


     public static void main(String[] args) {
        // TreeNode root = new TreeNode(4);
        // root.left = new TreeNode(3);
        // root.right = new TreeNode(8);
        // root.left.left = new TreeNode(1);
        // root.right.left = new TreeNode(5);
        // root.right.right = new TreeNode(9);

        // LevelOrderTraversal l = new LevelOrderTraversal();
        // System.out.println(l.levelOrder(root));
     }
 
}
