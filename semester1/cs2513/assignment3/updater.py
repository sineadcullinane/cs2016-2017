"""Import shelve functionality
"""
import shelve
from pet import Pet
import writer

"""Open the shelve, acccess the shelve using the known keys, print the objects
"""
db = shelve.open("pets")
scamp = db["Scamp"]
rosie = db["Rosie"]
print (scamp)
print (rosie)

"""Update the objects then print again
"""
scamp.setAge(scamp._age + 1)
rosie.setAge(rosie._age + 1)
print (scamp)
print (rosie)

"""Rewrite objects to the shelve
"""
db[scamp._name] = scamp
db[rosie._name] = rosie

"""Close the shelve
"""
db.close
