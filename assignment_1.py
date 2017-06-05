class Light(object):
    """Class to represent a light

       Class to represent a light and provide a description of its
       state and power in wattage.

       Attributes:
          _state = State of light (on or off)
          _power = The lights power in wattage
    """

    def __init__ (self, state, power):
        """Constructor for the light

           Args:
                state: a string value representing state of light (on or off).
                power: numeric value representing power of light in wattage.
        """

        if power is None or power < 0:
            print("Power is invalid")

        self._state = state
        self._power = power



    def switchLight(self):
        """Method to switch the light from its current state.
        """

        if self._state == "Off":
            self._state = "On"
        else:
            self._state = "Off"
            
    def getState (self):
        """Getter for _state attribute.

           Returns:
               string representation of the state
        """
        return self._state

    state = property(getState)

        
    def getPower (self):
        """Getter for _power attribute.

           Returns:
               int representation of the power
        """
        return self._power
    def setPower (self, power):
        """Setter for _power attribute
        """
        if power is None or power < 0:
            print("Power is invalid")
        else:
            self._power = power

    power = property(getPower, setPower)


    def __str__(self):
        """String method to generate a representation of the light.

           Returns:
              string representation of the instance.
        """
        descriptive_str = ("State: %s - Power: %i" % (self.state, self.power))

def main():
    """Main method that contains our test block
    """

    light1 = Light('On', 50)
    print(light1.state, light1.power)
    
    light1.setPower(40)
    print(light1.state, light1.power)

    light1.switchLight()
    print(light1.state, light1.power)

if __name__ == '__main__':
    """Execution mode check to bypass tests for imports and run for direct
       execution.
    """
    main()
