"""Import random and tkinter from python library
"""
import random

from tkinter import *

#root = Tk()

class SquareGame(object):
    """Class to represent the square game
    """

    def __init__(self, root):
        """Constructor for square game
        """
        self.canvas = Canvas(root, width=500, height=500)
        self.canvas.pack()
        root.bind("<Button-1>", self.play)
        square = self.canvas.create_rectangle(20, 20, 40, 40, fill='red', outline='red')


    def play(self, event):
        """Method to draw and clear squares, and check if user has successfully clicked the square
        """
        self.canvas.delete('all')
        randomx = random.randint(0, 475)
        randomy = random.randint(0, 475)
        item = self.canvas.create_rectangle(randomx, randomy, randomx + 30, randomy + 30,  fill='blue', outline='blue')
        if event.x < randomx and event.x > randomx + 30:
            print ("Well done")
        elif event.y < randomy and event.y > randomy + 30:
            print ("Well done")
        else:
            print ("Miss")


    def insquare(event):
        pass

"""Create instance of square game
"""
root = Tk()
game = SquareGame(root)
