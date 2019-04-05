
"""
#########   Homework_5.3(a)  ################
"""   


cur_b = 4 # The algorithm starts at b = 4
learning_rate = 0.01 # Learning rate
precision = 0.000001 #This tells us when to stop the algorithm
previous_step_size = 0.1 #
max_iCount = 10000 # maximum number of iterations
iCount = 0 #iteration counter

df = lambda b: 6*b - 5 #Gradient of our function 

while iCount < max_iCount and precision < previous_step_size:
    prev_b = cur_b #Store current g value in prev_g
    cur_b = cur_b - learning_rate * df(prev_b) #Gradient descent
    previous_step_size = abs(cur_b - prev_b) #Change in b
    iCount = iCount + 1 #iteration count
    print("At iteration: ",iCount," b value :", cur_b) #Print iterations
    
print("The minimizer is : ", cur_b)

min_value = 3*cur_b**2 - 5*cur_b + 4
print("The minimum value = ", min_value)






"""
#########   Homework_5.5(a)  ################

"""   

import numpy as np

X = [[180, 150], [150, 175], [170, 165]]
y = [[110], [140], [180]]

X_Transpose =np.transpose(X)
X_Transpose__X = np.matrix(X_Transpose)* np.matrix(X)
 
X_Transpose__X__Inv = np.linalg.inv(X_Transpose__X)
X_Transpose__X__Inv__X_Transpose = np.matrix(X_Transpose__X__Inv) * np.matrix(X_Transpose)

Beta = np.matrix(X_Transpose__X__Inv__X_Transpose) * np.matrix(y)
    
print("X:", X)
print("X_Transpose:", X_Transpose)
 
print("X_Transpose . X :", X_Transpose__X)

print("X_Transpose__X Inverse: ", X_Transpose__X__Inv)

print("X_Transpose__X__Inv . X_Transpose: ", X_Transpose__X__Inv__X_Transpose)

print("Beta", Beta)

x_feature = [[175, 170]]
y_predicted = np.matrix(x_feature) * np.matrix(Beta)

print("x_feature: ", x_feature)
print ("y_predicted: ", y_predicted)




"""
#########   Homework_5.5(b)  ################

"""   


import numpy as np
from numpy import linalg as LA

X = [[1, 2], [3, 4]]
Norm_X = LA.norm(X)
print("X:", X)
print("Norm_X:", Norm_X)


import numpy as np
from numpy import linalg as LA

X = [[180, 150], [150, 175], [170, 165]]
y = [[110], [140], [180]]

X_Transpose =np.transpose(X)
X_Transpose__y = np.matrix(X_Transpose)* np.matrix(y)
Norm_X = LA.norm(X)
Beta = X_Transpose__y / (Norm_X * Norm_X)
    
print("X:", X)
print("Norm_X:", Norm_X)

print("X_Transpose:", X_Transpose)

 
print("X_Transpose . y :", X_Transpose__y)

print("Beta", Beta)

x_feature = [[175, 170]]
y_predictedValue =  (np.matrix(x_feature) * np.matrix(Beta) ) 

print("x_feature: ", x_feature)
print ("y_predictedValue: ", y_predictedValue)



