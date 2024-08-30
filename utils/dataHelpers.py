from decimal import DivisionByZero
import numpy as np
import pandas as pd

def parseData(dataFile, openWithPandas=False):
    '''Reads data file and returns the parsed Data'''

    try:
        if openWithPandas:
            data = pd.read_csv(dataFile)
        else:
            data = np.loadtxt(dataFile, delimiter=',', dtype='str')
            data = data[1:].astype(np.float64)
    except FileNotFoundError:
        AssertionError(f"File: {dataFile} not found")
    except  PermissionError:
        AssertionError(f"File: {dataFile} does not have permissions")
    return data

def normalizeFeatures(*args): # normalization functions can be passed to this function to normalize the features
    '''Normalize features.'''

    features = []
    try:
        for feature in args:
            normalized = (feature - min(feature)) / (max(feature) - min(feature))
            features.append(normalized)
    except DivisionByZero:
        AssertionError("Division by zero encountered")

    return features

# Save learned thetas to a file
def readThetas(fileName):
    '''Writes theta0, theta1 to a file'''
    try:
        with open(fileName, 'r') as f:
            thetas = f.readline()
    except (FileNotFoundError, PermissionError):
        AssertionError("Can not open file.")
    return thetas.split(',')


