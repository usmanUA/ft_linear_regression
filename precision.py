from utils.dataHelpers import readThetas, parseData
from pandas.errors import EmptyDataError


def calculateR2(y, predY, n):
    '''Calculates R2 Score of the actual and predicted vallues'''
    mean_y = sum(y) / n
    rss = sum((y - predY) ** 2)
    tss = sum((y - mean_y) ** 2)
    if tss == 0:
        assert sum(y) == mean_y * n, "Error calculating R2 Score"
        return 1
    return 1 - (rss/tss)


def main():
    '''Calculates and prints the Top Evaluation Metrics for Linear Regression'''

    try:
        thetas = readThetas('thetas.txt')
        data = parseData('data.csv')
        X, y = data[:, 0], data[:, 1]
    except EmptyDataError:
        AssertionError('Could not parse data files')
    try:
        thetas = [float(thetas[0]), float(thetas[1])]
    except FloatingPointError:
        AssertionError("Can not convert str to float")
    n = y.size
    predY = thetas[0] + (thetas[1] * X)
    deltaErr = y - predY
    mse = sum(abs(deltaErr)) / n
    rmse = (sum(deltaErr ** 2) / n) ** 0.5
    r2Score = calculateR2(y, predY, n)
    print("\033[37mEvualtion metrics included: Mean Absolute Error, Root Mean Squared Error and R2 Score.\033[0m")
    print(f"\033[31mMSE: {mse}, RMSE: {rmse}, R2-Score: {r2Score}\033[31m")



if __name__ == '__main__':
    main()
