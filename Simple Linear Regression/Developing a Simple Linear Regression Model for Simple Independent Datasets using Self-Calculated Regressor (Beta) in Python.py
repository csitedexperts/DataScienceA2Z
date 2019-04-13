
# Importing the required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Importing the dataset from the data file
datasetDS = pd.read_csv('ExpSalary_Data.csv')
#print (datasetDS)
X = datasetDS.iloc[:, 0:1].values ## NOT  X = datasetDS.iloc[:, 0].values
## Since X is a Matrix here
y = datasetDS.iloc[:, 1:2].values  ## NOT  y = datasetDS.iloc[:, 1].values
## Since y is a Transposed Matrix of the y itself

#print (X)
#print (y)

# Visualize the Original dataset

### Can we do this ??

### Yes, this is a 2D matrix 


plt.scatter(X, y, color = 'blue')
plt.plot(X, y, color='red')
plt.title("Original Set's Experience vs Salary Regression Line")
plt.xlabel("Years of Experience")
plt.ylabel("Yearly Salary ($)")
plt.grid()
plt.show()

X_Transpose =np.transpose(X)
X_Transpose__X = np.matrix(X_Transpose) * np.matrix(X)
 
X_Transpose__X__Inv = np.linalg.inv(X_Transpose__X)
X_Transpose__X__Inv__X_Transpose = np.matrix(X_Transpose__X__Inv) * np.matrix(X_Transpose)

reg = np.matrix(X_Transpose__X__Inv__X_Transpose) * np.matrix(y)
    
print("X:", X)
print("X_Transpose:", X_Transpose)
print("X_Transpose . X :", X_Transpose__X)
print("X_Transpose__X Inverse: ", X_Transpose__X__Inv)
print("X_Transpose__X__Inv . X_Transpose: ", X_Transpose__X__Inv__X_Transpose)
print("Regressor: ", reg)

x_feature = [[4]]
y_predicted = np.matrix(x_feature) * np.matrix(reg)

print("x_feature: ", x_feature)
print ("y_predicted: ", y_predicted)


x_feature = [[6]]
y_predicted = np.matrix(x_feature) * np.matrix(reg)

print("x_feature: ", x_feature)
print ("y_predicted: ", y_predicted)


x_feature = [[8]]
y_predicted = np.matrix(x_feature) * np.matrix(reg)

print("x_feature: ", x_feature)
print ("y_predicted: ", y_predicted)


### Verify/Compare it with the previous model 
### Try it yourself




