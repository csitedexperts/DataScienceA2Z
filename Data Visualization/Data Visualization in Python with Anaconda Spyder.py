
# Importing the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Importing the Salary .csv data set
salaryDS = pd.read_csv('Dummy_Salary_Data.csv')
#print (salaryDS)

exp = salaryDS.iloc[:, 0].values
salary = salaryDS.iloc[:, 1].values

#print (exp)
#print (salary)

"""
Visualize/plot your preprocessed data (in two dimensions).

"""
# import matplotlib.pyplot as plt

plt.plot(exp, color = "blue")  
plt.plot(salary, color = 'red')  
plt.title("Plot Visualization of Processed Samples")
plt.xlabel("Experience (in year)")
plt.ylabel("Salary  ($/Year)")
plt.grid()
plt.show()


"""
Compute a Histogram for the Experience data.
"""
plt.hist(exp, bins=20)  # arguments are passed to np.histogram
plt.title("Experience (in year) Histogram with Preprossed Data ")
plt.grid()
plt.show()


"""
Conclusion: A histogram plot shows that ....
    
"""

### Try / Fix it yourself

# Importing the Titanic .csv data set
titanicDS = pd.read_csv('Dummy_Titanic_Data.csv')
#print (titanicDS)

survival_status = titanicDS.iloc[:, 1].values
ticket_class = titanicDS.iloc[:, 2].values
gender = titanicDS.iloc[:, 3].values
age = titanicDS.iloc[:, 4].values
ticket_fare = gender = titanicDS.iloc[:, 7].values

#print (survival_status)
#print (ticket_class)
#print (gender)
#
#print (age)
#print (ticket_fare)


"""
Visualize/plot your preprocessed data (in two dimensions).

"""
import matplotlib.pyplot as plt

plt.plot(gender, color = 'blue')  
plt.plot(age, color = 'red')  
plt.title("Plot Visualization of Processed Samples")
plt.xlabel("Gender (Male / Female)")
plt.ylabel("Age (in year)")
plt.grid()
plt.show()




"""
Compute a Histogram for Experience and Salary data.
"""
plt.hist(gender, bins=2)  # arguments are passed to np.histogram
plt.title("Gender Histogram with Preprossed Data")
plt.grid()
plt.show()

"""
Conclusion: A histogram plot shows that ....
    
"""



"""
 Making Normal Distributed Chart 
"""

mean, stdev = 0.5, 0.1

dataset = np.random.normal(mean, stdev, size=100)

# Create the bins and histogram
count, bins, ignored = plt.hist(dataset, bins=100, normed=True)

# Plot the normal distribution curve
plt.plot(bins, 1/(stdev * np.sqrt(2 * np.pi)) *
    np.exp( - (bins - mean)**2 / (2 * stdev**2) ),  linewidth=3, color='red')
plt.grid()
plt.show()




"""
 Another Normal Distributed program with method  
"""

class NormalDistribution:
    def __init__(self, a1, b1, c1):
        self.a1 = a1
        self.b1 = b1
        self.c1 = c1
        
    def distributionCurve(self):
        plt.plot(self.c1, 1/(self.b1 * np.sqrt(2 * np.pi)) *
            np.exp( - (self.c1 - self.a1)**2 / (2 * self.b1**2) ), linewidth=2, color='red')
        plt.grid()
        plt.show()

mean, stdev = 5, 2 
dataset = np.random.normal(mean, stdev, size=1000)
        
w1, x1, z1 = plt.hist(dataset, bins=100, normed=True) #hist

hist = NormalDistribution(mean, stdev, x1)
plot = hist.distributionCurve()



"""
Conclusion: The normal plot shows that ...

    
"""



### Try / Fix it yourself


"""
Generate a 10x4 random DS, initially polulated with zeros.
"""
rowCount = 10
colCount = 4
randomDS = np.zeros((rowCount, colCount), dtype = int)
#print (randomDS)

"""
Populate the First column with i.i.d. 
random variables N(100, 10) for simulating height), 
and the second column with i.i.d. random N(125, 15))
 for simulating weight).

"""
height = randomDS[:, 0]
weight = randomDS[:, 1]

for i in range(rowCount):
    height[i] = np.random.normal(loc=100, scale= 10, size=1)
    weight[i] = np.random.normal(loc=125, scale= 15, size=1)

print ("weight: ", weight)
print ("height: ", height)

"""
Visualize/plot your preprocessed data (in two dimensions).

"""
plt.plot(weight, color = 'blue')  
plt.plot(height, color = 'red')  
plt.title("Plot Visualization of Processed Samples")
plt.xlabel("Height (in cm)")
plt.ylabel("Weight (in lb)")
plt.grid()
plt.show()


"""
Conclusion: The scatter plot shows that ...

    
"""

plt.hist(weight, bins=10)  # arguments are passed to np.histogram
plt.title("Weight Histogram with Preprossed Data ")
plt.show()


plt.hist(height, bins=10)  # arguments are passed to np.histogram
plt.title("Height ratio Histogram with Preprossed Data ")
plt.grid()
plt.show()

"""
Conclusion: A histogram plot shows that ...

    
"""
