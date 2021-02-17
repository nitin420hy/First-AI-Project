import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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

    except FileNotFoundError:
        print('No csv file in the directory')
        

if __name__=="__main__":
    main()
    input()
