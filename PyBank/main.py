import os
import csv
import statistics


monthCount = 0
total = 0
avgChange = 0
changeList = []
previous = 0
increase = ''
decrease = ''
greatestIncrease = 0
greatestDecrease = 0
firstLoop = True

# open csv in separate folder
# for each row:
#   add 1 to monthCount
#   add rows p/l to total
#   find average of changes(?)
#   check if row is the greatest inc/dec of profit
# then display data as shown in example
# export text file containing the data

csvpath = os.path.join('Resources','budget_data.csv')



with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        monthCount += 1
        total += int(row[1])
        if firstLoop == False:
            changeList.append(int(row[1])-previous)
        else:
            firstLoop = False

        if greatestIncrease < int(row[1])-previous:
            increase = row[0]
            greatestIncrease = int(row[1])-previous

        if greatestDecrease > int(row[1])-previous:
            decrease = row[0]
            greatestDecrease = int(row[1])-previous
        
        previous = int(row[1])
    avgChange = round(statistics.mean(changeList),2)    

    print("")
    print("Finanical Analysis")
    print("----------------------------")
    print(f"Total Months: {monthCount}")
    print(f"Total: ${total}")
    print(f"Average Change: ${avgChange}")
    print(f"Greatest Increase in Profits: {increase} (${greatestIncrease})")
    print(f"Greatest Decrease in Profits: {decrease} (${greatestDecrease})")





with open(os.path.join("Analysis", "PyBank_Analysis.txt"), "w") as file1:
    file1.write("\n")
    file1.write("Finanical Analysis\n")
    file1.write("----------------------------\n")
    file1.write(f"Total Months: {monthCount}\n")
    file1.write(f"Total: ${total}\n")
    file1.write(f"Average Change: ${avgChange}\n")
    file1.write(f"Greatest Increase in Profits: {increase} (${greatestIncrease})\n")
    file1.write(f"Greatest Decrease in Profits: {decrease} (${greatestDecrease})\n")
    file1.close