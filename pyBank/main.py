from cgi import print_form
import os
import csv
#from tkinter.tix import COLUMN
csvpath= os.path.join("pyBank\\resources\\Resources_py_bank.csv")
# csvpath= os.path.join("C:\\Users\\appua\\OneDrive\\Desktop\\Analysis _projects\\My_Challenge1\\pyBank\\resources\\Resources_py_bank.csv")
with open(csvpath) as csvfile :
    csv_reader= csv.reader(csvfile,delimiter =",")
    
    #skip header ,Here  Header should not be skipped in counting rows
    date = []
    revenue = []
    revenue_change = []
    date_month = []
 
    row_count = 0
    total = 0
    avg_rev_change = 0
    date_max = {}
    date_increase = ""
    next(csv_reader)

    for row in csv_reader:
        row_count +=  1 # we used comprehension ,to calculate number of rows
        total = total + int(row[1])  #to count total.   
        # revenue.append(int(row[1]))
        revenue.append(int(row[1]))
        date.append(row[0])
    
#calculate changes in profits/losses over entire period,and average of those changes
    
    for i in range(1,len(revenue)):   
           revenue_change.append(revenue[i] - revenue[i-1])
           avg_rev_change = round(sum(revenue_change)/len(revenue_change),2)

    max_increase_value = max(revenue_change)
    min_increase_value = min(revenue_change)   
    bank_py ="Financial Analysis \n ----------------------------------------\n Toatl months:{} \n Total: $ {} \n Average Change:$ {} \n Greatest increase in Profits: $ ({})\n Greatest decrease in profits: $({})".format(row_count,total,avg_rev_change,max_increase_value,min_increase_value)
                
    print("Financial Analysis")
    print("-------------------------------------------------------") 
    print("total months:" ,row_count)
    print("Total:" , "$" , total)
    print("Average Change: ","$" , avg_rev_change)

    print(f"Greatest Increase in Profits:",  "$" ,(int(max_increase_value)))
    print(f"Greatest Decrease in Profits:",  "$" ,(int(min_increase_value)))
    
    
    #output to file
file1 = open("pybank.txt","w") 
file1.writelines(bank_py) #Write analysis into pybank.txt
file1.close()
