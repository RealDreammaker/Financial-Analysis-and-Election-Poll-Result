import os
import csv

fileinputpath = os.path.join(".","Resources","budget_data.csv")
totalmonths = 0
nettotal = 0 
changeprofitlost =[]
greatestinscreaseprofit = 0 
greatestdecreaseprofit = 0 
lastprofitlost = 0

with open(fileinputpath,"r") as csvfileinput:
    filecontent = csv.reader(csvfileinput)
    header = next(csvfileinput)
    for row in filecontent:
        currentamount = int(row[1])
        totalmonths += 1
        nettotal += currentamount
        if totalmonths > 1:
            currentchange = currentamount- lastprofitlost
            changeprofitlost.append(currentchange)
        lastprofitlost=currentamount
        
        if greatestinscreaseprofit < currentchange:
            greatestinscreaseprofit = currentchange
            greatprofitmonth = row[0]
            
        if greatestdecreaseprofit > currentchange:
            greatestdecreaseprofit = currentchange
            greatlostmonth = row[0]

totalchange = 0

for change in changeprofitlost:
    totalchange += change  

averagechange = totalchange / (totalmonths -1)
        
fileoutputpath = os.path.join (".","Analysis","PerformanceSummary.txt")

with open(fileoutputpath,"w") as outputfile:
    outputcontent = csv.writer(outputfile)
    outputcontent.writerow(["Financial Analysis"])
    outputcontent.writerow(["----------------------------"])
    outputcontent.writerow(["Total Months: "+ str(totalmonths)])
    outputcontent.writerow(["Total: $" + str(nettotal)])
    outputcontent.writerow(["Average  Change: $ "+ str(round(averagechange,2))])
    outputcontent.writerow(["Greatest Increase in Profits: "+ greatprofitmonth + " ($" + str(greatestinscreaseprofit) + ")"])
    outputcontent.writerow(["Greatest Decrease in Profits: "+ greatlostmonth + " ($" + str(greatestdecreaseprofit) + ")"])
    