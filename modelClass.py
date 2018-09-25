

def square(a):
    return a * a

class model:

    global theta0
    global theta1

    theta0 = 0
    theta1 = 0

    def __init__(self, theta0, theta1):
        self.theta0 = theta0
        self.theta1 = theta1

    def hypothesis(self, x):
        return self.theta0 + self.theta1 * x

    def cost(self, data):
        dif = []

        for i in range(0, 101):
            dif.append(square(self.hypothesis(data[i][0]) - data[i][1]))
        cots = 1/(len(data)*2) * sum(dif)

        return cots