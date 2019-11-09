import os

import csv
NumberMonths = 0
ProfitLoss = []
maxprofit = []
minprofit = []
month = []

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
        #print(row)
        NumberMonths = NumberMonths + 1
        ProfitLoss.append(int(row[1]))
        sum = sum + int(row[1])
        month.append(row[0])

    month_over_month = []
    for i in range(1,len(ProfitLoss)):
        monthly_change = ProfitLoss[i] - ProfitLoss[i-1]
        month_over_month.append([month[i], monthly_change])

    largest_increase = month_over_month[0][1]
    largest_increase_month = month_over_month[0][0]
    largest_decrease = month_over_month[0][1]
    largest_decrease_month = month_over_month[0][0]

    for j in range(len(month_over_month)):
        if month_over_month[j][1] > largest_increase:
            largest_increase = month_over_month[j][1]
            largest_increase_month = month_over_month[j][0]

        if month_over_month[j][1] < largest_decrease:
            largest_decrease = month_over_month[j][1]
            largest_decrease_month = month_over_month[j][0]

    avg = sum / NumberMonths
    
    print("The number of months is :", NumberMonths)
    print("The total profit is :", sum)
    print("The average profit is :", avg)
    print("The greatest profit is",largest_increase, largest_increase_month)
    print("The lowest profit is",largest_decrease, largest_decrease_month)


