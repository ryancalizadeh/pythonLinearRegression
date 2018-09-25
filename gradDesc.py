from modelClass import *

def gradDesc(model, data, learningRate):
    
    check = True
    prevCost = model.cost(data)
    prevTheta = [model.theta0, model.theta1]

    while check:
        print("Slope: ", model.theta1)
        print("Y-intercept: ", model.theta0)
        print("Cost: ", model.cost(data))
        
        sumData0 = 0
        sumData1 = 0
        for i in data:
            sumData0 += (model.hypothesis(i[0]) - i[1])

        for i in data:
            sumData1 += (model.hypothesis(i[0]) - i[1]) * i[0]


        temp0 = model.theta0 - learningRate * sumData0 / len(data)
        temp1 = model.theta1 - learningRate * sumData1 / len(data) 

        model.theta0 = temp0
        model.theta1 = temp1

        newCost = model.cost(data)

        if newCost > prevCost:
            check = False
            print("The most recent update increased cost: ending now and reverting to previous values")
            model.theta0, model.theta1 = prevTheta[0], prevTheta[1]
        elif newCost == prevCost:
            check = False
            print("Arrived at local minimum: Ending now")
        elif newCost < prevCost:
            print("Succesful epoch: lowered cost by: ", prevCost - newCost)

        prevCost = newCost



