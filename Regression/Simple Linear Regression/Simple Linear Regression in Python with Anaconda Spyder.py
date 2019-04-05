
# Importing the required libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split

# Importing the depVector .csv data set
datasetDS = pd.read_csv('Dummy_Salary_Data.csv')
#print (depVectorDS)
indDMatrix = datasetDS.iloc[:, 0:1].values ## NOT  indDMatrix = datasetDS.iloc[:, 0].values
depVector = datasetDS.iloc[:, 1].values

#print (indDMatrix)
#print (depVector)


# Splitting the data sets into Training set and Test set

indDMatrix_train, indDMatrix_test = train_test_split(indDMatrix, test_size = .2, random_state = 0)

depVector_train, depVector_test = train_test_split(depVector, train_size = .8, random_state = 0)


# Fitting Simple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(indDMatrix_train, depVector_train)

# Predicting the Test set results
y_pred = regressor.predict(indDMatrix_test)

# Visualize the Training set results
plt.scatter(indDMatrix_train, depVector_train, color = 'blue')
plt.plot(indDMatrix_train, regressor.predict(indDMatrix_train), color='red')
plt.title('depVector vs Experience (Training set)')
plt.indDMatrixlabel('Years of Experience')
plt.ylabel('depVector')
plt.show()

# Visualize the Test set results
plt.scatter(indDMatrix_test, depVector_test, color = 'blue')
plt.plot(indDMatrix_train, regressor.predict(indDMatrix_train), color='red')
plt.title('depVector vs Experience (Test set)')
plt.indDMatrixlabel('Years of Experience')
plt.ylabel('depVector')
plt.show()
