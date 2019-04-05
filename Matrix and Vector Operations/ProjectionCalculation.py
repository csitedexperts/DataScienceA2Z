


"""
#########   Homework_4.3  ################

"""   

import numpy as np

U = [[1, 1], [1, 2], [1, 3], [1, 4]]
x = [[-1], [0], [2], [5]]

U_Transpose =np.transpose(U)
U_Transpose__U = np.matrix(U_Transpose)* np.matrix(U)
 
U_Transpose__U__Inv = np.linalg.inv(U_Transpose__U)
U_Transpose__U__Inv__U_Transpose = np.matrix(U_Transpose__U__Inv) * np.matrix(U_Transpose)

Projection = np.matrix(U) * (np.matrix(U_Transpose__U__Inv__U_Transpose)*np.matrix(x))
    
print("U:", U)
print("U_Transpose:", U_Transpose)
 
print("U_Transpose . U :", U_Transpose__U)

print("U_Transpose__U Inverse: ", U_Transpose__U__Inv)

print("U_Transpose__U__Inv . U_Transpose: ", U_Transpose__U__Inv__U_Transpose)

print("Projection", Projection)

