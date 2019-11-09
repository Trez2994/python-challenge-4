import os

import csv

csvpath = os.path.join(os.getcwd()+'\\PyPoll', 'Resources', 'election_data.csv')

with open(csvpath, newline='') as csvfile:

    #CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    total_votes = 0
    candidates_list = []

    for row in csvreader:
        #print(row)
        total_votes = total_votes + 1
        candidates_list.append(row[2])
    
    for i in range(len(candidates_list)): 
        print(candidates_list[i])
    
    print(total_votes)
    #print(candiates_list)