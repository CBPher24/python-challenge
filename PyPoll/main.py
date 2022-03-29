#import modules and data needed
import os
import csv
csvpath = os.path.relpath("PyPoll/Resources/election_data.csv")

#variables needed
tot_votes = 0
#running list of candidates
candid = {}
#tot_votes for each candidate
#percentage of total votes for candidate
n = 0

#open and start read on csv
with open(csvpath) as csvfile:
    elect = csv.reader(csvfile, delimiter=',')
    next(elect)
    #loop to run through data
    for row in elect:
    #running count of votes
        tot_votes = tot_votes + 1
        #check to see if same candidate
        if row[2] != candid.values()[n]:
            candid.setdefault(row[2], []).append(row[2])
        #running count of votes for candidate



#print statement for terminal
#print("Election Results\n------------------------")
#print(f"Total Votes: {tot_votes}\n------------------------")
#all canidates, percentage of votes, and total votes for canidate
#name: percentage% (total votes)

#print("------------------------")
#canidate with the most votes aka Winner
#print(f"Winner: {}")

#print("------------------------")

#export data to txt file