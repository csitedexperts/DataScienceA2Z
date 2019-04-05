
# Importing the libraries
import numpy as np
import pandas as pd

"""
Generate a m x n data matrix X, initially polulated with zeros.
"""

rowCount = 10 # m 
colCount = 40  # n

X = np.zeros((rowCount, colCount), dtype = int)
#X = np.zeros((rowCount, colCount), dtype = float)

print (X)
   

"""

Populate the First column with indentpendly identically distributed (i.i.d.) 
random variables N(125, 16) (simulating height), 
and the second column with i.i.d. randomN(125 variables , 64) (simulating weight).

"""
height = X[:, 0]  # Assign the First Column as height
weight = X[:, 1]  # Assign the Second Column as weight

print (height)
print (weight)

whRatioList = [0.0] * (rowCount) # Generating a list of size rowCount
whRatioArray = np.asarray(whRatioList) # Converting the list into array
print (whRatioArray.size)

for i in range(whRatioArray.size):
    height[i] = np.random.normal(loc=125, scale= 4, size=1)
    weight[i] = np.random.normal(loc=125, scale= 8, size=1)
    whRatioArray[i] = weight[i]/height[i]

"""

Populate the First row with indentpendly identically distributed (i.i.d.) 
random variables N(125, 16) (simulating height), 
and the second row with i.i.d. randomN(125 variables , 64) (simulating weight).

"""

dataRow1 = X[0]  # Assign the First Row as dataRow1
dataRow2 = X[1]  # Assign the Second Row as dataRow2
print (dataRow1)
print (dataRow2)


for i in range(whRatioArray.size):
    print("Weight[%d] = %d " % (i, weight[i]))
    print("Height[%d] = %d " % (i, height[i]))
#    print("Weight[%d] / Height[%d] = %d / %d = %.2f" % (i, i, weight[i], height[i], (weight[i]/height[i])))
    print("Weight[%d] / Height[%d] = %d / %d = %f" % (i, i, weight[i], height[i], whRatioArray[i]))


# Importing the Titanic .csv data file
titanicDS = pd.read_csv('Dummy_Titanic_Data.csv')
print (titanicDS)


###########  Using iloc() Method

sl_no = titanicDS.iloc[:, 0].values
print (sl_no)






col12 = titanicDS.iloc[:, [1, 2]].values
print (col12)

col123 = titanicDS.iloc[:, [1, 2, 3]].values
print (col123)


col12347 = titanicDS.iloc[:, [1, 2, 3, 4, 7]].values
print (col12347)



col1_7 = titanicDS.iloc[:, 1:7].values
print (col1_7)


















passerger1 = titanicDS.iloc[0]
print (passerger1)


passerger2 = titanicDS.iloc[1]
print (passerger2)

passerger3 = titanicDS.iloc[2]
print (passerger3)

passerger4 = titanicDS.iloc[3]
print (passerger4)



passergerTop10 = titanicDS.head(10)
print (passergerTop10)

#   - -  - - - - - - -

passerger2436 = titanicDS.iloc[2435]
print (passerger2436)


#passerger2436 = titanicDS.iloc[2436]  # Invalid - Out of bounds
#print (passerger2436)


passergerTop10 = titanicDS.head(10)
print (passergerTop10)

passerger12 = titanicDS.iloc[[0,1]]
print (passerger12)



passerger12_100 = titanicDS.iloc[[0,1,99]]
print (passerger12_100)


passerger12x127 = titanicDS.iloc[[0,1], [0,1,7]]
print (passerger12x127)


passerger12x1247 = titanicDS.iloc[[0,1], [0,1,4,7]]
print (passerger12x1247)



###########  Using loc() Method

passerger12x1247 = titanicDS.loc[[0,1], ['Gender', 'Age']]
print (passerger12x1247)


passergerAllGenderAge = titanicDS.loc[:, ['Gender', 'Age']]
print (passergerAllGenderAge)

passergerAllGenderAge = titanicDS.loc[:, 'Gender':'Ticket_Fare']
print (passergerAllGenderAge)

passergerAllGenderAge = titanicDS.loc[titanicDS.Gender == 1, 'Age':'Ticket_Fare']
print (passergerAllGenderAge)

passergerAllGenderAge = titanicDS.loc[titanicDS.Age >= 40, 'Age':'Ticket_Fare']
print (passergerAllGenderAge)



###########  Using ix() 
passergerAllGenderAge = titanicDS.ix[0:9, 'Gender':'Ticket_Fare']
print (passergerAllGenderAge)


#  Next Time: IA, I will discuss more on Matrix and Vector assignments, if needed


  