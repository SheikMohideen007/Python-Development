# Problem Statement:

# A data engineering team maintains a student performance tracker. A backend engineer is asked to write a Python function that processes a list of student dictionaries, filters out any student whose name should be excluded, assigns a rank value to each remaining student starting from 1, and returns a new list of dictionaries containing only the name and rank for students who passed (score ≥ 50).

# Constraints & Requirements:

# Use a for loop to iterate over the input list.
# Use continue to skip any student whose name appears in the exclude_names list.
# Use break to stop processing once a student with score exactly 0 is encountered (indicating a corrupted record sentinel).
# Build a result list of dictionaries. Each result dictionary must have exactly two keys: "name" and "rank". Only include students whose "score" is ≥ 50.
# The rank counter increments only for students who are NOT excluded (regardless of whether they pass or fail). Students who are excluded do not consume a rank.
# Return the result list from the function.
# Do not use any external libraries; use only built-in Python.
# Inlined Sample Data & Inputs (required if Q11 references data, files, schemas, logs, or API payloads):

# Input schema: each element in students is a dictionary with keys "name" (str) and "score" (int).

# Sample input shown to the student (verbatim):
students = [
    {"name": "Venki",    "score": 95},
    {"name": "Karthik",  "score": 72},
    {"name": "Harini",   "score": 45},
    {"name": "Abishek",  "score": 88},
    {"name": "Vicky",    "score": 60},
    {"name": "Rinky",    "score":  0},
    {"name": "Surya",    "score": 55},
]

exclude_names = ["Harini"]
# Expected output for the sample above:
# [
#     {"name": "Venki",   "rank": 1},
#     {"name": "Karthik", "rank": 2},
#     {"name": "Abishek", "rank": 3},
#     {"name": "Vicky",   "rank": 4},
# ]

def rank_students(students, exclude_names:list):
    rank_list=[]
    for student in students:
        if(exclude_names.__contains__(student['name'])):
            continue
        if(student['score']==0):
            break
        if(student['score']>=50):
           rank_list.append({'name':student['name'],'rank':len(rank_list)+1})

    return rank_list


print(rank_students(students=students,exclude_names=exclude_names))        
