# Problem Statement:

# A backend engineer at a logistics company needs to build a student record management utility. 
# The utility must (1) write a fresh set of student records to a JSON file, 
# (2) append a system-event log entry to a plain text log file, and 
# (3) read the JSON file back into Python and print each student's name and score. 
# The entire solution must use Python's json module and proper file-handling patterns with with blocks.

# Constraints & Requirements:

# Use Python's json module (json.dump and json.load).
# Use with blocks for all file operations — no bare open() / close() calls.
# Write the student records to "records.json" using "w" mode.
# Append a log message to "events.log" using "a" mode.
# Read "records.json" back and print each student's name and score.
# The solution must work correctly on the inlined sample below.
# Inlined Sample Data & Inputs (required):

# Use the following student records as input to your solution:

students = [
    {"name": "Aryan", "score": 88},
    {"name": "Divya", "score": 74},
    {"name": "Keerthana", "score": 91},
    {"name": "Rajan", "score": 65},
    {"name": "Snehal", "score": 79},
]
log_message = "Records written successfully."
# Expected output when reading back from records.json:
# Aryan: 88
# Divya: 74
# Keerthana: 91
# Rajan: 65
# Snehal: 79
# Expected side-effect: "events.log" contains (at minimum, appended) the line Records written successfully.

import json


with open("records.json", "w") as json_file:
    json.dump(students, json_file)

with open("records.json","r") as json_file:
    data=json.load(json_file)
    for student in data:
        print(f"{student['name']}: {student['score']}")



with open("events.log", "a") as log_file:
    log_file.write(log_message + "\n")