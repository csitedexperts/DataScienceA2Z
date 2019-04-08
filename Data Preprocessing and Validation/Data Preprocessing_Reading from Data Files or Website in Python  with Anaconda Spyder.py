# Importing the libraries

import pandas as pd

# Importing dataset from a .csv data file

#fileLocation = "Dummy_Salary_Data.csv"
#fileLocation = 'Dummy_Salary_Data.csv'

#fileLocation = "C:\\Users\\mhossa12\\workspace\\DataScienceA2Z\\Data Preprocessing and Validation\\Dummy_Salary_Data.csv"
fileLocation = "C:/Users/mhossa12/workspace/DataScienceA2Z/Data Preprocessing and Validation/Dummy_Salary_Data.csv"

datasetDS = pd.read_csv(fileLocation)
print (datasetDS)

dataMatrix = datasetDS.iloc[:, 0:2].values  ## [0, 2)
print (dataMatrix)


expMatrix1 = datasetDS.iloc[:, 0:1].values
salMatrix1 = datasetDS.iloc[:, 1:2].values
print (expMatrix1)
print (salMatrix1)

expVector1 = datasetDS.iloc[:, 0].values
salVector1 = datasetDS.iloc[:, 1].values
print (expVector1)
print (salVector1)

print ("expVector1 size: ", expVector1.size)
print ("salVector1.size ", salVector1.size )

expVector2 = dataMatrix[:, 0]
salVector2 = dataMatrix[:, 1]
print (expVector2)
print (salVector2)

print ("expVector2 size: ", expVector2.size)
print ("salVector2.size ", salVector2.size )

for i in range(expVector1.size):
    print("expVector1[%d] = %.f " % (i, expVector1[i]))

for i in range(expVector1.size):
    if (expVector1[i]) < 2:
        print("expVector1[%d] = %.f " % (i, expVector1[i]))
		
for i in range(expVector1.size):
    if (expVector1[i]) > 8:
        print("expVector1[%d] = %.f " % (i, expVector1[i]))
 
 
 
### Try it yourself 


# Importing the Titanic .csv data file
titanicDS = pd.read_csv('Dummy_Titanic_Data.csv')
print (titanicDS)

titanicDM = titanicDS.iloc[:, 0:8].values
print (titanicDM)

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


# Importing dataset from a .xls data file
titanic3DS = pd.read_excel('TitanicData3.xls')
print (titanic3DS)



# Importing dataset from a web site file

#fileLocation = webURL
fileLocation = "http://bit.ly/uforeports"
datasetDS = pd.read_csv(fileLocation)

### Try it yourself 

