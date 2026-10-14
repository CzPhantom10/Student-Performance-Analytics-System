# Student Performance Analytics System

A data analysis project built with **Python**, **NumPy**, and **Pandas** for analyzing student academic performance, grading, pass/fail status, and department-level cohort insights.

Developed for the **EWB Courses - Python with AI** assignment.

---

## Project Structure

```text
EWB PROJECT/
├── students.csv             # Dataset with 20 student records
├── functions.py             # Reusable data processing and analytical functions
├── main.py                  # Driver script executing the complete analytics pipeline
├── Project_Documentation.md # Detailed 10-section project report
├── README.md                # Project overview and run instructions
└── .gitignore               # Ignores __pycache__ and environment files
```

---

## Features

- **Pandas Data Management:** Ingestion and DataFrame structuring of student records across 4 academic departments.
- **NumPy Numerical Operations:** Vectorized calculations for totals, averages, standard deviations, and metric extremes.
- **Grading Engine:** Automatic assignment of letter grades (A+, A, B, C, D, F) based on average marks.
- **Multi-Factor Pass/Fail Logic:** Enforces both subject-level minimum scores (>= 40 in each subject) and attendance criteria (>= 75%).
- **Subject-Wise Benchmark Analysis:** Evaluates subject average, highest, lowest, and subject pass rates.
- **Top Performers Ranking:** Identifies and ranks top 5 rankers.
- **Department-Wise Performance:** Aggregates statistics grouped by academic department.
- **Visual Grade Distribution:** Terminal-based visual ASCII bar chart.

---

## Prerequisites & Installation

Ensure you have Python 3.8+ installed. Install the required libraries:

```bash
pip install numpy pandas
```

---

## Running the Project

From the project root directory, run:

```bash
python main.py
```

---

## Dataset Overview (`students.csv`)

The dataset contains 20 student records with the following attributes:
- `StudentID`: Unique student identifier (e.g. `STU001`)
- `Name`: Full student name
- `Department`: Academic branch (Computer Science, Information Technology, Electronics, Mechanical)
- `Math`, `Science`, `English`, `ComputerScience`: Marks scored out of 100
- `Attendance`: Attendance percentage

---

## Analytical Findings Summary

| Metric | Result |
| :--- | :--- |
| **Total Students** | 20 |
| **Overall Class Average** | 75.67% |
| **Top Scorer** | Rohan Verma (95.75%) |
| **Lowest Scorer** | Arjun Gupta (44.00%) |
| **Highest Scoring Subject** | Computer Science (77.70 marks) |
| **Passing Students** | 17 (85.0%) |
| **Failing Students** | 3 (15.0%) |

---
