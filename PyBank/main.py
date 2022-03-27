#import modules and data needed
import os
import csv
csvpath = os.path.relpath("PyBank/Resources/budget_data.csv")


#Initial Variables set
num_of_months = 0
net_total = 0
curr_month = 0
prev_month = 0
change = curr_month - prev_month
total_change = 0.00
#avg_change = change / num_of_months
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
    
    total_change = total_change + change
    
    #if statement off of change to find greatest increase and date

    #if statement off of change to find greates decrease and date

#calculate the average of total change

#print statement
print("Financial Analysis\n----------------------")
print(f"Total Months: {num_of_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${avg_change}")
print(f"Greatest Increase in Profits: {grtst_inc_date} \(${grtst_inc}\)")
print(f"Greatest Decrease in Profits: {grtst_dec_date} \(${grtst_dec}\)")


#export to text file
