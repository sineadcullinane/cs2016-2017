#Name : Sinead Cullinane
#ID : 115329236


class Pet(object):
    """Class to represent a pet

        Attributes:
        _name: name of the pet as a string
        _type: type of the pet as a string
        _age: age of the pet as an integer
    """

    def __init__(self, name, type, age):
        """Constructor for the pet class
        """
        self._name = name
        self._type = type
        self._age = age

    def getName(self):
        """Getter for the _name attribute

           Returns:
               A string representing the name
        """
        return self._name

    def getType(self):
        """Getter for the _type attribute

           Returns:
               A string representing the type
        """
        return self._type

    def getAge(self):
        """Getter for the _age attribute

           Returns:
               An integer representing the age
        """
        return self._age

    def setAge(self, age):
        """Setter for the _age attribute.

            Sets the attribute.
        """
        self._age = age

    def __str__(self):
        """String method to generate a representation of the pet

           Returns:
               string represention of the instance
        """
        return ("Name: %s - Type: %s - Age: %i" % (
            self._name, self._type, self._age))


def main():
    """Main method that contains our test block
    """
    scamp = Pet("Scamp", "Good Dog", 6)
    rosie = Pet("Rosie", "Bad Dog", 10)
    print (scamp)
    print (rosie)
    rosie.setAge(11)
    print (rosie)

if __name__ == "__main__":
    """Execution mode check to bypass tests for imports and run for direct
    execution.
    """
    main()
    
