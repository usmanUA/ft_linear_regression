from pandas.errors import EmptyDataError
from utils.dataHelpers import *
import matplotlib.pyplot as plt
import seaborn as sns

# Save learned thetas to a file
def saveThetas(thetas):
    '''Writes theta0, theta1 to a file'''
    try:
        with open('thetas.txt', 'w') as f:
            f.write(f"{thetas[0]}, {thetas[1]}")
    except (FileNotFoundError, PermissionError):
        AssertionError("Can not open file.")


# Cost Function 
def costFunction(theta0, theta1, X, Y, m):
    ''' Calculates and returns the cost '''
    predY = theta0 + (theta1 * X)
    deltaErr = predY - Y
    return deltaErr, ((sum(deltaErr) * -1) ** 2) / (2 * m)

def optimizeThetas(X, Y, iterations, learningRate=0.3): # make this function generic for next projects too
    '''Returns optimized thetas using gradient descent'''

    params = np.zeros(2)
    cost = np.zeros(iterations)
    m = Y.size
    for iter in range(0, iterations):
        deltaErr, cost[iter] = costFunction(params[0], params[1], X, Y, m)
        params[0] -= learningRate * (sum(deltaErr) / m)
        params[1] -= learningRate * ((sum(deltaErr * X) / m))
    return params, cost

# normalize the paramets based on the original mileage values
def normalizeThetas(thetas, X):
    ''' Normalize thetas based on the min/max of the dataset '''
    xMin = min(X)
    xMax = max(X)
    yMin = thetas[0]
    yMax = thetas[0] + thetas[1]
    theta1 = (yMax - yMin) / (xMax - xMin)
    theta0 = (yMin - (theta1 * xMin))
    return theta0, theta1

def plotLinearFit(X, y, thetas, plot):
    '''Plots the data and the linear fit line to see how it fits'''
    predY = thetas[0] + (thetas[1] * X)
    plot.scatter(x=X, y=y, label='Actual Price')
    plot.set_title('Mileage vs Price')
    plot.set_xlabel('Mileage (KM)')
    plot.set_ylabel('Price (EUR)')
    plot.plot(X, predY, label='Predicted Price', color='magenta')
    plot.legend()

def plotCost(cost, iterations, plot):
    '''Plots the cost against the total number of iterations'''
    cycles = list(range(1, iterations+1))
    plot.scatter(cycles, cost)
    plot.set_title("Cost vs No. of iterations")
    plot.set_xlabel("No. of iterations")
    plot.set_ylabel("Cost")
    plot.plot(cycles, cost)

def plotData(X, y, thetas, cost, iterations):
    '''Plots the given data as a scatterplot'''
    fig, plots = plt.subplots(1, 2, figsize=(13, 5))
    fig.subplots_adjust(wspace=0.4)
    plotLinearFit(X, y, thetas, plots[0])
    plotCost(cost, iterations, plots[1])
    plt.show()


def main():
    '''Trains the model and predicts the prices given the car mileage through user input'''

    try:
        data = parseData('data.csv')
        X, y = data[:, 0], data[:, 1]
        normX = normalizeFeatures(X)[0]
    except EmptyDataError as e:
        print(e)
    thetas, cost = optimizeThetas(normX, y, 2000)
    thetas[0], thetas[1] = normalizeThetas(thetas, X)
    saveThetas(thetas)
    plotData(X, y, thetas, cost, 2000)





if __name__ == '__main__':
    main()
