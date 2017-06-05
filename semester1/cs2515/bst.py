class BSTNode:
    """ An internal node in a (doubly linked) binary search tree. """
    
    def __init__(self, item):
        """ Initialise a BSTNode on creation, with value==item. """
        self._element = item
        self._leftchild = None
        self._rightchild = None
        self._parent = None

    def __str__(self):
        
        """ Return a string representation of the tree rooted at this node.

            The string will be created by an in-order traversal.
        """
        outstr = ''
        if self._leftchild:
            outstr = outstr + str(self._leftchild)
        outstr = outstr + ' ' + str(self._element)
        if self._rightchild:
            outstr = outstr + str(self._rightchild)
        return outstr
        

    def _statistics(self):
        """ Return a string of the basic statistics for the tree. """
        return ('size = ' + str(self.size())
               + '; height = ' + str(self.height()))    
  
    def search(self, item):
        """ Return the first subtree containing item, or None. """
        if item == self._element:
             return self
        elif item < self._element:
             if self._leftchild:
                self = self._leftchild
                return self.search(item)
             else:
                return None
        elif item > self._element:
            if self._rightchild:
                self = self._rightchild
                return self.search(item)
            else:
                return None
        

    def add(self, item):
        """ Add item to the tree, maintaining BST properties.
            Note: if item is already in the tree, this does nothing.
        """
        if item < self._element:
            if self._leftchild:
                self = self._leftchild
                self.add(item)
            else:
                item = BSTNode(item)
                self._leftchild = item
                item._parent = self
        elif item > self._element:
            if self._rightchild:
                self = self._rightchild
                self.add(item)
            else:
                item = BSTNode(item)
                self._rightchild = item
                item._parent = self
            
    def findmin(self):
        """ Return the minimal element below this node. """
        if self._leftchild != None:
            self = self._leftchild
            return self.findmin()
        else:
            return (self._element)
            

    def _findminnode(self):
        """ Return the BSTNode with the minimal element below this node. """
        if self._leftchild != None:
            self = self._leftchild
            return self._findminnode()
        else:
            return (self)

    def findmax(self):
        """ Return the maximal element below this node. """
        if self._rightchild != None:
            self = self._rightchild
            return self.findmax()
        else:
            return (self._element)

    def _findmaxnode(self):
        """ Return the BSTNode with the maximal element below this node. """
        if self._rightchild != None:
            self = self._rightchild
            return self.findmax()
        else:
            return (self)
    
    def height(self):
        """ Return the height of this node.

            Note that with the recursive definition of the tree the height
            of the node is the same as the depth of the tree rooted at this
            node.
        """
        if self == None:
            return 0
        elif self._leftchild == None and self._rightchild == None:
            return 0
        else:
            if self._leftchild == None:
                return 1 + (self._rightchild.height())
            elif self._rightchild == None:
                return 1 + (self._leftchild.height())
            else:
                return 1 + max(self._leftchild.height(), self._rightchild.height())

    def size(self):
        """ Return the size of this subtree.

            The size is the number of nodes (or elements) in the tree.
        """
        count = 1
        if self:
            if self._leftchild:
                count += 1 + self._leftchild.size()
            if self._rightchild:
                count += 1 + self._rightchild.size()
        return count

    def leaf(self):
        """ Return True if this node has no children. """
        if not self._leftchild and not self._rightchild:
            return True
        else:
            return False

    def semileaf(self):
        """ Return True if this node has exactly one child. """
        if self._leftchild and not self._rightchild:
            return True
        if self._rightchild and not self._leftchild:
            return True
        else:
            return False

    def full(self):
        """ Return true if this node has two children. """
        if self._leftchild and self._rightchild:
            return True
        else:
            return False

    def internal(self):
        """ Return True if this node has at least one child. """
        if self._leftchild or self._rightchild:
            return True
        else:
            return False

    def remove(self, item):
        """ Remove and return item from the tree rooted at this node.

            Maintains the BST properties.
        """
        node = self.search(item)
        print (node)
        node._remove_node()
        

    def _remove_node(self):
        """ (Private) Remove this BSTBode from its tree.

            Maintains the BST properties.
        """
        #if this is a full node
            #find the biggest item in the left tree
            #  - there must be a left tree, since this is a full node
            #  - the node for that item can have no right children
            #move that item up into this item
            #remove that old node, which is now a semileaf
            #return the original element
        #else if this has no children
            #find who the parent was
            #set the parent's appropriate child to None
            #wipe this node
            #return this node's element
        #else if this has no right child (but must have a left child)
            #shift leftchild up into its place, and clean up
            #return the original element
        #else this has no left child (but must have a right child)
            #shift rightchild up into its place, and clean up
            #return the original element
        if self._leftchild and self._rightchild:
            print ("full")
            top = self
            left = self._leftchild
            node = left._findmaxnode()
            if top._leftchild != node:
                node._leftchild = top._leftchild
            if top._rightchild != node:
                node._rightchild = top._rightchild
            node._parent = top._parent
            top._rightchild._parent = node
            if top._parent._rightchild == top:
                top._parent._rightchild = node
            if top._parent._leftchild == top:
                top._parent._leftchild = node
            top._leftchild = None
            top._rightchild = None
            top._parent = None
            return top._element
        if self._leftchild == None and self._rightchild == None:
            print ("leaf")
            parental = self._parent
            parental._leftchild = None
            parental._rightchild = None
            self._parent = None
            return self._element
        if self._leftchild and not self._rightchild:
            print ("left")
            left = self._leftchild
            if self._parent != None:
                left._parent = self._parent
                if left._parent._rightchild != None:
                    if self._parent._rightchild == self:
                       self._parent._rightchild = left
                       self._parent = None
                if left._parent._leftchild != None:
                    if self._parent._leftchild  == self:
                       self._parent._lefthcild = left
                       self._parent = None
            self._leftchild = None
            return self._element
        if self._rightchild and not self._leftchild:
            print ("right")
            right = self._rightchild
            if self._parent != None:
                right._parent = self._parent
                if right._parent._rightchild != None:
                    if self._parent._rightchild == self:
                       self._parent._rightchild = right
                       self._parent = None
                if right._parent._leftchild != None:
                   if right._parent._leftchild  == self:
                      self._parent._lefthcild = right
                      self._parent = None
            self._rightchild = None
            return self._element
            #For the case of removing 1 the directly above section of my code
            #does not work. I understand that it is removing the rightchild (6)
            #instead of the parent (1) because it is a root node but I do
            #not know how to fix it. Any attempts to do so has caused the entirety
            #of my remove function to error, so I've decided to leave it as is
            #until I can find a solution.


    def _pullup(self, node):
        """ Pull up the child tree rooteed at node into this BSTNode. """
        #method body goes here.
        pass
        #I found that I did not need this function

    def _print_structure(self):
        """ (Private) Print a structured representation of tree at this node. """
        outstr = str(self._element) + '(' + str(self.height()) + ')['
        if self._leftchild:
            outstr = outstr + str(self._leftchild._element) + ' '
        else:
            outstr = outstr + '* '
        if self._rightchild:
            outstr = outstr + str(self._rightchild._element) + ']'
        else:
            outstr = outstr + '*]'
        if self._parent:
            outstr = outstr + ' -- ' + str(self._parent._element)
        else:
            outstr = outstr + ' -- *'
        print(outstr)
        if self._leftchild:
            self._leftchild._print_structure()
        if self._rightchild:
            self._rightchild._print_structure()

    def _isthisapropertree(self):
        """ Return True if this node is a properly implemented tree. """
        ok = True
        if self._leftchild:
            if self._leftchild._parent != self:
                ok = False
            if self._leftchild._isthisapropertree() == False:
                ok = False
        if self._rightchild:
            if self._rightchild._parent != self:
                ok = False
            if self._rightchild._isthisapropertree() == False:
                ok = False          
        if self._parent:
            if (self._parent._leftchild != self
                and self._parent._rightchild != self):
                ok = False
        return ok
    
    def _testadd():
        node = BSTNode('mushroom')
        node._print_structure()
        print('adding green bean')
        node.add('green bean')
        node._print_structure()
        print('adding radish')
        node.add('radish')
        node._print_structure()
        print('adding pea')
        node.add('pea')
        node._print_structure()
        print('adding pepper')
        node.add('pepper')
        node._print_structure()
        print('adding parsnip')
        node.add('parnip')
        node._print_structure()
        print ('searching for pepper') #test for search
        x = node.search('pepper') 
        print (x)
        print ('finding min') #test for min
        print (node.findmin())
        print ('finding max') #test for max
        print (node.findmax())
        print ('finding size') #test for size
        print (node.size())
        print ('finding height') #test for height
        print (node.height())
        return node
            
    def _test():
        node = BSTNode(1)
        print('Ordered:', node)
        node._print_structure()
        print('adding', 0)
        node.add(0)
        print('Ordered:', node)
        node._print_structure()
        print('removing', 0)
        node.remove(0)
        print('Ordered:', node)
        node._print_structure()
        print('adding', 2)
        node.add(2)
        print('Ordered:', node)
        node._print_structure()
        print('removing', 2)
        node.remove(2)
        print('Ordered:', node)
        node._print_structure()
        print('adding', 6)
        node.add(6)
        print('Ordered:', node)
        node._print_structure()
        print('removing', 1)
        node.remove(1)
        print('Ordered:', node)
        node._print_structure()
        print('adding', 2)
        node.add(2)
        print('Ordered:', node)
        node._print_structure()
        print('adding', 4)
        node.add(4)
        print('Ordered:', node)
        node._print_structure()
        print('adding', 3)
        node.add(3)
        print('Ordered:', node)
        node._print_structure()
        print('adding', 5)
        node.add(5)
        print('Ordered:', node)
        node._print_structure()
        print('removing', 2)
        node.remove(2)
        print('Ordered:', node)
        node._print_structure()
        print('removing', 4)
        node.remove(4)
        print('Ordered:', node)
        node._print_structure()
        print('removing', 3)
        node.remove(3)
        print('Ordered:', node)
        node._print_structure()
        print('removing', 5)
        node.remove(5)
        print('Ordered:', node)
        node._print_structure()
        print('adding', 12)
        node.add(12)
        print('Ordered:', node)
        node._print_structure()
        print('adding', 8)
        node.add(8)
        print('Ordered:', node)
        node._print_structure()
        print('adding', 9)
        node.add(9)
        print('Ordered:', node)
        node._print_structure()
        print('adding', 7)
        node.add(7)
        print('Ordered:', node)
        node._print_structure()
        print('removing', 12)
        node.remove(12)
        print('Ordered:', node)
        node._print_structure()
        print('removing', 8)
        node.remove(8)
        print('Ordered:', node)
        node._print_structure()
        print('removing', 9)
        node.remove(9)
        print('Ordered:', node)
        node._print_structure()
        print('removing', 7)
        node.remove(7)
        print('Ordered:', node)
        node._print_structure()



############-TEST-BLOCK-############

#BSTNode._test()

#BSTNode._testadd()
