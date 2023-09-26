#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 20:29:39 2023

@author: luisabarros
"""

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
