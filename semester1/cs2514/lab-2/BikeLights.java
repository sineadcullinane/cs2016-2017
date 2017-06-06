/**
 * BikeLights public class outlining more specific version of abstract Bike class
 * that contains Front and Rear Light components
 *
 * @author Sinead Cullinane
 */
public class BikeLights extends Bike {
    private FrontLight frontLight;
    private RearLight rearlight;
    
/**
 * Auxillary class representing Front Light component
 */
class FrontLight {
    }

/**
 * Auxillary class representing Rear Light component
 */
class RearLight {
    }

/**
 * Overriden version of getter methods outlined in abstract Bike class
 */
@Override
   String getBrakes( ) {return "Brakes";}
@Override
   String getWheels( ) {return "Wheels"; }
@Override
    String getSaddle( ) {return "Saddle";}  
@Override
    String getHandlebar( ) {return "Handlebar";}

/**
 * Getter for Front and Rear Light components
 */
String getFrontLight( ) {return "Front Light"; }
String getRearLight( ) {return "Rear Light"; }

/**
 * Overriden version of printComponents method from abstract Bike class
 * which adds Front and Rear Light components
 */
@Override
void printComponents( ) {System.out.println("Components:");
                         System.out.println(getBrakes());
                         System.out.println(getWheels());
                         System.out.println(getSaddle());
                         System.out.println(getHandlebar());
                         System.out.println(getFrontLight());
                         System.out.println(getRearLight());
            }

}
