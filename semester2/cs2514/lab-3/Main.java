/**
 * Main constructor class for Animal interface hierarchy
 *
 * @author Sinead Cullinane
 */
public class Main {
    public static void main( final String[] args ) {
        final Animal animal = new Hippo( );
        animal.roam();
        animal.eat();
        animal.makeNoise();
    }
}
