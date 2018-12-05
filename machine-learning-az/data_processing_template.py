# data preprocessing

# importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# importing dataset
dataset = pd.read_csv('Data.csv')
# creates matrix of independents variables until last column minus 1
X = dataset.iloc[:, :-1].values

# creates matrix of dependent variable. The last column.
lastColumn = 3
Y = dataset.iloc[:, lastColumn].values