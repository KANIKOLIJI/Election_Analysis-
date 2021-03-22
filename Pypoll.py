#the data we need to retrieve
#1. the total number of votes cast
#2. a complete list of candidates who received votes
#3. The percentage of votes each candidate won 
#4. the total number of votes each candidate won
#5. the winner of election based on popular vote
# Assign a variable for the file to load and the path.
import csv
import os
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
# Open the election results and read the file.
total_votes = 0

candidate_options = []

candidate_votes = {}

winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data :
    #to do: read and analuze the data here
    file_reader = csv.reader(election_data)
    #print the header row
    headers = next(file_reader)
    
    #print each row in the scv file.
    for row in file_reader:
        #Add to the total vote count
        total_votes += 1

        candidate_name = row[2]
        if candidate_name not in candidate_options :
            candidate_options.append(candidate_name)

            candidate_votes [candidate_name] = 0

        candidate_votes [candidate_name]+= 1

with open(file_to_save, "w") as txt_file:
    Election_Results = (
    f"\nElection Results\n"
    f"----------------------\n"
    f"Total votes: {total_votes:,}\n"
    f"----------------------\n"
    )
    print(Election_Results, end="")
    txt_file.write(Election_Results)

    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (f"{candidate_name}: {vote_percentage: .1f}% ({votes: ,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    winning_candidate_summery = (
        f"----------------\n"
        f"winner: {winning_candidate}\n"
        f"winning vote count: {winning_count: ,}\n"
        f"winning percentage: {winning_percentage: .1f}%\n"
        f"----------------\n"
            )
    #print the total votes
    print(winning_candidate_summery)
    txt_file.write(winning_candidate_summery)       
    #with open(file_to_save, "w") as txt_file :
        #txt_file.write("Counties in the Election")
        #txt_file.write("----------------------")
        #txt_file.write("Arapahoe\nDenver\nJefferson") 
            
    # Close the file.
    election_data.close()


