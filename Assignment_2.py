import math
import sys
from databaseFunc import databaseNeeds
from datetime import datetime
URI = "mongodb://localhost:27017/"

def shortestDistance(x1, y1, x2, y2):

    try:
        post_data = {
            'x1': x1,
            'x2':x2,
            'y1':y1,
            'y2':y2,
            'timestamp': 'Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.now())

        }
        #Insert into Entries database
        databaseNeeds.insertEntries(post_data)
        sDist = math.sqrt(((float(x2) - float(x1))*(float(x2) - float(x1))) + ((float(y2) - float(y1)) * (float(y2) - float(y1))))
        print('Shortest distance is: '+ str(sDist) +'\n')
        post_data = {
            'Shortest_Distance': sDist,
            'timestamp': 'Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.now())

        }
        databaseNeeds.insertResults(post_data)
    except ValueError:
        print('Error - incorrect data type used')
        pickAFunc()


def retirement(age, annualSalary, percentSaved, retirementSaveGoal):
    # print("")
    try:
        yearLeft = 0;
        amountTotal = 0;
        age = int(age);
        post_data = {
            'age': age,
            'annualSalary': annualSalary,
            'percentSaved': percentSaved,
            'retirementSaveGoal': retirementSaveGoal,
            'timestamp': 'Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.now())

        }
        databaseNeeds.insertEntries(post_data)
        retirementSaveGoal = int(retirementSaveGoal)

        amount = int(annualSalary) * (float(percentSaved) / 100);
        amountT = amount * 0.35;

        while amountTotal < retirementSaveGoal and age < 100:
            yearLeft = yearLeft + 1;
            age = age + 1;
            if age == 100:
                print("Dead, you didn't make the goal")
                return "Dead"

            amountTotal = amountTotal +amountT + amount;
            # print(amountTotal)
            # print("Your age "+ str(age))
        print("Goal amount will be reached at " + str(age))
        databaseNeeds.insertResults(post_data)
        return age

    except ValueError:
        print("Invalid Type")
        raise ValueError("Invalid arguments.")

def pickAFunc():

    if(databaseNeeds.connection()):
       True
    else:
       sys.exit()
    funcOption = input('Pick a function'+
                 '\n1 - Shortest Distance' +
                 '\n2 - Retirement'
                 '\n0 - Exit\n'
                 )



    if (funcOption == 1):
        #Prints Previous Data Stored Locally
        x = {"_id": 0, "x1": 1, "x2": 1, 'y1': 1, "y2": 1, "timestamp": 1}
        databaseNeeds.printData(x)
        getX1 = input ('Please enter your x1 value\n')
        getY1 = input ('Please enter your y1 value\n')
        getX2 = input ('Please enter your x2 value\n')
        getY2 = input ('Please enter your y2 value\n')
        shortestDistance(getX1, getY1, getX2, getY2)

        pickAFunc()

    elif (funcOption == 2):

        # Prints Previous Data Stored Locally
        x = {"_id": 0, "age": 1, "annualSalary": 1 ,'percentSaved':1,"retirementSaveGoal":1}
        databaseNeeds.printData(x)
        age = input("How old are you?")
        annualSalary = input("what is your annual Salary")
        percentSaved = input("what percentage saved")
        retirementSaveGoal = input("what is your retirement saving goal?")
        retirement(age, annualSalary, percentSaved, retirementSaveGoal)
        pickAFunc()
    elif (funcOption == '0'):
            sys.exit()
    else:
        pickAFunc()


pickAFunc()
