# Problem Statement:

# A data analyst at a logistics company receives a NumPy-based student grades dataset. The analyst must use NumPy to compute per-subject and per-student averages using axis-based aggregation, apply boolean masking to identify high-performing students, and reshape the grades array into a different layout. Using the inlined sample data below, write a complete Python script that performs all five steps described in the requirements.

# Constraints & Requirements:

# Use NumPy only — import as import numpy as np. Do not use Pandas.
# Do not use any Python for loops for steps 2–4; use NumPy vectorised operations throughout.
# Use np.mean with the appropriate axis parameter for steps 2 and 3.
# The boolean mask in step 4 must be derived from the per-student averages computed in step 3.
# The reshape in step 5 must use .reshape(2, 6) explicitly.

# Steps required:

# Create the 2D NumPy grades array from the sample data below.
# Compute the per-subject average (one value per column, across all students) using axis=0.
# Compute the per-student average (one value per row, across all subjects) using axis=1.
# Apply a boolean mask to filter and return only the rows (students) whose average score is >= 80.
# Reshape the original grades array from shape (4, 3) to shape (2, 6) and print the result.
# Inlined Sample Data & Inputs:

# The grades array represents 4 students (rows) and 3 subjects — Maths, Science, English (columns):

# student_id | Maths | Science | English
# -----------|-------|---------|--------
# S1         |  80   |   90    |   85
# S2         |  95   |   85    |   82
# S3         |  60   |   70    |   65
# S4         |  88   |   92    |   79
# As a NumPy array literal:

# grades = np.array([
#     [80, 90, 85],   # S1: Maths, Science, English
#     [95, 85, 82],   # S2
#     [60, 70, 65],   # S3
#     [88, 92, 79]    # S4
# ])
# # shape: (4, 3)
# Expected outputs for this sample:
# Per-subject averages (axis=0): [80.75, 84.25, 77.75] (Maths avg, Science avg, English avg)
# Per-student averages (axis=1): [85.0, 87.33..., 65.0, 86.33...]
# Students with average >= 80 (rows for S1, S2, S4): [[80, 90, 85], [95, 85, 82], [88, 92, 79]]
# Reshaped (2, 6) array: first row [80, 90, 85, 95, 85, 82], second row [60, 70, 65, 88, 92, 79]

import numpy as np

grades = np.array([
    [80, 90, 85],   # S1: Maths, Science, English
    [95, 85, 82],   # S2
    [60, 70, 65],   # S3
    [88, 92, 79]    # S4
])

per_subject_avg = np.mean(grades, axis=0)

print('Per-Subject averages (axis=0):', per_subject_avg)

per_student_avg= np.mean(grades,axis=1)
print(type(per_student_avg))
print('Per-Student averages (axis=1):', per_student_avg)

student_average=grades[per_student_avg>=80]

print('Student average greater than 80 is: ',student_average)


print('Shape of the Current original array is : ',grades.shape)
reshaped_array=grades.reshape(2,6)
print('After reshape the original array is : ',reshaped_array)