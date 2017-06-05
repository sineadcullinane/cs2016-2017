class Author(object):
    """Class to represent an author

        Attributes:
        _author_name: author name
        _publisher: author's publisher
    """

    def __init__(self, author_name, publisher):
        """Constructor for author
        """
        self._author_name = author_name
        self._publisher = publisher

        
    def getAuthorName(self):
        """Getter for the _author_name attribute

           Returns:
              A string representing the author's name
        """
        return self._author_name
    
    def setAuthorName(self, author_name):
        """Setter for the _author_name attribute

           Sets the attribute
        """
        
        self._author_name = author_name

    def getPublisher(self):
        """Getter for the _publisher attribute

           Returns:
               A string representing the publisher
        """
        return self._publisher
    def setPublisher(self, publisher):
        """Setter for the _publisher attribute.

            Sets the attribute.
        """
        self._publisher = publisher

    def __str__(self):
        """String method to generate a representation of the author

           Returns:
              string represention of the instance
        """
        return ("Author: %s - Publisher: %s" % (
           self._author_name, self._publisher,))


def main():
    """Main method that contains our test block
    """
    auth = Author("John","A Books")
    print(auth)

if __name__ == "__main__":
    """Execution mode check to bypass tests for imports and run for direct
    execution.
    """
    main()
    
