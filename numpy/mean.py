import numpy as np

# Rows: Students, Columns: [Math, Science, English]
grade_matrix = np.array([
    [80, 90, 85], # Student 1
    [95, 85, 92], # Student 2
    [60, 70, 65]  # Student 3
])

# Column averages (Average performance score achieved per subject class)
subject_means = np.mean(grade_matrix, axis=0)
print("Subject Performance Averages (Math, Sci, Eng):", subject_means)

# Row averages (Overall  average grade earned per individual student)
student_means = np.mean(grade_matrix, axis=1)
print("Individual Student Grade Averages:", student_means)