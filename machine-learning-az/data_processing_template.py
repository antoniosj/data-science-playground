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

# tirar a media para preencher valor faltando
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
# fit colunas 1 e 2 do index
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])

# Encoding categorical data
# Colunas que tem um mesmo padrão (ex: 10 linhas com 3 tipos de países vão ser divididos
# em 0, 1 e 2 e depois vão ter 3 valores (0, 0, 1) para o ml não achar que um valor é
# maior que o outro apenas por causa da categoria dele

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
# X = colunas independentes e X[:, ] = todas as linhas da coluna 0
labelEncoder_X = LabelEnconder()
X[:, 0] = labelEncoder_X.fit_transform(X[:, 0])
#OneHotEncoder vai transformar minhas categorias em uma tabela de 0, 0, 1
oneHotEncoder = OneHotEncoder(categorial_features = [0])
# lembrar de formatar os valores em .0f 
X = oneHotEncoder.fit_transform(X).toarray()

# Y = coluna dependente
labelEncoder_Y = LabelEncoder()
# como essa coluna só são dois valores (0 e 1) não precisa do onehotencoder.
Y = labelEncoder_Y.fit_transform(Y)
# Splitting the dataset into training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)
