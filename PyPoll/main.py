import os
import csv



# open csv in separate folder
# for each row:
#   check if unique candidate and if yes add to list
#   add vote to total votes cast
#   add vote to candidate
# Tally  votes and percentages for each candidate
# Declare winner
# export to txt file

candidates = []
voteList = []
voteCount = 0
results = {}



csvpath = os.path.join('Resources','election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        voteCount += 1
        voteList.append(row[2])
        if row[2] not in candidates:
            candidates.append(row[2])
    
    for candidate in candidates:
        results[candidate] = voteList.count(candidate) 

    winner = max(results, key=results.get) 




    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {voteCount}")
    print("-------------------------")
    for key, value in results.items():
        print(f"{key}: {format(value/voteCount,'.3%')} ({value})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

with open(os.path.join("Analysis", "PyPoll_Analysis.txt"), "w") as file1:
    file1.write("\n")
    file1.write("Election Results\n")
    file1.write("-------------------------\n")
    file1.write(f"Total Votes: {voteCount}\n")
    file1.write("-------------------------\n")
    for key, value in results.items():
        file1.write(f"{key}: {format(value/voteCount,'.3%')} ({value})\n")
    file1.write("-------------------------\n")
    file1.write(f"Winner: {winner}\n")
    file1.write("-------------------------\n")
    file1.close























# import pandas as pd

# data_file = "Resources/election_data.csv"

# data_file_df = pd.read_csv(data_file)


# unique = data_file_df["Candidate"].unique()
# print(unique)

# count = data_file_df[["Candidate","Khan"]].value_counts()
# print(count)