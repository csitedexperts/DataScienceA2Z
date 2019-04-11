# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 17:09:03 2019

@author: mhossa12
"""

# Multiple Linear Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
datasetDS = pd.read_csv('Comp_Business.csv')
#X = dataset.iloc[:, :-1].values
#y = dataset.iloc[:, 4].values

X = datasetDS.iloc[:, 0:4].values ## NOT  X = datasetDS.iloc[:, 4].values
## Since X is a Matrix here
#Or X = dataset.iloc[:, :-1].values
#y = datasetDS.iloc[:, 4:5].values  ## NOT  y = datasetDS.iloc[:, 4].values
## Since y is a Transposed Matrix of the y itself
y = datasetDS.iloc[:, 4].values

# Encoding categorical data
#from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn import preprocessing as pp
#import LabelEncoder, OneHotEncoder
labelencoder = pp.LabelEncoder()
X[:, 3] = labelencoder.fit_transform(X[:, 3])
onehotencoder = pp.OneHotEncoder(categorical_features = [3])
X = onehotencoder.fit_transform(X).toarray()

# Avoiding the Dummy Variable Trap
X = X[:, 1:]

# Splitting the dataset into the Training set and Test set
from sklearn import cross_validation as cv

# Splitting the data sets into Training and Test sets
X_train, X_test = cv.train_test_split(X, test_size = .20, random_state = 0)
y_train, y_test = cv.train_test_split(y, train_size = .80, random_state = 0)
# Training  => 80% 

# Fitting the Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)
print (y_pred)
# Now Build the optimal model using Backward Elimination Model
import statsmodels.formula.api as sm
X = np.append(arr = np.ones((50, 1)).astype(int), values = X, axis = 1)
X_opt = X[:, [0, 1, 2, 3, 4, 5]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()

