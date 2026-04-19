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

<img width="1020" height="387" alt="image" src="https://github.com/user-attachments/assets/50262512-3708-49a4-967d-c3fe98dde022" />

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
- high-level performance metrics

---

### 📉 Trend Analysis
- Planned vs Actual workload over time
- Workload deviations
- Resource demand dynamics

---

### 🖇️ Organizational Analysis
- Workload breakdown by Unit
- Employee-level analysis
- Drill-down capabilities
- Tooltips with Employee by Project details

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
