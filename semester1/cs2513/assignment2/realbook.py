from author import Author
from book import Book

class RealBook(Book):
    """Class to represent a book

        Attributes:
        _title: title of book
        _price: price of book
        _postage: postage cost of book
        _total_cost: total cost of book
        _author_name: book author's name
        _publisher: publisher of book
    """

    def __init__(self, title, price, postage, author_name, publisher):
        """Constructor for book
        """
        Book.__init__(self, title, price, author_name, publisher)
        self._postage = postage
        self._total_cost = self._price + self._postage

    
    def getPostage(self):
        """Getter for the _postage attribute

           Returns:
               An int representing the postage
        """
        return self._postage
    def setPostage(self, postage):
        """Setter for the _postage attribute.

            Sets the attribute.
        """
        self._postage = postage

    def getTotalCost(self):
        """Getter for the _total_cost attribute

           Returns:
               An int representing the total_cost
        """
        return self._total_cost

        
    def __str__(self):
        """String method to generate a representation of the book

           Returns:
               string represention of the instance
        """
        return ("Title: %s - Price: %.2f - Postage: %.2f - Total Cost: %.2f - %s" % (
            self._title, self._price, self._postage, self._total_cost, Author.__str__(self)))


def main():
    """Main method that contains our test block
    """
    book = RealBook("Yo", 4.99, 2.00, "John","A Books")
    print (book)

if __name__ == "__main__":
    """Execution mode check to bypass tests for imports and run for direct
    execution.
    """
    main()
    

        
