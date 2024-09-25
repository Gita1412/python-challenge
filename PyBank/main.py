#dependencies
import os
import csv

#set the file path
csvpath = os.path.join('Resources', 'budget_data.csv')
csv_budget_data = csvpath

#open file for reading
with open(csv_budget_data) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')

    #skip the header row
    csv_header = next(csv_reader)
   

    #initial variables to track the financial data
    total_months = 0
    net_total = 0
    previous_profit_loss = None
    changes = []
    dates = []
    months = []
    greatest_increase = {"amount": float('-inf'), "date": ""}
    greatest_decrease = {"amount": float('inf'), "date": ""}

  

    for row in csv_reader: 
        date = row[0]
        profit_loss = int(row[1])
        print(row)
        
        #count total months
        total_months += 1

        #count net total
        net_total += profit_loss
        
        #calculate changes in "Profit/Losses"
        if previous_profit_loss is not None:
            change = profit_loss - previous_profit_loss
            changes.append(change)
            dates.append(date)

        # Check for greatest increase (month and amount)
            if change > greatest_increase["amount"]:
                greatest_increase["amount"] = change
                greatest_increase["date"] = date

      # Check for greatest decrease (month and amount)
            if change < greatest_decrease ["amount"]:
                greatest_decrease ["amount"] = change
                greatest_decrease ["date"] = date

        #store the current profit/loss for next
        previous_profit_loss = profit_loss

    

#calculate average across the months
average_change = sum(changes) / len(changes) if changes else 0


#print output summary
print("Financial Analysis")
print("-----------------------------------------")
print(f"Total Months: {total_months}")
print(f"Total:${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")
print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")

#export text file
import os
output_path = os.path.join('analysis', 'financial_analysis.txt')
with open(output_path, 'w') as f:
    f.write("Financial Analysis\n")
    f.write("----------------------------\n")
    f.write(f"Total Months: {total_months}\n")
    f.write(f"Total: ${net_total}\n")
    f.write(f"Average Change: ${average_change:.2f}")
    f.write(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n")
    f.write(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})\n")