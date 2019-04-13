
# Importing the required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Importing the dataset from the data file
datasetDS = pd.read_csv('CompSalary_Data.csv')

X = datasetDS.iloc[:, 0:7].values ## NOT  X = datasetDS.iloc[:, 7].values
## Since X is a Matrix here
y = datasetDS.iloc[:, 7:8].values  ## NOT  y = datasetDS.iloc[:, 7].values
## Since y is a Transposed Matrix of the y itself

print (X)
print (y)


X_Transpose =np.transpose(X)
X_Transpose__X = np.matrix(X_Transpose)* np.matrix(X)
 
X_Transpose__X__Inv = np.linalg.inv(X_Transpose__X)
X_Transpose__X__Inv__X_Transpose = np.matrix(X_Transpose__X__Inv) * np.matrix(X_Transpose)

reg = np.matrix(X_Transpose__X__Inv__X_Transpose) * np.matrix(y)
    
print("X:", X)
print("X_Transpose:", X_Transpose)
print("X_Transpose . X :", X_Transpose__X)
print("X_Transpose__X Inverse: ", X_Transpose__X__Inv)
print("X_Transpose__X__Inv . X_Transpose: ", X_Transpose__X__Inv__X_Transpose)
print("Regressor: ", reg)

x_feature = [[4, 14, 3, 5, 1, 1, 4]]
y_predicted = np.matrix(x_feature) * np.matrix(reg)

print("x_feature: ", x_feature)
print ("y_predicted: ", y_predicted)

x_feature = [[6, 16, 2, 5, 2, 0, 4]]
y_predicted = np.matrix(x_feature) * np.matrix(reg)

print("x_feature: ", x_feature)
print ("y_predicted: ", y_predicted)


x_feature = [[8, 12, 5, 10, 2, 1, 4]]
y_predicted = np.matrix(x_feature) * np.matrix(reg)

print("x_feature: ", x_feature)
print ("y_predicted: ", y_predicted)



## Homework: Using the Dummy_Titanic_Data.csv practice this 
## The datasets are pretty similar, so you should be able to do it yourself.
## Remember, ONLY practice you will make you perfect.



### Verify/Compare it with the previous model 
### Try it yourself




### Could we do this ??

"""
# Visualize the Original dataset
import matplotlib.pyplot as plt

plt.scatter(X, y, color = 'blue')
plt.plot(X, y, color='red')
plt.title("Original Set's Experience vs Salary Regression Line")
plt.xlabel("Years of Experience")
plt.ylabel("Yearly Salary ($)")
plt.grid()
plt.show()










### No, this is not a 2D matrix 

"""