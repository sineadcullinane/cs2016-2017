/**
 * Main constructor class for generic class Tree
 *
 * @author Sinead Cullinane
 */
public class Main {
    public static void main(String [ ] args) {
        final Tree<Integer> tree = new Tree<Integer>( );

        tree.insert( 1 );
        tree.insert( 2 );
        tree.insert( 0 );

        tree.showPreOrder();
        tree.showInOrder();
        tree.showPostOrder();
    }
}
