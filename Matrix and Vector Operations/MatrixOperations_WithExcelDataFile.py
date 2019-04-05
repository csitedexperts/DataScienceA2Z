
# Importing the libraries
import pandas as pd

# Importing the Salary .csv data set
salaryDS = pd.read_csv('Dummy_Salary_Data.csv')
print (salaryDS)

exp = salaryDS.iloc[:, 0].values
salary = salaryDS.iloc[:, 1].values

print (exp)
print (salary)

# Importing the Titanic .csv data file
titanicDS = pd.read_csv('Dummy_Titanic_Data.csv')
print (titanicDS)

sl_no = titanicDS.iloc[:, 0].values
print (sl_no)

survival_status = titanicDS.iloc[:, 1].values
ticket_class = titanicDS.iloc[:, 2].values
gender = titanicDS.iloc[:, 3].values
age = titanicDS.iloc[:, 4].values

ticket_fare = gender = titanicDS.iloc[:, 7].values

print (survival_status)
print (ticket_class)
print (gender)

print (age)
print (ticket_fare)


# Importing the Titanic Excel data file
titanic3DS = pd.read_excel('Titanic_Data3.xls')
print (titanic3DS)
