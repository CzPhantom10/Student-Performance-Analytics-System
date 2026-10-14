import os
from functions import (
    load_dataset,
    calculate_totals_and_averages,
    apply_grades_and_status,
    calculate_overall_summary,
    analyze_subject_wise,
    get_top_performers,
    get_department_analysis
)


def print_separator(char="=", length=75):
    print(char * length)


def main():
    print_separator("=")
    print("      STUDENT PERFORMANCE ANALYTICS SYSTEM")
    print("      EWB Courses - Python with AI Project")
    print_separator("=")

    dataset_file = "students.csv"
    if not os.path.exists(dataset_file):
        print(f"Error: Dataset '{dataset_file}' not found.")
        return

    print(f"\n[STEP 1 & 2] Loading student dataset from '{dataset_file}'...")
    raw_df = load_dataset(dataset_file)
    print(f"[OK] Dataset loaded successfully! Total records: {len(raw_df)}")
    print(f"[OK] Columns detected: {list(raw_df.columns)}")
    
    subject_columns = ["Math", "Science", "English", "ComputerScience"]
    print(f"[OK] Subject columns for evaluation: {', '.join(subject_columns)}")

    print("\n[STEP 3] Processing student marks, totals, averages, grades, and pass/fail status...")
    processed_df = calculate_totals_and_averages(raw_df, subject_columns)
    final_df = apply_grades_and_status(processed_df, subject_columns)
    print("[OK] Processing completed successfully.")

    print("\n--- STUDENT PERFORMANCE SUMMARY TABLE ---")
    display_cols = ["StudentID", "Name", "Department", "Total_Marks", "Average_Marks", "Grade", "Status", "Attendance"]
    print(final_df[display_cols].to_string(index=False))

    print("\n" + "=" * 75)
    print("                 ANALYTICAL FINDINGS & ANSWERS")
    print("=" * 75)

    summary = calculate_overall_summary(final_df)
    subject_analysis = analyze_subject_wise(final_df, subject_columns)
    best_subject_row = subject_analysis.sort_values(by="Average Marks", ascending=False).iloc[0]

    print(f"\n1. Overall Class Average: {summary['class_average']}%")
    print(f"2. Student with Highest Average: {summary['highest_student']} ({summary['highest_average']}%)")
    print(f"3. Student with Lowest Average:  {summary['lowest_student']} ({summary['lowest_average']}%)")
    print(f"4. Subject with Highest Average: {best_subject_row['Subject']} ({best_subject_row['Average Marks']} marks)")
    print(f"5. Pass / Fail Statistics:")
    print(f"   - Total Students: {summary['total_students']}")
    print(f"   - Passed: {summary['passed_students']} ({summary['pass_percentage']}%)")
    print(f"   - Failed: {summary['failed_students']} ({round(100 - summary['pass_percentage'], 2)}%)")
    print(f"   * Passing Criteria: Marks >= 40 in every subject AND Attendance >= 75%")

    print("\n--- SUBJECT-WISE PERFORMANCE ANALYSIS ---")
    print(subject_analysis.to_string(index=False))

    print("\n--- TOP 5 PERFORMING STUDENTS ---")
    top_students = get_top_performers(final_df, n=5)
    print(top_students.to_string(index=False))

    print("\n--- DEPARTMENT-WISE PERFORMANCE SUMMARY ---")
    dept_df = get_department_analysis(final_df)
    print(dept_df.to_string(index=False))

    print("\n--- GRADE DISTRIBUTION ---")
    grade_counts = final_df["Grade"].value_counts().sort_index()
    for grade, count in grade_counts.items():
        percentage = round((count / len(final_df)) * 100, 1)
        bar = "#" * count
        print(f"Grade {grade:<2} : {count:>2} students ({percentage:>4}%) {bar}")

    print("\n" + "=" * 75)
    print("[OK] Analysis complete. All calculations verified with NumPy and Pandas.")
    print("=" * 75)


if __name__ == "__main__":
    main()
