/**
 * Main constructor class for Temperature.java
 * Takes in the degrees in Kelvin and prints the degrees out in Kelvin,
 * Centigrade and Fahrenheit
 *
 * @author Sinead Cullinane
 */
    
    public static void main( String[] args ) {
        Temperature firstDegree = new Temperature( 10 );
        
        firstDegree.printKelvin( );
        firstDegree.printCentigrade( );
        firstDegree.printFahrenheit( );
      }
}
