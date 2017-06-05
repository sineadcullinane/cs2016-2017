from author import Author
from book import Book

class EBook(Book):
    """Class to represent an ebook

        Attributes:
        _title: title of ebook
        _price: price of ebook
        _author_name: ebook author's name
        _publisher: publisher of ebook
        _url = url of ebook
    """

    def __init__(self, title, price, author_name, publisher, url):
        """Constructor for ebook
        """
        Book.__init__(self, title, price, author_name, publisher)
        self._url = url


    def getURL(self):
        """Getter for the _url attribute

           Returns:
               An string representing the url
        """
        return self._url
    def setURL(self, url):
        """Setter for the _url attribute.

            Sets the attribute.
        """
        self._url = url
    

        
    def __str__(self):
        """String method to generate a representation of the book

           Returns:
               string represention of the instance
        """
        return ("Title: %s - Price: %.2f - %s - URL: %s" % (
            self._title, self._price, Author.__str__(self), self._url))


def main():
    """Main method that contains our test block
    """
    ebook = EBook("Yo", 4.99, "John","A Books","www.bruh.com/ebook")
    print (ebook)

if __name__ == "__main__":
    """Execution mode check to bypass tests for imports and run for direct
    execution.
    """
    main()
    

        

