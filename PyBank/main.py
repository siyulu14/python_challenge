import os
import csv

# Path to collect data from the Resources folder
csv_path = os.path.join("Resources/budget_data.csv")

# initial variables
months = 0
total_pl = 0
greatest_inc_amount = 0
greatest_dec_amount = 0

# open and read csv file
with open(csv_path, newline = "") as csvfile:
    
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # skip the header
    next(csvreader)

    # loop in budget_data
    for row in csvreader:
        
        # count months and toal profit/losses
        months = months + 1
        total_pl = total_pl + float(row[1])

        # compare the amount
        if float(row[1]) > 0 and float(row[1]) > greatest_inc_amount:
            greatest_inc_amount = float(row[1])
            greatest_inc_date = row[0]

        elif float(row[1]) < 0 and float(row[1]) < greatest_dec_amount:
            greatest_dec_amount = float(row[1])
            greatest_dec_date = row[0]
                

    average_pl = total_pl / months

    # show the results
    print("Financial Analysis")
    print("--------------------------")
    print(f"Total Months: {months}")
    print(f"Total: {total_pl}")
    print(f"Average Change: ${average_pl}")
    print(f"Greatest Increase in Profits: {greatest_inc_date} (${greatest_inc_amount})")
    print(f"Greatest Decrease in Profits: {greatest_dec_date} (${greatest_dec_amount})")
    






