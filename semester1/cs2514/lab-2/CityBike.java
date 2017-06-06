/**
 * CityBike public class outlining more specific version of BikeLights class
 * that adds High Frame component and Carrier component
 *
 * @author Sinead Cullinane
 */
public class CityBike extends BikeLights {
    private HighFrame highFrame;
    private Carrier carrier;

/**
 * Auxillary class representing High Frame component
 */
class HighFrame {
    }

/**
 * Auxillary class representing Carrier component
 */
class Carrier {
    }

/**
 * Getter for High Frame component
 */
String getHighFrame( )  {return "High Frame"; }

/**
 * Getter for Carrier component
 */
String getCarrier( )  {return "Carrier"; }
    
/**
 * Overriden version of printComponents method from BikeLights class
 * which adds Medium Frame component and Carrier component
 */
@Override
void printComponents( ) {super.printComponents( );
                         System.out.println(getHighFrame());
                         System.out.println(getCarrier());
            }
}
