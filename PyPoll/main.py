#import modules and data needed
import os
import csv
import sys
csvpath = os.path.relpath("PyPoll/Resources/election_data.csv")
analysis = os.path.relpath("PyPoll/Analysis/analysis.txt")

#variables needed
tot_votes = 0
#running dict of candidates
candid = {}
prev_high = 0
#define function to do each canidate calc
def result(name):
    ballots = candid[name]
    perc = round(( ballots / tot_votes ) * 100, 3)
    a.write(f"{name}: {perc}% ({ballots})\n")

#open and start read on csv
with open(csvpath) as csvfile:
    elect = csv.reader(csvfile, delimiter=',')
    next(elect)
    #loop to run through data
    for row in elect:
    #running count of votes
        tot_votes = tot_votes + 1
        person = row[2]
        #check to see if same candidate
        if person not in candid:
            candid[person] = 1   
        else:
            candid[person] = candid[person] + 1
       
#running loop check for winner
for names in list(candid.keys()):
    count = candid[names]
    if count > prev_high:
        prev_high = count
        winner = names

#saving the analysis to file
a = open(analysis, "w")

a.write("Election Results\n------------------------\n")
a.write(f"Total Votes: {tot_votes}\n------------------------\n")
for x in list(candid.keys()):
    result(x)
a.write("------------------------\n")
a.write(f"Winner: {winner}\n")
a.write("------------------------\n")
a.close()

#reading file for terminal output
a = open(analysis, "r")
print(a.read())
