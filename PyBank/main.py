#import csv/data needed


#Initial Variables set
num_of_months = 0
net_total = 0
curr_month = 0
prev_month = 0
change = curr_month - prev_month
total_change = 0.00
avg_change = change / num_of_months
grtst_inc = 0
grtst_inc_date = " "
grtst_dec = 0
grtst_dec_date = " "

#initialize curr_month

#loop to go through the csv file

    #add up months

    #running tab of net total

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
