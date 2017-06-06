/**
 * HybridBike public class outlining more specific version of BikeLights class
 * that contains Medium Frame component
 *
 * @author Sinead Cullinane 115329236
 */
public class HybridBike extends BikeLights {
    private MediumFrame mediumFrame;

/**
 * Auxillary class representing Medium Frame component
 */
class MediumFrame {
    }

/**
 * Getter for Medium Frame component
 */
String getMediumFrame( )  {return "Medium Frame"; }

/**
 * Overriden version of printComponents method from BikeLights class
 * which adds Medium Frame component
 */
@Override
void printComponents( ) {super.printComponents( );
                         System.out.println(getMediumFrame());
            }
}
