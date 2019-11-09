import os

import csv
NumberMonths = 0
ProfitLoss = []
maxprofit = []
minprofit = []


csvpath = os.path.join(os.getcwd()+'\\PyBank', 'Resources', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    sum = 0
    for row in csvreader:
        print(row)
        NumberMonths = NumberMonths + 1
        ProfitLoss.append(int(row[1]))
        sum = sum + int(row[1])
     



    avg = sum / len(ProfitLoss)
    min = min(ProfitLoss)
    max = max(ProfitLoss)

    






print(NumberMonths)
print("The total profit is :", sum)
print("The average profit is :", avg)
print("The lowest profit is :", min)
print("The greatest profit is :", max)
