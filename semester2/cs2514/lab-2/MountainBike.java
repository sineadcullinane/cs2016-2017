/**
 * MountainBike public class outlining more specific version of BikeLights class
 * that removes Front and Rear Light compnents and adds Low Frame component
 *
 * @author Sinead Cullinane
 */
public class MountainBike extends BikeLights {
    private LowFrame lowFrame;

/**
 * Auxillary class representing Low Frame component
 */
class LowFrame {
    }

/**
 * Getter for Low Frame component
 */
String getLowFrame( )  {return "Low Frame";}
    
/**
 * Overriden version of printComponents method from BikeLights class
 * which removes Front and Rear Light components and adds Low Frame component
 */
@Override
void printComponents( ) {System.out.println("Components:");
                         System.out.println(getBrakes());
                         System.out.println(getWheels());
                         System.out.println(getSaddle());
                         System.out.println(getHandlebar());
                         System.out.println(getLowFrame());
            }
}
