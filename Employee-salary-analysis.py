import pandas as pd
import matplotlib.pyplot as plt

# Dataset
data = {
    "Employee": [
        "Amit", "Priya", "Rahul", "Neha",
        "Rohan", "Sneha", "Karan", "Pooja"
    ],
    "Department": [
        "HR", "IT", "Finance", "IT",
        "HR", "Finance", "IT", "Marketing"
    ],
    "Salary": [
        35000, 60000, 50000, 65000,
        40000, 55000, 70000, 45000
    ],
    "Experience": [
        2, 5, 4, 6,
        3, 5, 7, 2
    ],
    "Performance": [
        "Good", "Excellent", "Good", "Excellent",
        "Average", "Good", "Excellent", "Average"
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

print("Employee Salary Analysis")
print(df)

print("\nHead")
print(df.head())

print("\nTail")
print(df.tail())

print("\nInfo")
df.info()

print("\nDescribe")
print(df.describe())

# Highest Salary
Highest_Salary = df["Salary"].max()
print("\nHighest Salary:", Highest_Salary)

# Lowest Salary
Lowest_Salary = df["Salary"].min()
print("\nLowest Salary:", Lowest_Salary)

# Employee with Highest Salary
Highest_Salary_Employee = df.loc[df["Salary"].idxmax()]
print("\nEmployee with Highest Salary")
print(Highest_Salary_Employee)

# Employee with Lowest Salary
Lowest_Salary_Employee = df.loc[df["Salary"].idxmin()]
print("\nEmployee with Lowest Salary")
print(Lowest_Salary_Employee)

# Employees with Salary > 50000
High_Earners = df[df["Salary"] > 50000]
print("\nEmployees with Salary > 50000")
print(High_Earners)

# IT Department Employees
IT_Department = df[df["Department"] == "IT"]
print("\nIT Department Employees")
print(IT_Department)

# Employees with Experience > 4
High_Experienced = df[df["Experience"] > 4]
print("\nEmployees with Experience > 4")
print(High_Experienced)

# Department-wise Average Salary
Average_Salary = df.groupby("Department")["Salary"].mean()
print("\nDepartment Wise Average Salary")
print(Average_Salary)

# Department-wise Highest Salary
Highest_Department_Salary = df.groupby("Department")["Salary"].max()
print("\nDepartment Wise Highest Salary")
print(Highest_Department_Salary)

# Number of Employees in Each Department
Total_Employees = df["Department"].value_counts()
print("\nEmployees in Each Department")
print(Total_Employees)

# Bonus (10%)
df["Bonus"] = df["Salary"] * 0.10

# Total Salary
df["Total Salary"] = df["Salary"] + df["Bonus"]

# Sort by Total Salary
df = df.sort_values("Total Salary", ascending=False)

print("\nSorted Data")
print(df)

# Challenge Solution
High_Earners_Experienced = df[
    (df["Salary"] > 50000) &
    (df["Experience"] > 4)
]

print("\nEmployees with Salary > 50000 and Experience > 4")
print(High_Earners_Experienced)

# Graph 1
plt.bar(df["Employee"], df["Total Salary"])
plt.title("Employee vs Total Salary")
plt.xlabel("Employee")
plt.ylabel("Total Salary")
plt.show()

# Graph 2
plt.bar(Average_Salary.index, Average_Salary.values)
plt.title("Department Wise Average Salary")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.show()