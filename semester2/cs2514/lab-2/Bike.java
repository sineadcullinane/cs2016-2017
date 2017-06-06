/**
 * Bike abstract class outlining most general type of bike
 *
 * @author Sinead Cullinane
 */
public abstract class Bike {
    private Brakes brakes;
    private Wheels wheels;
    private Saddle saddle;
    private Handlebar handlebar;
   
/**
 * Auxillary class representing Brakes component
 */
class Brakes {
    }
/**
 * Auxillary class representing Wheels component
 */
class Wheels {
	}
/**
 * Auxillary class representing Saddle component
 */
class Saddle {
	}
/**
 * Auxillary class representing Handlebar component
 */
class Handlebar {
	}

/**
 * Abstract getter methods for all components
 */
abstract String getBrakes( );
abstract String getWheels( );
abstract String getSaddle( );
abstract String getHandlebar( );

/**
 * Abstract method that prints out components of the Bike class
 */
abstract void printComponents( );
    }
