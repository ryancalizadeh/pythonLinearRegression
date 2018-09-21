from generate import *
from modelClass import *

dataSet = generate()
dataSet.generate()
model = model(0, 0)

model.theta0 = dataSet.y_intercept
model.theta1 = dataSet.slope

print(model.cost(dataSet.dataSet))