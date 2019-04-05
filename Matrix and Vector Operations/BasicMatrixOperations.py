# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 19:41:38 2019

@author: mhossa12
"""

import numpy as np

# You need to install numpy in order to import it 
# Numpy transpose returns similar result when 
# applied on 1D matrix 

matrix_M = [[4,1,5],[3,6,2]] 
print(matrix_M) 

print("\n") 
print(np.transpose(matrix_M)) 


matrix_a = [[8,4,2],[6,1,5]]
matrix_b = [[3,10,4],[5,6,1]]

matrix_c = np.matrix(matrix_a) + np.matrix(matrix_b)

print(matrix_c) 



matrix_a = [[8,4,2],[6,1,5]]
matrix_b = [[3,10,4],[5,6,1]]

matrix_d = np.matrix(matrix_a) - np.matrix(matrix_b)

print(matrix_d) 


matrix_a = [[8,4,2],[6,1,5]]

matrix_e = 2 * np.matrix(matrix_a)
print(matrix_e) 




matrix_a = [[8,4,2],[6,1,5]]  
matrix_b = [[3,10],[5,6], [1, 2]]

matrix_f = np.matrix(matrix_a) * np.matrix(matrix_b)

print(matrix_f) 


matrix_m = [[5,1,6],[0, 8, -2]]  
matrix_n = [[2],[3],[4]]

matrix_g = np.matrix(matrix_m) * np.matrix(matrix_n)

print(matrix_g) 

matrix_1 = [[4, 7], [2, 6]]
matrix1_inv = np.linalg.inv(matrix_1)
print(matrix1_inv) 

matrixE = [[1, 0, 0], [-5, 1, 0], [0, 0, 1]]
matrixE_inv = np.linalg.inv(matrixE)
print(matrixE_inv) 









matrixM = [[1, 0, 5], [2, 1, 6], [3, 4, 0]]
matrixM_inv = np.linalg.inv(matrixM)
print(matrixM_inv) 


