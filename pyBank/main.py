import os
import csv
csvpath= os.path.join("pyBank\\resources\\Resources_py_bank.csv")
# csvpath= os.path.join("C:\\Users\\appua\\OneDrive\\Desktop\\Analysis _projects\\My_Challenge1\\pyBank\\resources\\Resources_py_bank.csv")
with open(csvpath) as csvfile :
    csv_reader= csv.reader(csvfile,delimiter =",")
    
    #skip header
    # csv_header=next(csv_reader) 
    row = 0
    for row in csv_reader:
         #num_months = len(row)
        print("Financial Analysis")
        print ("-----------------------------------------------------")
        row_count = sum(1 for row in csv_reader)
        print(f"Total months:" ,row_count)
        # print((row))
    # if ((profits/losses).Value > 0)  
           

