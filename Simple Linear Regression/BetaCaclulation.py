
"""

"""   

import numpy as np

X = [[180, 150], [150, 175], [170, 165]]
y = [[110], [140], [180]]

X_Transpose =np.transpose(X)
X_Transpose__X = np.matrix(X_Transpose)* np.matrix(X)
 
X_Transpose__X__Inv = np.linalg.inv(X_Transpose__X)
X_Transpose__X__Inv__X_Transpose = np.matrix(X_Transpose__X__Inv) * np.matrix(X_Transpose)

Beta1 = np.matrix(X_Transpose__X__Inv__X_Transpose) * np.matrix(y)
    
print("X:", X)
print("X_Transpose:", X_Transpose)
 
print("X_Transpose . X :", X_Transpose__X)

print("X_Transpose__X Inverse: ", X_Transpose__X__Inv)

print("X_Transpose__X__Inv . X_Transpose: ", X_Transpose__X__Inv__X_Transpose)

print("Beta1", Beta1)

x_feature = [[175, 170]]
y_predicted = np.matrix(x_feature) * np.matrix(Beta1)

print("x_feature: ", x_feature)
print ("y_predicted: ", y_predicted)



