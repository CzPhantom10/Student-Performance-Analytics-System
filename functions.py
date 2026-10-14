import numpy as np
import pandas as pd


def load_dataset(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    return df


def calculate_totals_and_averages(df: pd.DataFrame, subject_cols: list) -> pd.DataFrame:
    df_copy = df.copy()
    marks_matrix = df_copy[subject_cols].to_numpy()
    df_copy["Total_Marks"] = np.sum(marks_matrix, axis=1)
    df_copy["Average_Marks"] = np.round(np.mean(marks_matrix, axis=1), 2)
    return df_copy


def assign_grade(average_score: float) -> str:
    if average_score >= 90:
        return "A+"
    elif average_score >= 80:
        return "A"
    elif average_score >= 70:
        return "B"
    elif average_score >= 60:
        return "C"
    elif average_score >= 50:
        return "D"
    else:
        return "F"


def check_pass_fail(row: pd.Series, subject_cols: list, passing_mark: int = 40, min_attendance: int = 75) -> str:
    for subject in subject_cols:
        if row[subject] < passing_mark:
            return "Fail"
    
    if row["Attendance"] < min_attendance:
        return "Fail"
    
    return "Pass"


def apply_grades_and_status(df: pd.DataFrame, subject_cols: list) -> pd.DataFrame:
    grades = []
    statuses = []
    
    for _, row in df.iterrows():
        grade = assign_grade(row["Average_Marks"])
        status = check_pass_fail(row, subject_cols)
        grades.append(grade)
        statuses.append(status)
    
    df["Grade"] = grades
    df["Status"] = statuses
    return df


def calculate_overall_summary(df: pd.DataFrame) -> dict:
    averages = df["Average_Marks"].to_numpy()
    
    highest_avg = np.max(averages)
    lowest_avg = np.min(averages)
    class_avg = np.mean(averages)
    class_std = np.std(averages)
    
    top_student = df.loc[df["Average_Marks"] == highest_avg, "Name"].iloc[0]
    lowest_student = df.loc[df["Average_Marks"] == lowest_avg, "Name"].iloc[0]
    
    total_students = len(df)
    passed_count = int(np.sum(df["Status"] == "Pass"))
    failed_count = int(np.sum(df["Status"] == "Fail"))
    pass_percentage = (passed_count / total_students) * 100
    
    return {
        "total_students": total_students,
        "highest_average": round(float(highest_avg), 2),
        "highest_student": top_student,
        "lowest_average": round(float(lowest_avg), 2),
        "lowest_student": lowest_student,
        "class_average": round(float(class_avg), 2),
        "class_std_dev": round(float(class_std), 2),
        "passed_students": passed_count,
        "failed_students": failed_count,
        "pass_percentage": round(pass_percentage, 2),
    }


def analyze_subject_wise(df: pd.DataFrame, subject_cols: list, passing_mark: int = 40) -> pd.DataFrame:
    subject_stats = []
    
    for subject in subject_cols:
        marks = df[subject].to_numpy()
        avg_score = np.mean(marks)
        highest_score = np.max(marks)
        lowest_score = np.min(marks)
        passed_in_subject = np.sum(marks >= passing_mark)
        pass_rate = (passed_in_subject / len(marks)) * 100
        
        subject_stats.append({
            "Subject": subject,
            "Average Marks": round(float(avg_score), 2),
            "Highest Marks": int(highest_score),
            "Lowest Marks": int(lowest_score),
            "Pass Rate (%)": round(float(pass_rate), 2)
        })
        
    return pd.DataFrame(subject_stats)


def get_top_performers(df: pd.DataFrame, n: int = 5) -> pd.DataFrame:
    top_df = df.sort_values(by="Average_Marks", ascending=False).head(n).copy()
    top_df["Rank"] = np.arange(1, len(top_df) + 1)
    columns_order = ["Rank", "StudentID", "Name", "Department", "Total_Marks", "Average_Marks", "Grade"]
    return top_df[columns_order]


def get_department_analysis(df: pd.DataFrame) -> pd.DataFrame:
    dept_summary = df.groupby("Department").agg(
        Student_Count=("StudentID", "count"),
        Department_Average=("Average_Marks", "mean"),
        Average_Attendance=("Attendance", "mean")
    ).reset_index()
    
    dept_summary["Department_Average"] = dept_summary["Department_Average"].round(2)
    dept_summary["Average_Attendance"] = dept_summary["Average_Attendance"].round(2)
    return dept_summary.sort_values(by="Department_Average", ascending=False)
