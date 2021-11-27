# This script is for PyBank

# Import dependencies
import os
import csv

fileinputpath = os.path.join(".","Resources","budget_data.csv")

# Declaring variables for analysis
totalmonths = 0
totalchange = 0
nettotal = 0 
change_PL =[]
greatest_inscrease_profit = 0 
greatest_decrease_profit = 0 
last_month_PL = 0

with open(fileinputpath,"r") as csv_input:
    filecontent = csv.reader(csv_input)
    
    # skip header because there's no header row
    header = next(csv_input)
    
    # loop through the file content to get data
    for row in filecontent:
        current_amount = int(row[1])
        
        # adding up net profit and counting months for the whole period
        totalmonths += 1
        nettotal += current_amount
        
        # get changes in profit from second month and add to a list (first month has no data available to compare )
        if totalmonths > 1:
            current_change = current_amount - last_month_PL
            change_PL.append(current_change)
                 
            # set current change in profit as a new greatest increase in profit if it is higher and remember the current month 
            if greatest_inscrease_profit < current_change:
                greatest_inscrease_profit = current_change
                best_month = row[0]

             # set current change in profit as a new greatest decrease in profit if it is lower and remember the current month 
            if greatest_decrease_profit > current_change:
                greatest_decrease_profit = current_change
                worst_month = row[0]
                
        # remember last month change of profit
        last_month_PL=current_amount                    
        
        
# add up changes in profit
for change in change_PL:
    totalchange += change  
  
average_change = totalchange / (totalmonths - 1)

dashes = "----------------------------"
# define a function to print out result nicely - justified margin
def print_justify(text, variable):        
    length = len(dashes)
    gap = length - len(text) - len(str(variable))
    return text + (" " * gap) + str(variable)


# assign result ouput to a list
result = [] 
result.append("Financial Analysis")
result.append(dashes)
result.append(print_justify("Total Months: ", totalmonths))
result.append(print_justify("Total: " ,  "$" + str(nettotal)))
result.append(print_justify("Average  Change:", "$" + str(round(average_change,2))))
result.append("Greatest Increase in Profits: "+ best_month + " ($" + str(greatest_inscrease_profit) + ")")
result.append("Greatest Decrease in Profits: "+ worst_month + " ($" + str(greatest_decrease_profit) + ")")

# print result to screen
for item in result:
    print(item)

# writing result to output file
fileoutputpath = os.path.join (".","Analysis","PerformanceSummary.txt")
with open(fileoutputpath,"w") as outputfile:
    outputcontent = csv.writer(outputfile)
    for item in result:
        outputcontent.writerow([item])
