import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(r"C:\Users\abhin\Desktop\python\Student Result Analyser\student.csv")

print("📊 Student Data:")
print(df)

# Calculate total & percentage
df["Total"] = df[["Math", "Science", "English", "History"]].sum(axis=1)
df["Percentage"] = np.round(df["Total"] / 4, 2)

# Find Topper
topper = df.loc[df["Percentage"].idxmax()]

print("\n🏆 Class Topper:", topper["Name"], "with", topper["Percentage"], "%")

# Pass/Fail Analysis (>=40% = Pass)
df["Result"] = np.where(df["Percentage"] >= 40, "Pass", "Fail")

# Subject-wise average
subject_avg = df[["Math", "Science", "English", "History"]].mean()

print("\n📈 Subject Averages:")
print(subject_avg)

# 🔹 Visualization

# Bar chart: Student Percentage
plt.figure(figsize=(10,6))
plt.bar(df["Name"], df["Percentage"], color="skyblue")
plt.title("Student Percentage Comparison")
plt.xlabel("Students")
plt.ylabel("Percentage")
plt.show()

# Pie chart: Pass vs Fail
plt.figure(figsize=(6,6))
df["Result"].value_counts().plot.pie(autopct="%1.1f%%", colors=["lightgreen","salmon"])
plt.title("Pass vs Fail Distribution")
plt.show()

# Line graph: Subject Average
plt.figure(figsize=(8,5))
plt.plot(subject_avg.index, subject_avg.values, marker="o", color="purple")
plt.title("Average Marks in Each Subject")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.show()
