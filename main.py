
import pandas as pd
import numpy as np
import functions as fn


df = pd.read_csv('students.csv')
print("--- Initial Student Data ---")
print(df.head())


subjects = ['Math', 'Physics', 'CS']


df['Total_Marks'] = np.sum(df[subjects], axis=1)
df['Average_Marks'] = np.mean(df[subjects], axis=1)


grades = []
status = []
for avg in df['Average_Marks']:
    grades.append(fn.assign_grade(avg))
    status.append(fn.check_pass_fail(avg))

df['Grade'] = grades
df['Status'] = status


print("\n--- Performance Analysis ---")


class_avg = np.mean(df['Average_Marks'])
print(f"Overall Class Average: {class_avg:.2f}")


highest_avg = np.max(df['Average_Marks'])
lowest_avg = np.min(df['Average_Marks'])
print(f"Highest Average: {highest_avg:.2f} | Lowest Average: {lowest_avg:.2f}")


print("\n--- Subject-wise Averages ---")
for sub in subjects:
    sub_avg = np.mean(df[sub])
    print(f"{sub} Average: {sub_avg:.2f}")


pass_count = len(df[df['Status'] == 'Pass'])
fail_count = len(df[df['Status'] == 'Fail'])
print(f"\nTotal Passed: {pass_count} | Total Failed: {fail_count}")


top_student = df[df['Average_Marks'] == highest_avg]
print("\n Top Performer(s) ")
print(top_student[['Name', 'Department', 'Total_Marks', 'Average_Marks', 'Grade']])


df.to_csv('processed_students.csv', index=False)