"""Import tkinter from python library
"""
from tkinter import *

class Calculate(object):
    """Class to represent calculations of a calculator
    
       Attributes:
       _isFirstOperand: Boolean to check if user input is the first operand
       _firstOperand: Integer representation of first operand
       _secondOperand: Integer representation of second operand
       _operator: Operator
    """
   
    def __init__(self):
        """Constructor for calculate
        """
        self._isFirstOperand = True
        self._firstOperand = -1
        self._secondOperand = -1
        self._operator = None

    def isFirstOperand(self):
        """ Method to check if user input is first operand
        """
        if self._isFirstOperand:
            return True
        else:
            return False

    def setOperand(self, value):
        """Setter for the _firstOperand and _secondOperand attributes provided 
           from the user input
        
           Sets the attribute(s)
        """
        if self._isFirstOperand == True:
            self._firstOperand = value
            self._isFirstOperand = False
        else:
            self._secondOperand = value
            self._isFirstOperand = True
        return value

    def setOperator(self, value):
        """Setter for the _operator attribute provided from the user input
        
           Sets the attribute
        """
        if self._isFirstOperand == False:
            self._operator = value
            return value
        elif value == "=":
            return doCalculation()
        

    def doCalculation(self):
        """Method to carry out the calculator calculation
        """
        if self._operator == "+":
            return (self._firstOperand + self._secondOperand)
        elif self._operator == "-":
            return (self._firstOperand - self._secondOperand)
        elif self._operator == "*":
            return (self._firstOperand * self._secondOperand)
        elif self._operator == "/":
            return (self._firstOperand / self._secondOperand)

def setOperand(num, calculate):
    """Setter for the _firstOperand and _secondOperand attributes provided
       from an instance of the calculate class
        
       Sets the attribute(s)
    """
    if calculate._isFirstOperand == True:
        calculate._firstOperand = num
        calculate._isFirstOperand = False
    else:
        calculate._secondOperand = num
        calculate._isFirstOperand = True
    lab1['text'] = str(num)

def setOperator(operator, calculate):
    """Setter for the _operator attribute provided from an instance of the
       calculate class
    """
    calculate._operator = operator
    lab1['text'] = operator

def equalsPressed(calculate):
    """Method to print answer of calculation to the calculator screen
    """
    lab1['text'] = (calculate.doCalculation())

"""Create instance of the class
"""
calculate = Calculate()

"""Create top level container and configure calculator interface
"""
root = Tk()
root.configure(bg='lightgray')
root.minsize(width=200, height=180)
root.maxsize(width=200, height=180)

lab1 = Label(root, text = "", bg = "red", height = 2)
lab1.pack(fill=X)
frame1 = Frame(root)

"""Configure buttons of the calculator gui
"""
frame1.pack()
but1 = Button(frame1, text = "1", width = 5, bg = "lightblue", command=(lambda: setOperand(1, calculate)))
but2 = Button(frame1, text = "2", width = 5, bg = "lightblue", command=(lambda: setOperand(2, calculate)))
but3 = Button(frame1, text = "3", width = 5, bg = "lightblue", command=(lambda: setOperand(3, calculate)))
but4 = Button(frame1, text = "4", width = 5, bg = "lightblue", command=(lambda: setOperand(4, calculate)))
but5 = Button(frame1, text = "5", width = 5, bg = "lightblue", command=(lambda: setOperand(5, calculate)))
but6 = Button(frame1, text = "6", width = 5, bg = "lightblue", command=(lambda: setOperand(6, calculate)))
but7 = Button(frame1, text = "7", width = 5, bg = "lightblue", command=(lambda: setOperand(7, calculate)))
but8 = Button(frame1, text = "8", width = 5, bg = "lightblue", command=(lambda: setOperand(8, calculate)))
but9 = Button(frame1, text = "9", width = 5, bg = "lightblue", command=(lambda: setOperand(9, calculate)))
but0 = Button(frame1, text = "0", width = 5, bg = "lightblue", command=(lambda: setOperand(0, calculate)))
butp = Button(frame1, text = "+", width = 5, bg = "violet", command=(lambda: setOperator('+', calculate)))
butm = Button(frame1, text = "-", width = 5, bg = "violet", command=(lambda: setOperator('-', calculate)))
buts = Button(frame1, text = "*", width = 5, bg = "violet", command=(lambda: setOperator('*', calculate)))
butd = Button(frame1, text = "/", width = 5, bg = "violet", command=(lambda: setOperator('/', calculate)))
bute = Button(frame1, text = "=", width = 5, bg = "turquoise", command=(lambda: equalsPressed(calculate)))

but1.grid(row = 1, column = 1)
but2.grid(row = 1, column = 2)
but3.grid(row = 1, column = 3)
but4.grid(row = 2, column = 1)
but5.grid(row = 2, column = 2)
but6.grid(row = 2, column = 3)
but7.grid(row = 3, column = 1)
but8.grid(row = 3, column = 2)
but9.grid(row = 3, column = 3)
but0.grid(row = 4, column = 1)
butp.grid(row = 4, column = 2)
butm.grid(row = 4, column = 3)
buts.grid(row = 5, column = 1)
butd.grid(row = 5, column = 2)
bute.grid(row = 5, column = 3)
