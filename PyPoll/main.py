# This script is for PyPoll

# import dependencies
import os
import csv

# Open input file to read in data
file_path = os.path.join(".", "Resources","election_data.csv")

with open(file_path,"r") as input_file:
    content = csv.reader(input_file)
    
    # skip the header 
    header = next(content)
    
    # setting up variables
    total_votes =  0
    candidates = {}
    
    # looping through file content
    for row in content:
        
        # count the total vote
        total_votes += 1
        
        # if candidate is not yet in the dictionary, set count to 0
        if row[2] not in candidates:
            candidates[row[2]] = 0
            
        # count the total vote for the current candidate
        candidates[row[2]] += 1

dashes = "-------------------------" 

# define a function to print out result nicely - justified margin
def print_justify(text, variable):        
    length = len(dashes)
    gap = length - len(text) - len(str(variable))
    return text + (" " * gap) + str(variable)

# Writing result to a resuable list
result = []
result.append("Election Results")
result.append(dashes)
result.append(print_justify("Total Votes: ",total_votes))
result.append(dashes)

# calculate percentage votes for each candidate
for name in candidates:
    candidate_votes = candidates[name]
    percentage_votes = candidate_votes / total_votes * 100
    result.append(print_justify(name + ": " , f"%.3f%% (%d)" %(percentage_votes , candidate_votes)))

result.append(dashes)

# setting up variables
highest_vote = 0
winner = ""

# loop through each candidate to determine the candidate with highest votes
for name in candidates:
    if candidates[name] > highest_vote:
        highest_vote = candidates[name]
        winner = name       
result.append(print_justify("Winner: ", winner))
result.append(dashes)
# writing result ended

# print out result 
for item in result:
    print(item)
              
# writing result to output file        
file_path = os.path.join(".", "Analysis","election_result.txt")
    
with open(file_path,"w") as output_file:
    content = csv.writer(output_file)
    for item in result:
        content.writerow([item])
    