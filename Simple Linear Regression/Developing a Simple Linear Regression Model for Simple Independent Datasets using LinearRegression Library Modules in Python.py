
# Importing the required libraries
import pandas as pd
import matplotlib.pyplot as plt
import sklearn.cross_validation as cv


# Importing the dataset from the data file
datasetDS = pd.read_csv('ExpSalary_Data.csv')
#print (datasetDS)
X = datasetDS.iloc[:, 0:1].values ## NOT  X = datasetDS.iloc[:, 0].values
## Since X is a Matrix here
y = datasetDS.iloc[:, 1:2].values ## Can be  y = datasetDS.iloc[:, 1].values
## y is a Vector here
#print (X)
#print (y)

# Visualize the Original dataset
plt.scatter(X, y, color = 'blue')
plt.plot(X, y, color='red')
plt.title("Original Set's Experience vs Salary Regression Line")
plt.xlabel("Years of Experience")
plt.ylabel("Yearly Salary ($)")
plt.grid()
plt.show()

# Splitting the data sets into Training and Test sets

X_train, X_test = cv.train_test_split(X, test_size = .20, random_state = 0)

y_train, y_test = cv.train_test_split(y, train_size = .80, random_state = 0)
# Training  => 80% 

# Fitting Simple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

#print (regressor)  ## Can't be printed as something visible

# Predicting the Test set results
y_pred = regressor.predict(X_test)
#print (X_train)
#print (y_train)
print (y_pred)

# Visualize the Training set results
plt.scatter(X_train, y_train, color = 'blue')
plt.plot(X_train, regressor.predict(X_train), color='red')
plt.title("Training Set's Experience vs Salary Regression Line")
plt.xlabel("Years of Experience")
plt.ylabel("Yearly Salary ($)")
plt.grid()
plt.show()


# Visualize the Test set results
plt.scatter(X_test, y_test, color = 'blue')
plt.plot(X_train, regressor.predict(X_train), color='red')
plt.title("Test Set's Experience vs Salary Regression Line")
plt.xlabel("Years of Experience")
plt.ylabel("Yearly Salary ($)")
plt.grid()
plt.show()

