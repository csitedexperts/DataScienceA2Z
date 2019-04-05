# Importing the libraries

import pandas as pd
import statistics 

# Importing the dataset from a .csv file
invalidDS = pd.read_csv('Invalid_Salary_Data1.csv')

exp = invalidDS.iloc[:, 0].values
salary = invalidDS.iloc[:, 1].values
#print ("exp: ", exp)
exp_mean = statistics.mean(exp) # Is this a Valid / Invalid mean??
exp_median = statistics.median(exp)
print ("exp_mean: ", exp_mean)
print ("exp_median: ", exp_median)

#print ("salary: ", salary)
salary_mean = statistics.mean(salary) # Is this a Valid / Invalid mean??
salary_median = statistics.median(salary)
print ("salary_mean: ", salary_mean)
print ("salary_median: ", salary_median)


invalid_DS = invalidDS.iloc[:, 0:2].values

print (invalid_DS)


#### Another alternative and nicer way

# Making up missing data using Imputer 
from sklearn.preprocessing import Imputer


validated_DS = invalid_DS 
# => validated_DS = invalidDS.iloc[:, 0:2].values

print (validated_DS)  ### Not valid yet, right?
 
##  Please take care of the negative Exp values by yourself.



imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(validated_DS[:, 0:2]) ## [0, 2) => [0, 1]
validated_DS[:, 0:2] = imputer.transform(validated_DS[:, 0:2])


print (validated_DS)   ### Now vaild, right??


validated_exp = validated_DS[:, 0] ### Give attention here
validated_salary = validated_DS[:, 1]  ### Give attention here

print (validated_exp)
print (validated_salary)

validated_exp_mean = statistics.mean(validated_exp) 
# Now it is a valid statement 
validated_exp_median = statistics.median(validated_exp)
# Now it is a valid statement 

print ("validated_exp_mean: ", validated_exp_mean)
print ("validated_exp_median: ", validated_exp_median)

validated_salary_mean = statistics.mean(validated_salary) 
validated_salary_median = statistics.median(validated_salary)
# Now this is a valid statement 

print ("validated_salary_mean: ", validated_salary_mean)
print ("validated_salary_median: ", validated_salary_median)

