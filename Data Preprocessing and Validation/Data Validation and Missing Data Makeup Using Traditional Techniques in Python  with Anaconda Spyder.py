# Importing the libraries

import pandas as pd
import math
import statistics 

# Importing the Salary .csv data set
salaryDS = pd.read_csv('Invalid_Salary_Data1.csv')
print (salaryDS)

exp = salaryDS.iloc[:, 0].values

#print ("exp: ", exp)

exp_mean = statistics.mean(exp) # Is this a Valid / Invalid mean??

exp_median = statistics.median(exp)
#exp_mode = statistics.mode(exp)

print ("exp_mean: ", exp_mean)
print ("exp_median: ", exp_median)
#print ("exp_mode: ", exp_mode)

#print ("exp: ", exp)
print ("exp size: ", exp.size)

for i in range(exp.size):
    print("exp[%d] = %.f " % (i, exp[i]))

for i in range(exp.size):
    if (exp[i]) < 0:
        print("exp[%d] = %.f " % (i, exp[i]))


for i in range(exp.size):
    if (exp[i]) > 8:
        print("exp[%d] = %.f " % (i, exp[i]))
 
for i in range(exp.size):
    if (math.isnan(exp[i])):
        print("exp[%d] = %.f " % (i, exp[i]))
    
for i in range(exp.size):
    if (math.isnan(exp[i])):
        exp[i] = statistics.median(exp)        
        print("exp[%d] = %.f " % (i, exp[i]))

for i in range(exp.size):
    if (exp[i] < 0 ):
        exp[i] = abs(exp[i])        
        print("exp[%d] = %.f " % (i, exp[i]))

#print ("exp: ", exp)
print ("exp size: ", exp.size)

exp_mean_Recalculated = statistics.mean(exp)  # Recalculated mean

print ("exp_mean _Recalculated: ", exp_mean_Recalculated)
print ("exp_median: ", exp_median)



# Importing the Salary .csv data set
salaryDS_inv1 = pd.read_csv("Invalid_Salary_Data1.csv")
print (salaryDS_inv1)

salary_inv1 = salaryDS_inv1.iloc[:, 1].values

print ("salary _inv1: ", salary_inv1) 
print ("salary _inv1 size: ", salary_inv1.size)


salary_mean_inv1 = statistics.mean(salary_inv1)
salary_median_inv1 = statistics.median(salary_inv1)

print ("salary_mean _inv1: ", salary_mean_inv1)
print ("salary_median _inv1: ", salary_median_inv1)


# Please try it yourself


for i in range(salary_inv1.size):
    if (math.isnan(salary_inv1[i])):
        salary_inv1[i] = statistics.median(salary_inv1)
        print("salary_inv1[%d] = %.f " % (i, salary_inv1[i]))

print ("salary_inv1: ", salary_inv1)
print ("salary_inv1 size: ", salary_inv1.size)

salary_inv1_mean_Recalculated = statistics.mean(salary_inv1)  # Recalculated mean
salary_inv1_median_Recalculated = statistics.median(salary_inv1)  # Recalculated mean

print ("salary_inv1_mean _Recalculated: ", salary_inv1_mean_Recalculated)
print ("salary_inv1_median _Recalculated: ", salary_inv1_median_Recalculated)



# Please try it yourself *************************

# Importing the Titanic .csv data file
titanicDS_inv1 = pd.read_csv('Invalid_Titanic_Data1.csv')
#print (titanicDS_Inv1)
age_inv1 = titanicDS_inv1.iloc[:, 4].values

#print ("age_inv1: ", age_inv1)
age_mean_inv1 = statistics.mean(age_inv1)
age_median_inv1 = statistics.median(age_inv1)

print ("age_mean_inv1: ", age_mean_inv1)
print ("age_median_inv1: ", age_median_inv1)


# Please try it yourself *************************


















## Hints

for i in range(age_inv1.size):
    if (age_inv1[i] < 0):
        print("age_inv1[%d] = %.f " % (i, age_inv1[i]))
        age_inv1[i] = abs(age_inv1[i])        
        print("age_inv1[%d] = %.f " % (i, age_inv1[i]))

#print ("age_inv1: ", age_inv1)
print ("age_inv1 size: ", age_inv1.size)

age_mean_Recalculated = statistics.mean(age_inv1)  # Recalculated mean

print ("age_mean _Recalculated: ", statistics.mean(age_inv1))
print ("age_median: ", statistics.median(age_inv1))





## Let's look bacl to the original data set
# Importing the Titanic .csv data file
titanicDS = pd.read_csv('Dummy_Titanic_Data.csv')
age = titanicDS.iloc[:, 4].values

ticket_fare = gender = titanicDS.iloc[:, 7].values

age_mean = statistics.mean(age)
age_median = statistics.median(age)

print ("age_mean: ", age_mean)
print ("age_median: ", age_median)



# Another Data Validation and Missing Data Makeup Problem/Solution

# Importing the libraries

import numpy as np

"""
Generate a 10x4 random DS, initially polulated with zeros.
"""

rowCount = 10
colCount = 4
randomDS = np.zeros((rowCount, colCount), dtype = int)
#randomDS = np.zeros((rowCount, colCount), dtype = float)

print (randomDS)
   

"""

Populate the First column with i.i.d. 
random variables N(16, 100) for simulating height), 
and the second column with i.i.d. random N(25, 225))
 for simulating weight).

"""
height = randomDS[:, 0]
weight = randomDS[:, 1]

for i in range(rowCount):
    height[i] = np.random.normal(loc=16, scale= 10, size=1)
    weight[i] = np.random.normal(loc=25, scale= 15, size=1)

print ("weight: ", weight)
print ("height: ", height)

print ("\n")
for i in range(rowCount):
    if (weight[i] <= 0 ):
        weight[i] = abs(weight[i]) + 50
    elif (height[i] <= 0 ):
        height[i] = abs(height[i]) + 20
            
print("After cleaning/preprocessing:") 
print ("Cleaned /Preprocessed weight: ", weight)
print ("Cleaned /Preprocessed height: ", height)

