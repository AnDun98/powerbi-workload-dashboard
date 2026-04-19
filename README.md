# 📊 Workload & Resource Utilization Dashboard

# 📌 Overview
This project demonstrates building an interactive Power BI dashboard for workload analytics.

The dashboard combines **planned and actual working hours** from different systems to provide full visibility into employee workload, capacity usage and resource efficiency.

---

## 🎯 Business Problem
EPC companies face challenge in managing workforce allocation:

- lack of visibility into actual vs planned workload
- employee overloading or underutilization
- inefficient resource distributionacross projects
- difficulty identifying bottlenecks in organizational units

This dashboard addresses these issues by providing **centralized analytics for resource management**.

---

## ⚙️ Data Sources
The solution integrates two main data streams:

 ### 1. Planned Data
 - Planned working hours per employee
 - Project allocation
 - Expected workload

### 2. Actual Data
- Timesheets (actual hours worked)
- Real execution data

---

## 🛢️ Data Model
The dashboard is built on a structured data model including:

- **Employees** (with unit, job title, FTE)
- **Projects**
- **Planned Allocation**
- **Actual Timesheets**

Supports hierarchical analysis:

Project ⭢ Unit ⭢ Employee

---

## 📊 Key Metrics

### Workload & Performance
- Planned Mhrs (by selected month & cumulative)
- Spent Mhrs (by selected month & cumulative)
- Variance (Spent vs Planned) (by selected month & cumulative)
- Utilization %

### Capacity Management
- Capacity (based on FTE)
- Allocation %

### Efficiency
- Idle Mhrs
- Idle %

<img height="130" alt="image" src="https://github.com/user-attachments/assets/6f20920e-61c0-4b08-9209-4eb9c54af66d" />

---

## 🧠 Calculations
**Utilization**
= Spent Mhrs / Capacity

**Allocation**
= Planned Mhrs / Capacity

**Delta Mhrs**
= Spent Mhrs - Planned Mhrs

**Idle Mhrs**
= MAX(0, Capacity - Spent Mhrs)

---

## 📈 Dashboard Features
### ♟️ KPI Overview
- Total workload indicators
- Utilization and Idle rates
- High-level performance metrics

---

### 📉 Trend Analysis
- Planned vs Actual workload over time
- Workload deviations
- Resource demand dynamics

<img height="200" alt="image" src="https://github.com/user-attachments/assets/05e57e91-0553-4ddb-ae93-0d468a75e6a3" />

---

### 🖇️ Organizational Analysis
- Workload breakdown by Unit
  <img height="200" alt="image" src="https://github.com/user-attachments/assets/75f44c53-2905-4b8b-9762-fa0d4dbb5e7a" />

- Employee-level analysis
  <img height="200" alt="image" src="https://github.com/user-attachments/assets/bfcd4155-90a4-458d-b974-938fd342a066" />

- Drill-down capabilities
- Tooltips with Employee by Project details
  <img height="200" alt="image" src="https://github.com/user-attachments/assets/76542462-1754-4d81-9d79-371b1ae67099" />

---

### 🌡️ Heatmap Visualization
- Quick identification of idle petterns

---

## 🎛️ Filters
The dashboard supports flexible filtering by:

- Project
- Unit
- Date

---

## ✔️ Business Value
This solution enables:

- proactive workload management
- improved workforce planning
- reduced idle capacity
- better resource allocation across Projects
- increased operational efficiency
- data-driven decision making in Head of Department

---

## 🛠️ Tech Stack
- Power BI
- Python (data preparation & simulation)

---

## 📥 Project Structure

workload-dashboard/

|

|-- data/        # source & prepared datasets

|-- scripts/     # data generation & transformation logic

|-- dashboard/   # pbix file

|-- README.md
