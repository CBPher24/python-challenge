#import modules and data needed
import os
import csv
import sys
csvpath = os.path.relpath("PyBank/Resources/budget_data.csv")
analysis = os.path.relpath("PyBank/Analysis/analysis.txt")

#Initial Variables set
num_of_months = 0
net_total = 0
curr_month = 0
prev_month = 1088983
change = curr_month - prev_month
total_change = 0.00
grtst_inc = 0
grtst_inc_date = " "
grtst_dec = 0
grtst_dec_date = " "

#open and start read on csv
with open(csvpath) as csvfile:
    prof_loss = csv.reader(csvfile, delimiter=',')
    next(prof_loss)
    #loop to go through the csv file
    for row in prof_loss:
        #add up months
        num_of_months = num_of_months + 1
        #running tab of net total
        net_total = net_total + int(row[1])
        #initialize current month
        curr_month = int(row[1])
        #run change equation and add to total change
        change = curr_month - prev_month
        total_change = total_change + change
        #if statement off of change to find greatest increase and date
        if int(row[1]) > grtst_inc:
            grtst_inc = int(row[1])
            grtst_inc_date = row[0]
        #if statement off of change to find greates decrease and date
        if int(row[1]) < grtst_dec:
            grtst_dec = int(row[1])
            grtst_dec_date = row[0]
        #put current mont as previous
        prev_month = curr_month

#calculate the average of total change
avg_change = round(total_change / num_of_months, 2)

#print statement
print("Financial Analysis\n----------------------")
print(f"Total Months: {num_of_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${avg_change}")
print(f"Greatest Increase in Profits: {grtst_inc_date} (${grtst_inc})")
print(f"Greatest Decrease in Profits: {grtst_dec_date} (${grtst_dec})")

#export to text file
with open(analysis, "w") as save:
    sys.stdout = save
    print("Financial Analysis\n----------------------")
    print(f"Total Months: {num_of_months}")
    print(f"Total: ${net_total}")
    print(f"Average Change: ${avg_change}")
    print(f"Greatest Increase in Profits: {grtst_inc_date} (${grtst_inc})")
    print(f"Greatest Decrease in Profits: {grtst_dec_date} (${grtst_dec})")