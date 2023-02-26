#-------------------------------------------------------------------------
# AUTHOR: Joshua Reyes
# FILENAME: decision_tree_2.py
# SPECIFICATION:  test and train a decision tree
# FOR: CS 4210- Assignment #2
# TIME SPENT: ~1 1/2 hrs
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn import tree
import csv

dataSets = ['contact_lens_training_1.csv', 'contact_lens_training_2.csv', 'contact_lens_training_3.csv']

for ds in dataSets:

    dbTraining = []
    dbTest = []
    X = []
    Y = []
    correct = 0
    not_correct = 0
    #reading the training data in a csv file
    with open(ds, 'r') as csvfile:
         reader = csv.reader(csvfile)
         for i, row in enumerate(reader):
             if i > 0: #skipping the header
                dbTraining.append (row)

    #transform the original categorical training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
    # so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
    #--> add your Python code here
    # X =
    for row in dbTraining: 
        xRow = []
        for i, value in enumerate(row): 
            if i == 0:
                xRow.append(1 if value == "Young"  else 2 if value == "Preprebyopic" else 3)
            elif i == 1:
                xRow.append(1 if value == "Myope" else 2)
            elif i == 2:
                xRow.append(1 if value == "No" else 2)
            elif i == 3:
                xRow.append(1 if value == "Reduced" else 2)
        X.append(xRow)
    #transform the original categorical training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
    #--> add your Python code here
    # Y =
    for row in dbTraining: 
        for i, value in enumerate(row):
            if i == 4:
                Y.append(1 if value == "Yes" else 2)
    #loop your training and test tasks 10 times here
    for i in range (10):

       #fitting the decision tree to the data setting max_depth=3
       clf = tree.DecisionTreeClassifier(criterion = 'entropy', max_depth=3)
       clf = clf.fit(X, Y)

       #read the test data and add this data to dbTest
       #--> add your Python code here
       # dbTest =
       with open('contact_lens_test.csv', 'r') as csvfile:
         reader = csv.reader(csvfile)
         for i, row in enumerate(reader):
             if i > 0: #skipping the header
                dbTest.append (row)

       for data in dbTest:
           #transform the features of the test instances to numbers following the same strategy done during training,
           #and then use the decision tree to make the class prediction. For instance: class_predicted = clf.predict([[3, 1, 2, 1]])[0]
           #where [0] is used to get an integer as the predicted class label so that you can compare it with the true label
           #--> add your Python code here
            for row in dbTest: 
                xRow = []
                for i, value in enumerate(row): 
                    if i == 0:
                        xRow.append(1 if value == "Young"  else 2 if value == "Preprebyopic" else 3)
                    elif i == 1:
                        xRow.append(1 if value == "Myope" else 2)
                    elif i == 2:
                        xRow.append(1 if value == "No" else 2)
                    elif i == 3:
                        xRow.append(1 if value == "Reduced" else 2)
                class_predicted = clf.predict([xRow])[0]                

           #compare the prediction with the true label (located at data[4]) of the test instance to start calculating the accuracy.
           #--> add your Python code here
            if(class_predicted == data[4]):
                correct += 1;
            else:
                not_correct += 1;
            accuracy = correct / (correct+not_correct)
            print(accuracy)



    #find the average of this model during the 10 runs (training and test set)
    #--> add your Python code here

    #print the average accuracy of this model during the 10 runs (training and test set).
    #your output should be something like that: final accuracy when training on contact_lens_training_1.csv: 0.2
    #--> add your Python code here


