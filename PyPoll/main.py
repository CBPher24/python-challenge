#import modules and data needed
import os
import csv
csvpath = os.path.relpath("PyPoll/Resources/election_data.csv")

#variables needed
tot_votes = 0
#running dict of candidates
candid = {}
prev_high = 0
#define formule to do each canidate calc
def result(name):
    ballots = len(candid[name])
    perc = round(( ballots / tot_votes ) * 100, 3)
    print(f"{name}: {perc}% ({ballots})")
    
        





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
            candid[person] = row
        else:
            candid[person].append(row)
       
#running count of votes for candidate
for names in list(candid.keys()):
    count = len(candid[names])
    if count > prev_high:
        prev_high = count
        winner = names

# print(list(candid.keys()))
# print(len(candid["Raymon Anthony Doane"]))
#print statement for terminal
print("Election Results\n------------------------")
print(f"Total Votes: {tot_votes}\n------------------------")
#all canidates, percentage of votes, and total votes for canidate
#name: percentage% (total votes)
for x in list(candid.keys()):
    result(x)
print("------------------------")
#canidate with the most votes aka Winner
print(f"Winner: {winner}")

#print("------------------------")

#export data to txt file