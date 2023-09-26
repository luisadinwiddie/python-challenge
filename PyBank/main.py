#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 20:50:24 2023

@author: luisabarros
"""


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
