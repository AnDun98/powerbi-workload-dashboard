import pandas as pd
import numpy as np

np.random.seed(42)

dates = pd.date_range(start="2026-01-01", end="2026-12-31")

employees = pd.DataFrame({
    "employee_id": [f"E{i:03}" for i in range(1, 11)],
    "employee_name": ["Ivanov", "Petrov", "Sidorov", "Kuznetsova", "Smirnov",
                      "Volkov", "Fedorov", "Lebedev", "Morozov", "Pavlov"],
    "unit": ["Process", "Mechanical", "Process", "Planning", "Logistic",
                   "Mechanical", "Process", "Planning", "Logistic", "Process"],
    "department": ["Engineering", "Engineering", "Engineering", "Engineering", "Procurement",
                   "Engineering", "Engineering", "Engineering", "Procurement", "Engineering"],
    "roles": ["Engineer", "Senior Engineer", "Planner", "Manager", "Engineer",
              "Engineer", "Senior Engineer", "Planner", "Manager", "Engineer"],
    "fte": np.random.choice([0.5, 0.75, 0.9, 1.0], 10)
})

projects = pd.DataFrame({
    "project_id": ["P001", "P002", "P003"],
    "project_name": ["Gas Plant", "Compressor", "Refinery"]
})

data = []

for date in dates:
    for _, emp in employees.iterrows():
        project = np.random.choice(projects["project_id"])

        capacity = 8 * emp["fte"]

        planned = np.random.uniform(0, capacity)
        actual = max(0, planned + np.random.uniform(-2, 2))

        data.append([
            emp["employee_id"],
            project,
            date,
            round(planned, 2),
            round(actual, 2),
            capacity
        ])

df = pd.DataFrame(data, columns=[
    "employee_id", "project_id", "date", "planned_hours", "actual_hours", "capacity"])

df.merge(employees, on="employee_id", how="left")

employees.to_csv("employees.csv", index=False)
projects.to_csv("projects.csv", index=False)
df.to_csv("dataset.csv", index=False)
