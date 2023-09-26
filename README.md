Well. This one was a challenge. I could understand more the paypoll than paybank. I couldnt find the max value and mix value in PayBank, only the months that have the relationship. I tried my best. I believe that this one was less overwhelming than the VBA. But still a challege :) See you next time!
My code for PayPoll:
import csv
import os

# Define the file paths
file_to_load = os.path.join("Resources", "election_data.csv")
file_to_output = os.path.join("analysis", "election_analysis.txt")

# Initialize variables to keep track of election data
total_votes = 0
candidates = {}  # Dictionary to store candidate vote counts

# Read the CSV file and count the votes for each candidate
with open(file_to_load) as election_data:
  reader = csv.reader(election_data)
  header = next(reader)  # Skip the header row

# Loop through each row in the CSV
  for row in reader:
        total_votes += 1
        candidate_name = row[2]  # Get the candidate's name from the row

 # If the candidate is not in our dictionary, add them
        if candidate_name not in candidates:
            candidates[candidate_name] = 0

  # Increment the candidate's vote count
        candidates[candidate_name] += 1

# Determine the winning candidate
winning_candidate = max(candidates, key=candidates.get)
winning_count = candidates[winning_candidate]

# Generate the election results as a string
election_results = (
    f"\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n"
)

# Print and save the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(election_results)

# Loop through the candidates and calculate percentages
    for candidate, votes in candidates.items():
        vote_percentage = (votes / total_votes) * 100
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        txt_file.write(voter_output)

# Display the winning candidate
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n"
    )
    txt_file.write(winning_candidate_summary)

# Print the results to the terminal
print(election_results)
for candidate, votes in candidates.items():
    vote_percentage = (votes / total_votes) * 100
    voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})"
    print(voter_output)

print(winning_candidate_summary)

My code for PayBank:
# Importing libraries I might use
import csv
import statistics


# Telling python where the code is located.
filename =  "budget_data.csv"
resource_folder= "resources"

full_file_path = "./" + resource_folder + "/" + filename
# full_file_path = f"./{resource_folder}/{filename}"

opened_file = open(full_file_path, 'r')


# Using CSV< a fancy python library.
open_csv_library_file = csv.DictReader(opened_file)

#making lists
date_list = []
prof_loss_list = []
date_value_dict = {}
changes_list = []
# handle the values from the first row
first_row = next(open_csv_library_file)
prev_pl = int(first_row['Profit/Losses'])
prof_loss_list.append(prev_pl)
date_list.append(first_row['Date'])

# This is a dictionary, printing each row

for row in open_csv_library_file:
    date_list.append(row["Date"])
    current_pl = int(row['Profit/Losses'])
    prof_loss_list.append(current_pl)
    change = current_pl - prev_pl
    changes_list.append(change)
    prev_pl = current_pl

         
    date_value_dict[row["Date"]] = change


print(date_value_dict)
    
#the net total amount of "profit/losses" over the entire period
Total_amount_prof_loss = sum (prof_loss_list)


print( "Financial Analysis")
print("-----------------")

# The total number of months included in the dataset
total_months = len(date_list)
print(f"total months =  {total_months}")

# The net total amount of "Profit/Losses" over the entire period
total_proff_loss = sum(prof_loss_list)
print(f"total = {total_proff_loss}")

# The changes in "Profit/Losses" over the entire period, and then the average of those changes
average_prof_loss = statistics.mean(changes_list)
print(f"average change = {average_prof_loss}")


# The greatest increase in profits (date and amount) over the entire period
max_value = max(changes_list)
max_month = max (date_value_dict, key=date_value_dict.get)
print(max_month)

# The greatest decrease in profits (date and amount) over
min_value = min(date_value_dict)
min_month = min(date_value_dict, key=date_value_dict.get)
print(min_month)
