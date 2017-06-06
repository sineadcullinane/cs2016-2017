/**
 * Hippo class that implements Animal interface
 *
 * @author Sinead Cullinane
 */
public class Hippo implements Animal {
    /*
    * Attributes associated with the Hippo class
    */
    private static final int hungerLevel = 10;
    private static final String picture = "hippo.pg";
    public final boolean eatsGrass = true;

    /*
    * Override all interface methods defined in the Animal interface
    */
    @Override
    public void eat( ) {
        System.out.println( "Eating " + hungerLevel + " portions of " + food( ) + "." );
        }
    
    @Override
    public String food( ) {
        return (eatsGrass ? "grass" : "meat");
        }
        
    @Override
    public void makeNoise( ) {
        System.out.println("Grunt.");
        }
        
    @Override
    public void roam( ) {
        System.out.println("I'm lazy: not roaming.");
        }
}
