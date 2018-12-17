import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# importing dataset
dataset = pd.read_csv('Salary_Data.csv')
# creates matrix of independents variables until last column minus 1
X = dataset.iloc[:, :-1].values

# creates matrix of dependent variable. The last column.
# lastColumn = 1
Y = dataset.iloc[:, 1].values

# Splitting the dataset into training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 1/3, random_state = 0)

"""
# Feature scalling
# Standard or Normalization
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
"""

# Fitting simple linear regression to the training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, Y_train)

# Predicting the Test set results
# cria 1 tabela com o salario previsto pra cada funcionario.
# y_test = real salary y_pred = the predicted salary
# just for visualization and nothing else.
Y_pred = regressor.predict(X_test)

# Visualising the training set results
plt.scatter(X_train, Y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary x Experience (training set)')
plt.xlabel('Years of experience')
plt.ylabel('Salary')
plt.show()

plt.scatter(X_test, Y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary x Experience (training set)')
plt.xlabel('Years of experience')
plt.ylabel('Salary')
plt.show()