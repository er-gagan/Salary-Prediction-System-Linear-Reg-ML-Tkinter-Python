import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

X_train=Y_train= regressionObject= X_test= Y_test= Y_pred=None

def checkcsv():
    csv_files=[]
    cur_dir=os.getcwd()
    content_list=os.listdir(cur_dir)
    for x in content_list:
        if x.split('.')[-1]=='csv':
            csv_files.append(x)
    if len(csv_files)==0:
        return 'No csv file in the directory'
    else:
        return csv_files
    
def display_and_select_csv(csv_files):
    i=0
    csvlist = []
    for file_name in csv_files:
        csvlist.append(("Press",i,'...',file_name))
        csvlist.append("\n")
        i+=1
    return csvlist
    

def test_model(csvfile_select,testdata):
    global X_train,Y_train, regressionObject, X_test, Y_test, Y_pred
    dataset=pd.read_csv(csvfile_select)
    X=dataset.iloc[:,:-1].values
    Y=dataset.iloc[:,-1].values
    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=float(testdata))
    regressionObject=LinearRegression()
    regressionObject.fit(X_train,Y_train)
    Y_pred=regressionObject.predict(X_test)
    i=0
    xtest = []
    ytest = []
    ypred = []
    while i<len(X_test):
        xtest.append((float(X_test[i])))
        ytest.append(int(Y_test[i]))
        ypred.append(int(Y_pred[i]))
        i+=1
    return xtest,ytest,ypred

def show_data():
    global X_train,Y_train, regressionObject, X_test, Y_test, Y_pred
    plt.scatter(X_train,Y_train,color='red',label='training data')
    plt.plot(X_train,regressionObject.predict(X_train),color='blue',label='Best Fit')
    plt.scatter(X_test,Y_test,color='green',label='test data')
    plt.scatter(X_test,Y_pred,color='black',label='Pred test data')
    plt.title("Salary vs Experience")
    plt.xlabel('Years of Experience')
    plt.ylabel('Salary')
    plt.legend()
    plt.show()

def salary_predict(year):
    exp=[float(e) for e in year.split(',')]
    ex=[]
    for x in exp:
        ex.append([x])
    experience =np.array(ex)
    salaries=regressionObject.predict(experience)

    plt.scatter(experience,salaries,color='black')
    plt.xlabel('Years of Experience')
    plt.ylabel('Salaries')
    plt.show()

    d=pd.DataFrame({'Experience':exp,'Salaries':salaries})
    return d
