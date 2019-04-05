# Importing the libraries
import pandas as pd
import statistics 

#import scipy as statistics 

data1 = [1, 2, 3, 4, 4, 5, 7, 9] 

data1_mean = statistics.mean(data1) 


print("Mean is :", data1_mean) 
print("Mean is : %.2f" % (data1_mean))
print("Mean is : %.3f" % (data1_mean))
print("Mean is : %.4f" % (data1_mean))
print("Mean is : %.5f" % (data1_mean))
print("Mean is : %.6f" % (data1_mean))
 
data1_median = statistics.median(data1) 
print("Median is :", data1_mean) 
data1_mode = statistics.mode(data1) 
print("Mode is :", data1_mode) 
data1_stdev = statistics.stdev(data1) 
print("Stdev is :", data1_stdev) 
data1_variance = statistics.variance(data1) 
print("Variance is :", data1_variance) 



# Importing the Salary .csv data set
salaryDS = pd.read_csv('Dummy_Salary_Data.csv')
print (salaryDS)

exp = salaryDS.iloc[:, 0].values
salary = salaryDS.iloc[:, 1].values

print ("exp: ", exp)

exp_mean = statistics.mean(exp)
exp_median = statistics.median(exp)
exp_mode = statistics.mode(exp)
exp_stdv = statistics.stdev(exp)
exp_variance = statistics.variance(exp)

print ("exp_mean: ", exp_mean)
print ("exp_median: ", exp_median)
print ("exp_mode: ", exp_mode)
print ("exp_stdv: ", exp_stdv)
print ("exp_variance: ", exp_variance)


print ("salary: ", salary)

salary_mean = statistics.mean(salary)
salary_median = statistics.median(salary)
salary_mode = statistics.mode(salary)
salary_stdv = statistics.stdev(salary)
salary_variance = statistics.variance(salary)

print ("salary_mean: ", salary_mean)
print ("salary_median: ", salary_median)
print ("salary_mode: ", salary_mode)
print ("salary_stdv: ", salary_stdv)
print ("salary_variance: ", salary_variance)



# Importing the Titanic .csv data file
titanicDS = pd.read_csv('Dummy_Titanic_Data.csv')
print (titanicDS)

age = titanicDS.iloc[:, 4].values

ticket_fare = gender = titanicDS.iloc[:, 7].values

print ("age: ", age)

age_mean = statistics.mean(age)
age_median = statistics.median(age)
age_mode = statistics.mode(age)
age_stdv = statistics.stdev(age)
age_variance = statistics.variance(age)

print ("age_mean: ", age_mean)
print ("age_median: ", age_median)
print ("age_mode: ", age_mode)
print ("age_stdv: ", age_stdv)
print ("age_variance: ", age_variance)

print ("ticket_fare: ", ticket_fare)

ticket_fare_mean = statistics.mean(ticket_fare)
ticket_fare_median = statistics.median(ticket_fare)
ticket_fare_mode = statistics.mode(ticket_fare)
ticket_fare_stdv = statistics.stdev(ticket_fare)
ticket_fare_variance = statistics.variance(ticket_fare)

print ("ticket_fare_mean: ", ticket_fare_mean)
print ("ticket_fare_median: ", ticket_fare_median)
print ("ticket_fare_mode: ", ticket_fare_mode)
print ("ticket_fare_stdv: ", ticket_fare_stdv)
print ("ticket_fare_variance: ", ticket_fare_variance)
