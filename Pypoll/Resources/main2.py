import os
import csv
from tkinter import N
csvpath =os.path.join("Pypoll\\Resources\\election_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ",")
    header =next(csvreader)
    # skip header to count actual values
    total_votes = 0
    casper_votes = 0
    diana_votes = 0
    raymon_votes = 0
    for row in csvreader:
        total_votes = total_votes + 1
        if row[2] == "Charles Casper Stockham":
            casper_votes = casper_votes + 1
        elif row[2] == "Diana DeGette":
            diana_votes = diana_votes + 1
        elif row[2] ==  "Raymon Anthony Doane":
            raymon_votes = raymon_votes + 1   

  #lists out of data 
if((casper_votes > diana_votes) & (casper_votes > raymon_votes)):
    winner = "Charles Casper Stockham"
elif((diana_votes > casper_votes) & (diana_votes > raymon_votes)):
    winner = "Diana DeGette"
elif((raymon_votes > casper_votes) & (diana_votes < raymon_votes)):
    winner = "Raymon Anthony Doane"
# candidates = ["Charles casper stockham","Diana DeGette","Raymon Anthony Doane"]
# votes = ["casper_votes","diana_votes","raymon_votes"]
# # zip up values together as dictonary
# dict_candidates_and_votes = dict(zip(candidates,votes))

# key = max(dict_candidates_and_votes ,  key = dict_candidates_and_votes.get)

casper_percent = round(((casper_votes/total_votes) * 100),3)
diana_percent = round( ( (diana_votes/ total_votes) * 100),3)
raymon_percent = round(( (raymon_votes/total_votes ) * 100),3)

#output data 
#print("Winner :",winner)
#print("Winner :",winner)
Analysis1 = "Election Results\n--------------------\nTotal Votes:{}\n----------------------------------------\nCharles Casper Stockham : {}% ({})\n Diana DeGette :{}% ({})\nRaymon Anthony Doane: {}% ({})\n----------------------------\nWinner:{}\n -------------- ".format(total_votes,casper_percent,casper_votes,diana_percent,diana_votes,raymon_percent,raymon_votes,winner)
print(Analysis1)           
print(f"Election Results")
print("------------------------------------------------------")
print("Total Votes:",total_votes)
print("------------------------------------------------------")
print(f"Charles Casper Stockham : {casper_percent:.3f}% ({casper_votes})")
print(f"Diana DeGette : {diana_percent:.3f}% ({diana_votes})")
print(f"Raymon Anthony Doane: {raymon_percent:.3f}% ({raymon_votes})")
print("------------------------------------------------------------")
print("Winner :",winner)
print("--------------------------------------------------------------")

# output to file

file2= open("pypol.txt","w")
file2.writelines(Analysis1)
file2.close()




