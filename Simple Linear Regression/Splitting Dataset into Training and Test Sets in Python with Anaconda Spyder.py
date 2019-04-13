# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 01:14:23 2019

@author: mhossa12
"""

# Importing the required libraries
import pandas as pd
from sklearn.cross_validation import train_test_split

# Importing the Salary .csv data set
salaryDS = pd.read_csv('Dummy_Salary_Data.csv')
#print (salaryDS)
exp = salaryDS.iloc[:, 0:1].values ### NOT exp = salaryDS.iloc[:, 0].values
salary = salaryDS.iloc[:, 1].values

#print (exp)
#print (salary)

# Splitting the data sets into Training set and Test set

exp_train, exp_test = train_test_split(exp, test_size = .2, random_state = 0)

salary_train, salary_test = train_test_split(salary, train_size = .8, random_state = 0)

