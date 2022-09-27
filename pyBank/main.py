import os
import csv
csvpath= os.path.join("resources", "Resources_py_bank.csv")
with open(csvpath) as csvfile :
   csv_reader= csv.reader(csvfile,delimiter ="-")
 #  num_months = len()
   print("Financial Analysis")
   print ("-----------------------------------------------------")
   print("Total months:",num_months)
