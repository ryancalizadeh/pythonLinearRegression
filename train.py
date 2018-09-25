from generate import *
from modelClass import *
from gradDesc import *


dataSet = generate()
dataSet.generate()
model = model(0, 0)

gradDesc(model, dataSet.dataSet, 0.001)