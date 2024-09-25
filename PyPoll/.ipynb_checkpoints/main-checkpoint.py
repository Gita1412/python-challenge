import os
import csv

# Set the file path
csvpath = os.path.join('Resources', 'election_data.csv')

#open file for reading
with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csv_reader)
    print(f"Header: {csv_header}")


    # Initialize variables
    total_votes = 0
    candidates = {}
    winner = ""


    for row in csv_reader: 
        ballot_id = row[0]
        county = row[1]
        candidate = row[2]

        # Count total votes
        total_votes += 1  

         # Count votes for each candidate
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1



    # Calculate the winner
    winner = max(candidates, key=candidates.get)

# Print results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Export results to a text file
output_path = os.path.join('analysis', 'election_results.txt')
with open(output_path, 'w') as f:
    f.write("Election Results\n")
    f.write("-------------------------\n")
    f.write(f"Total Votes: {total_votes}\n")
    f.write("-------------------------\n")
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        f.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    f.write("-------------------------\n")
    f.write(f"Winner: {winner}\n")
    f.write("-------------------------\n")