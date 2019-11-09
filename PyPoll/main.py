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
    votes_khan = 0
    votes_correy = 0
    votes_li = 0
    votes_otooley = 0

    for row in csvreader:
        #print(row)
        total_votes = total_votes + 1
        candidates_list.append(row[2])
    
    for i in range(len(candidates_list)): 
        #print(candidates_list[i])
        if candidates_list[i] == "Khan":
            votes_khan = votes_khan + 1
        if candidates_list[i] == "Correy":
            votes_correy = votes_correy + 1
        if candidates_list[i] == "Li":
            votes_li = votes_li + 1
        if candidates_list[i] == "O'Tooley":
            votes_otooley = votes_otooley + 1

    percent_khan = round((votes_khan / total_votes) * 100)
    percent_correy = round((votes_correy / total_votes) * 100)
    percent_li = round((votes_li / total_votes) * 100)
    percent_otooley = round((votes_otooley / total_votes) * 100)

    if votes_khan > votes_correy:
        winner = "Khan"

        
    
    
    print("The total number of votes is",total_votes)
    print("The total number of votes for Khan is",votes_khan,"which is",percent_khan,"% of votes")
    print("The total number of votes for Correy is",votes_correy,"which is",percent_correy,"% of votes")
    print("The total number of votes for Li is",votes_li,"which is",percent_li,"% of votes")
    print("The total number of votes for O'Tooley is",votes_otooley,"which is",percent_otooley,"% of votes")
    print("The winner is",winner)

    #print(candiates_list)