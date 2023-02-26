#-------------------------------------------------------------------------
# AUTHOR: Joshua Reyes
# FILENAME: naive_bayes.py
# SPECIFICATION: Naive byes of weather data
# FOR: CS 4210- Assignment #2
# TIME SPENT: ~45min
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn.naive_bayes import GaussianNB
import csv
db = []
db1 = []
X = []
Y = []
#reading the training data in a csv file
#--> add your Python code here
with open('weather_training.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
         print(row)

#transform the original training features to numbers and add them to the 4D array X.
#For instance Sunny = 1, Overcast = 2, Rain = 3, so X = [[3, 1, 1, 2], [1, 3, 2, 2], ...]]
#--> add your Python code here
# X =
for row in db: 
  xRow = []
  for i, value in enumerate(row): 
    if i == 1:
      xRow.append(1 if value == "Sunny"  else 2 if value == "Overcast" else 3)
    elif i == 2:
      xRow.append(1 if value == "Hot" else 2 if value == "Mild" else 3)
    elif i == 3:
      xRow.append(1 if value == "High" else 2)
    elif i == 4:
      xRow.append(1 if value == "Weak" else 2)
  X.append(xRow)

#transform the original training classes to numbers and add them to the vector Y.
#For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> add your Python code here
# Y =
for row in db: 
  for i, value in enumerate(row):
    if i == 5:
      Y.append(1 if value == "Yes" else 2)

#fitting the naive bayes to the data
clf = GaussianNB()
clf.fit(X, Y)

#reading the test data in a csv file
#--> add your Python code here
with open('weather_test.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db1.append (row)
         print(row)
#printing the header os the solution
#--> add your Python code here
print("Day".ljust(15) + "Outlook".ljust(15) + "Temperature".ljust(15) + "Humidity".ljust(15) + "Wind".ljust(15) + "Confidence".ljust(15))
#use your test samples to make probabilistic predictions. For instance: clf.predict_proba([[3, 1, 2, 1]])[0]
#--> add your Python code here
print(clf.predict_proba(db1)[0])