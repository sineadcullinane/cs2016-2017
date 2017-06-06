/**
 * Main constructor class for Bike classes
 *
 * @author Sinead Cullinane
 */
public class Main {
    public static void main( String[] args ) {
        Bike mountainbike = new MountainBike( );
        Bike citybike = new CityBike( );
        Bike hybridbike = new HybridBike( );
        
        mountainbike.printComponents( );
        citybike.printComponents( );
        hybridbike.printComponents( );
      }
}
