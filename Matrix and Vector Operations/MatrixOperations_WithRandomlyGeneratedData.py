
# Importing the libraries
import random
import numpy as np

"""
Generate some random numbers.
"""

mylist = []
totalNumbers = 100
minNumber = 0
maxNumber = 10

for i in range(0, totalNumbers):   # [start, end) =>  [0, totalNumbers)
    x = random.randint(minNumber,maxNumber)  # [minNumber, maxNumber]
    mylist.append(x)

print(mylist)


"""
Generate a 10 x 4 data matrix X, initially polulated with zeros.
"""

rowCount = 10
colCount = 4
X = np.zeros((rowCount, colCount), dtype = int)
#X = np.zeros((rowCount, colCount), dtype = float)

print (X)
   

"""

Populate the First column with indentpendly identically distributed (i.i.d.) 
random variables N(125, 16) (simulating height), 
and the second column with i.i.d. randomN(125 variables , 64) (simulating weight).

"""
height = X[:, 0]
weight = X[:, 1]

print (height)
print (weight)

whRatioList = [0.0] * (rowCount) # Generating a list of size rowCount
whRatioArray = np.asarray(whRatioList) # Converting the list into array
print (whRatioArray.size)

for i in range(whRatioArray.size):
    height[i] = np.random.normal(loc=125, scale= 4, size=1)
    weight[i] = np.random.normal(loc=125, scale= 8, size=1)
    whRatioArray[i] = weight[i]/height[i]

print (weight)
print (height)

for i in range(whRatioArray.size):
    print("Weight[%d] = %d " % (i, weight[i]))
    print("Height[%d] = %d " % (i, height[i]))
#    print("Weight[%d] / Height[%d] = %d / %d = %.2f" % (i, i, weight[i], height[i], (weight[i]/height[i])))
    print("Weight[%d] / Height[%d] = %d / %d = %f" % (i, i, weight[i], height[i], whRatioArray[i]))

