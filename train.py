"""
Main program
"""

from generate import *
from modelClass import *
from gradDesc import *


dataSet = generate()
dataSet.generate()
model = model(0, 0)


epoch = gradDesc(model, dataSet.dataSet, float(input("Learning rate: ")))

print("\n ----- \n")

print("Epochs: ", epoch)
print("Your theta 0: ", model.theta0)
print("Correct theta 0: ", dataSet.y_intercept)
print("Your theta 1: ", model.theta1)
print("Correct theta 1: ", dataSet.slope, "\n")

print("Difference theta 0: ", abs(model.theta0 - dataSet.y_intercept))
print("Difference theta 1: ", abs(model.theta1 - dataSet.slope))
print("Final cost: ", model.cost(dataSet.dataSet))
print("\n")