/**
 * Temperature class for Kelvin, Centigrade and Fahrenheit
 *
 * @author Sinead Cullinane
 */

/**
 * The Temperature class
 * The degrees variable, which stores the temperature given in Kelvin
 * The centigrade variable, which will store the temperature in Centigrade 
 * The fahrenheit variable, which will store the temperature in Fahrenheit 
 */
public class Temperature {
    private static double degrees;
    private static double centigrade;
    private static double fahrenheit;
    
/**
 * The constructor for the Temperature class
 */
    public Temperature( double degrees ) {
        this.degrees = degrees;
    }
/**
 * Getter for Kelvin, which gets the degrees (which are already in Kelvin)
 */
    public double getKelvin( ) {
        return Temperature.degrees;
    }
    
/**
 * Getter for Centigrade, which converts the degrees from Kelvin into Centigrade
 */
    public double getCentigrade( ) {
        centigrade = degrees - 273.15;
        return centigrade;
    }
    
/**
 * Getter for Fahrenheit, which converts the degrees from Kelvin to Fahrenheit
 */
    public double getFahrenheit( ) {
        fahrenheit = degrees * 9/5 - 459.67;
        return fahrenheit;
    }
    
/**
 * Printer for Kelvin, which prints the degrees in Kelvin
 */
    public void printKelvin( ) {
        System.out.println("Kelvin: " + getKelvin());
    }
    
/**
 * Printer for Centigrade, which prints the degrees in Centigrade
 */
    public void printCentigrade( ) {
        System.out.println("Centigrade: " + getCentigrade());
    }
    
/**
 * Printer for Fahrenheit, which prints the degrees in Fahrenheit
 */
    public void printFahrenheit( ) {
        System.out.println("Fahrenheit: " + getFahrenheit());
    }
