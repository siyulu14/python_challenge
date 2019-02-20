import os
import csv

# Path to collect data from the Resources folder
csv_path = os.path.join("Resources/election_data.csv")

# initial variables
total_votes = 0
# list candidates
cdt_1 = "Khan"
cdt_2 = "Correy"
cdt_3 = "Li"
cdt_4 = "O'Tooley"

cdt_1_cnt = 0
cdt_2_cnt = 0
cdt_3_cnt = 0
cdt_4_cnt = 0

# open and read csv file
with open(csv_path, newline = "") as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # skip the header
    next(csvreader)

    # loop in election_data
    for row in csvreader:

        # count total votes
        total_votes = total_votes + 1

        # count each candidate's votes
        if row[2] == cdt_1:
            cdt_1_cnt = cdt_1_cnt + 1
            
        elif row[2] == cdt_2:
            cdt_2_cnt = cdt_2_cnt +1

        elif row[2] == cdt_3:
            cdt_3_cnt = cdt_3_cnt + 1

        else:
            cdt_4_cnt = cdt_4_cnt + 1

# calculate the percentage of votes each candidate won
cdt_1_pct = cdt_1_cnt/total_votes * 100
cdt_2_pct = cdt_2_cnt/total_votes * 100
cdt_3_pct = cdt_3_cnt/total_votes * 100
cdt_4_pct = cdt_4_cnt/total_votes * 100

# find the winner
x = max(cdt_1_cnt, cdt_2_cnt, cdt_3_cnt, cdt_4_cnt)

if x == cdt_1_cnt:
    winner = cdt_1
elif x == cdt_2_cnt:
    winner = cdt_2
elif x == cdt_3_cnt:
    winner = cdt_3
else:
    winner = cdt_4

# print out
print("Election Results")
print("----------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------")
print(f"Khan: {cdt_1_pct}% ({cdt_1_cnt})")
print(f"Correy: {cdt_2_pct}% ({cdt_2_cnt})")
print(f"Li: {cdt_3_pct}% ({cdt_3_cnt})")
print(f"O'Tooley: {cdt_4_pct}% ({cdt_4_cnt})")
print("----------------------------")
print(f"Winner: {winner}")
print("----------------------------")




