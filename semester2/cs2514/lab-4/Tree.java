/**
 * Generic class for binary trees, which contains a node class
 * TreeNode which defines a node for the binary tree, and methods
 * to insert items into the tree, and methods to print the tree
 * using in-order, pre-order, and post-order traversal
 *
 * @author Sinead Cullinane
 */

public class Tree< T extends Comparable<T>> {
    private TreeNode node;
    /**
     * Reference to the root node of the tree
     */
    private TreeNode root;
    /**
     *  Node class representing each node of the tree 
     * Containing a value treeNode, and references to the nodes
     * leftChild and rightChild
     */
    private class TreeNode {
        T treeNode;
        TreeNode leftChild;
        TreeNode rightChild;

        public TreeNode(T treeNode) {
            this.treeNode = treeNode;
        }
    }

    /**
     *  Method to check whether the tree is empty
     */
    public boolean isEmpty() {
        return node == null;
    }

    /**
     * Insert method to insert nodes into the tree
     * This is the general method the user will interact with
     * It inserts the node into the tree if the tree is empty
     * and calls a seperate method if the tree is non-empty
     */
    public void insert(T nodeValue) {
        if(isEmpty()) {
            node = new TreeNode(nodeValue);
            /**
             * Make this first inserted node the root node
             */
            root = node;
        }
        else {
            insert(node, nodeValue);
        }
    }

    /**
     * Recursive insert method to insert nodes into the tree
     * This is the more sophisticated method that
     * is hidden from the user
     * It uses the compareTo method to compare the newest node
     * to the left and right children of the tree node and insert
     * depending on whether the node is smaller or bigger than
     * the root node
     */
    private void insert(TreeNode node, T nodeValue) {

        if(nodeValue.compareTo(node.treeNode) < 0) {
            if(node.leftChild == null)
                node.leftChild = new TreeNode(nodeValue);
            else
                insert(node.leftChild, nodeValue);
        }
        else {
            if(node.rightChild == null)
                node.rightChild = new TreeNode(nodeValue);
            else
                insert(node.rightChild, nodeValue);
        }
    }
    
    /**
     * Method to print tree using in-order traversal
     * This is the public method the user will interact with
     * which calls a private method of the same name
     */
    public void showInOrder ( ) {
        showInOrder(root);
        System.out.println();
    }

    /**
     * Method to print tree using in-order traversal
     * This is the more sophisticated method that
     * is hidden from the user
     * It takes in the root node and recursively prints
     * using in-order traversal
     */
    private void showInOrder (TreeNode node) {
        if (node == null) return;

        showInOrder(node.leftChild);
        System.out.println(node.treeNode + " ");
        showInOrder(node.rightChild);
    }

    /**
     * Method to print tree using post-order traversal
     * This is the public method the user will interact with
     * which calls a private method of the same name
     */
    public void showPostOrder ( ) {
        showPostOrder(root);
        System.out.println();
    }

    /**
     * Method to print tree using post-order traversal
     * This is the more sophisticated method that
     * is hidden from the user
     * It takes in the root node and recursively prints
     * using post-order traversal
     */
    private void showPostOrder (TreeNode node) {
        if (node == null) return;

        showPostOrder(node.leftChild);
        showPostOrder(node.rightChild);
        System.out.println(node.treeNode + " ");
    }

    /**
     * Method to print tree using pre-order traversal
     * This is the public method the user will interact with
     * which calls a private method of the same name
     */
    public void showPreOrder ( ) {
        showPreOrder(root);
        System.out.println();
    }

    /**
     * Method to print tree using pre-order traversal
     * This is the more sophisticated method that
     * is hidden from the user
     * It takes in the root node and recursively prints
     * using pre-order traversal
     */
    private void showPreOrder (TreeNode node) {
        if (node == null) return;

        System.out.println(node.treeNode + " ");
        showPreOrder(node.leftChild);
        showPreOrder(node.rightChild);
    }

}
