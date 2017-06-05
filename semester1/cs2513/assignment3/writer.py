"""Import shelve functionality
"""
import shelve
from pet import Pet

"""Create instances of the classes
"""
scamp = Pet("Scamp", "Good Dog", 6)
rosie = Pet("Rosie", "Bad Dog", 10)

"""Open the shelve, assign objects to the shelve, then close the shelve
"""
db = shelve.open("pets")
db[scamp._name] = scamp
db[rosie._name] = rosie
db.close

def main():
    """Main method that contains our test block
    """
    db = shelve.open("pets")
    scamp = db["Scamp"]
    rosie = db["Rosie"]
    db.close
    print (scamp)
    print (rosie)

if __name__ == "__main__":
    """Execution mode check to bypass tests for imports and run for direct
    execution.
    """
    main()
