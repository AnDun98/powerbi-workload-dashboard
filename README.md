# powerbi-workload-dashboard
# 📊 Workload & Resource Utilization Dashboard

# 📌 Overview
This project demonstrates building an interactive Power BI dashboard for workload analytics.

The dashboard combines **planned and actual working hours** from different systems to provide full vid=sibility intoemployee workload, capacity usage and resource efficiency.

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
- Timesheets (spent hours worked)
- Real execution data

---

## 🛢️ Data Model
The dashboard is built on a structured data model including:

- **Employees** (with department, unit, role, FTE)
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

---

## 🧠 Calculations
**Utilization**
= Spent Mhrs / Capacity
