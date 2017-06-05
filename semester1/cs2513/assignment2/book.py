from author import Author

class Book(object):
    """Class to represent a book

        Attributes:
        _title: title of book
        _price: price of book
        _author_name: book author's name
        _publisher: publisher of book
    """

    def __init__(self, title, price, author_name, publisher):
        """Constructor for book
        """
        Author.__init__(self, author_name, publisher)
        self._title = title
        self._price = price
        

    def getTitle(self):
        """Getter for the _title attribute

           Returns:
               An string representing the title
        """
        return self._title
    def setTitle(self, title):
        """Setter for the _title attribute.

            Sets the attribute.
        """
        self._title = title

    def getPrice(self):
        """Getter for the _price attribute

           Returns:
               An int representing the price
        """
        return self._price
    def setPrice(self, price):
        """Setter for the _price attribute.

            Sets the attribute.
        """
        self._price = price

        
    def __str__(self):
        """String method to generate a representation of the book

           Returns:
               string represention of the instance
        """
        return ("Title: %s - Price: %.2f - %s" % (
            self._title, self._price, Author.__str__(self)))


def main():
    """Main method that contains our test block
    """
    book = Book("Yo", 4.99, "John","A Books")
    print (book)

if __name__ == "__main__":
    """Execution mode check to bypass tests for imports and run for direct
    execution.
    """
    main()
    

        

