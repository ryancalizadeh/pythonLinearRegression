"""
self.dataSet is a random dataSet as follows:

    [[-50, y1,], [-49, y2], [-48, y3], [-47, y4] ... [47, y98], [48, y99], [49, y100], [50, y101]]

Self.Slope and Self.y-intercept are randomly generated from 10 to -10

    Slope has a half chance of being divided by 10

    Each value is given a slight error from -3 to +3

self.absoluteModel(x) returns self.slope * x + self.y-intercept
"""

import random
random.seed()

class generate:

    global slope
    global y_intercept
    global dataSet

    slope = random.randint(-10, 10) / ((float(random.randint(0, 1)) * 9) + 1)
    y_intercept = random.randint(-10, 10)
    dataSet = []
    
    def __init__(self):
        self.slope = slope
        self.y_intercept = y_intercept
        self.dataSet = dataSet
    

    def absoluteModel(self, x):
        return self.slope * x + self.y_intercept
    
    def generate(self):
        for i in range(-50, 51):
            self.dataSet.append([i, round(self.absoluteModel(i) + random.uniform(-3, 3), 4)])

        
        #print("y = ", self.slope, "x + ", self.y_intercept)

"""

dataSet = generate()

print("Slope: ", slope)
print("y-intercept: ", y_intercept)
print("\n\n x  |  y")
for i in range(-9, 0):
    print(i, " | ", model(i))

for i in range(0, 10):
    print("", i, " | ", model(i))

for i in dataSet:
    print(i)

"""