# Problem Statement:

# A data operations engineer at a logistics company needs to build a Python utility that processes a roster of delivery drivers stored as a list of tuples. Each tuple holds a driver's name and their completed delivery count for the week. The engineer must write a function process_roster(roster) that performs the following operations and returns a summary dictionary:

# Convert each tuple in roster to a list (to allow mutation), append the string "active" as a status tag to each inner list, then convert each inner list back to a tuple.
# From the resulting list of updated tuples, extract only the driver names (first element of each tuple) into a new list called names.
# Sort names alphabetically in place (ascending order).
# Count how many drivers have completed more than 50 deliveries (use the second element of the original tuples).
# Return a dictionary with three keys: "updated_roster" (the list of updated tuples from step 1), "sorted_names" (the sorted names list from step 3), and "high_performers" (the integer count from step 4).
# Constraints & Requirements:

# Use only Python built-in features — no external libraries.
# Use .append() to add the status tag in step 1.
# Use .sort() (in-place) for step 3.
# The original roster parameter must not be mutated — work on a copy.
# Handle an empty list input gracefully (return the dictionary with empty/zero values).
# Inlined Sample Data & Inputs:

# Sample input shown to the student (verbatim):
sample_roster = [
    ("Chen Wei", 63),
    ("Maria Santos", 45),
    ("Carlos Mendes", 78),
    ("Fatima Al-Amin", 50),
    ("Kofi Mensah", 91),
    ("Lena Fischer", 30),
    ("Takeshi Yamamoto", 55),
]




def process_roster(sample_roster):
    #Step 1
    updated_roster = []
    for driver in sample_roster:
        driver_list = list(driver) 
        driver_list.append("active") 
        updated_roster.append(tuple(driver_list))  

    #Step 2
    driver_names=[]
    high_performers=0
    for roster in updated_roster:
        driver_names.append(roster[0])
        high_performers = high_performers + 1 if roster[1] > 50 else high_performers
    
    #Step 3
    driver_names.sort()
            
    
    return {
        'updated_roster': updated_roster,
        'sorted_names': driver_names,
        'high_performers': high_performers
    }

print(process_roster(sample_roster))


list=[1,2,2,3,2]
list2=[2]
list.append(list2)
list.remove(2)

print(list)
