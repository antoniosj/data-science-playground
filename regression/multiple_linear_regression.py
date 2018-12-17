import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# importing dataset
dataset = pd.read_csv('50_Startups.csv')
# creates matrix of independents variables until last column minus 1
X = dataset.iloc[:, :-1].values

# creates matrix of dependent variable. The last column.
# lastColumn = 1
y = dataset.iloc[:, 4].values

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
# Encoding categorical values (cities)
labelEncoder_X = LabelEncoder()
X[:, 3] = labelEncoder_X.fit_transform(X[:, 3])
#OneHotEncoder vai transformar minhas categorias em uma tabela de 0, 0, 1
oneHotEncoder = OneHotEncoder(categorical_features = [3])

X = oneHotEncoder.fit_transform(X).toarray()

# Avoiding the dummy variable trap

X = X[:, 1:]


# Splitting the dataset into training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)


# Fitting mlr to the training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train) 


# Predicting the test set results
y_pred = regressor.predict(X_test)

# select a significance lvl = eg 0,05 - step 1

# Building the optimal model using BACKWARD ELIMINATION
import statsmodels.formula.api as sm

# fit the full model with all possible predictors
X = np.append(arr = np.ones((50, 1)).astype(int), values = X, axis = 1)
X_opt = X[:, [0, 1, 2, 3, 4, 5]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit() # OLS = Ordinary least square
# see the summary and consider the predictor with the highest p-value. if p > sign lvl remove.
regressor_OLS.summary()

# removing this 0.99 predictor and fit model without this variable
X_opt = X[:, [0, 3]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()


