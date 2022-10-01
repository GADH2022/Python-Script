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
    print(revenue)
    print(date)
#calculate changes in profits/losses over entire period,and average of those changes
    
    for i in range(1,len(revenue)):   
           revenue_change.append(revenue[i] - revenue[i-1])
           avg_rev_change = round(sum(revenue_change)/len(revenue_change),2)

    date_max=dict(zip(revenue_change, date))
    print(date_max) 
    max_increase_value = max(revenue_change)
    min_increase_value = min(revenue_change)   
    for key,value in date_max.items():
        if(date_max[key]-1 == max_increase_value):
            date_increase = value
        #   date_increase_1 = value+1 
    # for max_increase_value in date_max.items():
    #     date_increase = {date, max_increase_value}
    print(date_increase)
    # print(date_increase+1)
    # max_increase_month = revenue_change.index(max_increase_value)+ 1
    # max_decrease_month = revenue_change.index(min_increase_value)+ 1 
    # print(max_increase_month) 
    # print(max_decrease_month)  
    print("Financial Analysis")
    print("-------------------------------------------------------") 
    print("total months:" ,row_count)
    print("Total:" , "$" , total)
    print("Average Change: ","$" , avg_rev_change)

    # print(f"Greatest Increase in Profits:", {max_increase_month}, "$" ,(int(max_increase_value)))
    # print(f"Greatest Decrease in Profits:", {max_decrease_month}, "$" ,(int(min_increase_value)))
    
    #calculate Greatest increase in profits(date and amount)
    #calculate Greatest decrease in profits(date and amount)
#output to file
#file1 = open("pybank.txt","w") 
#file1.writelines() #Write analysis into pybank.txt

