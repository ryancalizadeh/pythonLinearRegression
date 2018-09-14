"""
generate() returns a dataSet as follows:

    [[-50, y1,], [-49, y2], [-48, y3], [-47, y4] ... [47, y98], [48, y99], [49, y100], [50, y101]]

    Slope and y-intercept are randomly generated from 10 to -10

    Slope has a half chance of being divided by 10

    Each value is given a slight error from -3 to +3

model(x) returns slope * x + y-intercept
"""

import random
random.seed()

slope = random.randint(-10, 10) / ((float(random.randint(0, 1)) * 9) + 1)
y_intercept = random.randint(-10, 10)


def model(x):
    return slope * x + y_intercept

def generate():
    dataSet = []
    for i in range(-50, 51):
        dataSet.append([i, round(model(i) + random.uniform(-3, 3), 4)])
    return dataSet

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