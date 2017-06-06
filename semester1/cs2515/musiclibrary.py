class Track:
    """Class to represent a music track

       Attributes:
       _name: Track name
       _artiste: Artiste name
       _timeplayed: Timeplayed
    """
    def __init__(self, name, artiste):
        """Constructor for track class
        """
        self._name = name
        self._artiste = artiste
        self._timesplayed = 0

    def __str__(self):
        """String method to generate a representation of the track
        """
        track_str = ("(Track Name: %s ; Artiste: %s ; Times Played: %i)" % (
                     self._name, self._artiste, self._timesplayed))

    def play(self):
        """Method to update _timesplayed attribute
        """
        self._timesplayed = self._timesplayed + 1


class DLLNode:
    """Class to represent a doubly-linked list node

       Attributes:
       _element: Node element
       _next: Next node
       _prev: Previous node
    """
    def __init__(self, item, prevnode, nextnode):
        """Constructor for DLLNode class
        """
        self._element = item
        self._next = nextnode
        self._prev = prevnode

class MusicLibrary:
    """Class to represent the music library

       Attributes:
       _size: Size of music library
       _head: Head node of the library (does not hold an element)
       _tail: Tail node of the library (does not hold an element)
    """

    def __init__(self):
        self._size = 0
        self._head = DLLNode(None, None, None)
        self._tail = DLLNode(None, self._head, None)
        self._head._next = self._tail
        self._cursor = None
        self._timesplayed = 0

    def __str__(self):
        """String method to generate a representation of the music library
        """
        if self._size == 0:
            return ('Library is empty')
        else:
            string = "-"
            node = self._head._next
            while node._next != None:
                string = string + ("(Track Name: %s ; Artiste: %s ; Times Played: %i)\n" % (
                 node._element._name, node._element._artiste, node._element._timesplayed)) + "-"
                node = node._next
            string = string + (" Current Track: (%s)" % (self.get_current()))
            return string

    def remove_node(self, node):
        """Method to remove a node
        """
        node._prev._next = node._next
        node._next._prev = node._prev
        node._prev = None
        node._next = None
        self._size = self._size - 1

    def add_after(self, item, before):
        """Method to add a node after the specified node
        """
        n1 = DLLNode(item, None, None)
        before._next._prev = n1
        n1._next = before._next
        n1._prev = before
        before._next = n1
        self._size = self._size + 1

    def add_track(self, track):
        """Method that calls add_after() method to add track
        """
        if self._size == 0:
            self.add_after(track, self._head)
        else:
            self.add_after(track, self._tail._prev)

    def get_current(self):
        """Print the current track to screen
        """
        if self._cursor == None:
            print ("No current track")
        else:
            print ("Current Track: (%s ; %s; %i)" % (
               self._cursor._element._name, self._cursor._element._artiste, self._cursor._element._timesplayed))

    def next_track(self):
        """Method to get the next track
        """
        if self._cursor == None:
            self._cursor = self._head._next
            return (self._cursor._element)
        elif self._cursor._next == self._tail:
            print ('You are on the last track')
        else:
            self._cursor = self._cursor._next
            return (self._cursor._element)

    def prev_track(self):
        """Method to get the previous track
        """
        if self._cursor == None:
            print ('There is no previous track')
        elif self._cursor == self._head._next:
            print ('You are currently on the first track')
        else:
            self._cursor = self._cursor._prev
            return (self._cursor._element)
            
    def reset(self):
        """Method to reset library pointer to the first track
        """
        self._cursor = self._head._next
        return (self._cursor._element)

    def play(self):
        """Method to play the current track, printing it to screen
        """
        print ("Currently playing: (%s ; %s; %i)" % (
               self._cursor._element._name, self._cursor._element._artiste, self._cursor._element._timesplayed))
        self._cursor._element._timesplayed = self._cursor._element._timesplayed + 1
        Track.play(self)
        
    def remove_current(self):
        """Method to remove the current track
        """
        self.remove_node(self._cursor)        

    def length(self):
        """Method to get the library size
        """
        print ("Library size: %i" % (self._size))
          

def test():
    """Test block for the class
    """
    lib1 = MusicLibrary()
    lib1.length()
    track1 = Track("Say you wont let go","James Arthur")
    track2 = Track("The greatest", "Sia feat. Kendrick Lamar")
    track3 = Track("Closer", "Chainsmokers feat. Halsey")
    lib1.add_track(track1)
    lib1.add_track(track2)
    lib1.add_track(track3)
    print (lib1)
    lib1.next_track()
    lib1.play()
    lib1.next_track()
    lib1.get_current()
    lib1.prev_track()
    lib1.prev_track()
    lib1.play()
    lib1.remove_current()
    print (lib1)
    lib1.length()
    print(lib1)

