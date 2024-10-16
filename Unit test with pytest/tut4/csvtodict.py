import csv
import json

# Read the CSV file
csv_file = 'results.csv'  # Replace with the path to your CSV file
json_file = 'student_result.json'  # Output JSON file

# Open the CSV file and read its contents
with open(csv_file, mode='r') as file:
    # Using DictReader to read rows as dictionaries
    csv_reader = csv.DictReader(file)
    
    # Convert the CSV data into a list of dictionaries
    data = [row for row in csv_reader]

# Write the JSON data to a file
with open(json_file, mode='w') as file:
    json.dump(data, file, indent=4)

print("CSV data has been successfully converted to JSON!")
