import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def welcome():
    print("Welcome to Salary Prediction System")
    print("Please ENTER key to proceed")
    input()

def checkcsv():
    csv_files=[]
    cur_dir=os.getcwd() #current working directory
    content_list=os.listdir(cur_dir)
    for x in content_list:
        if x.split('.')[-1]=='csv':
            csv_files.append(x)
    if len(csv_files)==0:
        return "No csv file in the directory"
    else:
        return csv_files
    
def display_and_select_csv(csv_files):
    i=0
    for file_name in csv_files:
        print(i,'...',file_name)
        i+=1
    return csv_files[int(input("select file to create ML Model"))]

def main():
    welcome()
    try:
        csv_files=checkcsv()
        if csv_files=='No csv file in the directory':
            raise FileNotFoundError('No csv file in the directory')
        csv_file=display_and_select_csv(csv_files)
        print(csv_file,'is selected')
        print('Reading csv file')
        print('Creating Dataset')
        dataset=pd.read_csv(csv_file)
        print('Created dataset')
        x=dataset.iloc[:,:-1].values
        y=dataset.iloc[:,-1].values
        
        s=float(input("Enter test data size (between 0 and 1)"))
        x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=s)
        
        print("Model creation in progression")
        regressionObject=LinearRegression()
        regressionObject.fit(x_train,y_train)
        print("Model is created")
        print("Pres Enter key to predict test data in trained model")
        input()

        y_pred=regressionObject.predict(x_test)
        


    except FileNotFoundError:
        print('No csv file in the directory')
        

if __name__=="__main__":
    main()
    input()
