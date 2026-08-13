"""Clean and analyse a sample student-score dataset.

The script saves three charts in the charts folder beside this file.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


PROJECT_FOLDER = Path(__file__).parent
DATA_FILE = PROJECT_FOLDER / "student_scores.csv"
CHARTS_FOLDER = PROJECT_FOLDER / "charts"


def assign_grade(score):
    """Return a letter grade for a numeric score."""
    if score >= 90:
        return "A"
    if score >= 75:
        return "B"
    if score >= 60:
        return "C"
    return "D"


def load_and_clean_data():
    """Load the CSV and replace missing scores with the subject average."""
    data = pd.read_csv(DATA_FILE)
    data["score"] = data["score"].fillna(data.groupby("subject")["score"].transform("mean"))
    data["score"] = data["score"].round(1)
    data["grade"] = data["score"].apply(assign_grade)
    return data


def create_charts(data):
    """Create bar, line, and pie charts from the cleaned dataset."""
    CHARTS_FOLDER.mkdir(exist_ok=True)
    subject_averages = data.groupby("subject")["score"].mean().sort_values(ascending=False)

    plt.figure(figsize=(8, 5))
    subject_averages.plot(kind="bar", color="#4C78A8")
    plt.title("Average Score by Subject")
    plt.ylabel("Average score")
    plt.ylim(0, 100)
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(CHARTS_FOLDER / "average_scores_bar.png")
    plt.close()

    plt.figure(figsize=(8, 5))
    for student, student_data in data.groupby("student"):
        plt.plot(student_data["subject"], student_data["score"], marker="o", label=student)
    plt.title("Student Scores Across Subjects")
    plt.ylabel("Score")
    plt.ylim(0, 100)
    plt.legend(title="Student")
    plt.tight_layout()
    plt.savefig(CHARTS_FOLDER / "student_scores_line.png")
    plt.close()

    grade_counts = data["grade"].value_counts().reindex(["A", "B", "C", "D"], fill_value=0)
    plt.figure(figsize=(6, 6))
    plt.pie(grade_counts, labels=grade_counts.index, autopct="%1.1f%%", startangle=90)
    plt.title("Grade Distribution")
    plt.tight_layout()
    plt.savefig(CHARTS_FOLDER / "grade_distribution_pie.png")
    plt.close()


def main():
    data = load_and_clean_data()
    create_charts(data)

    print("=== Student Score Analysis ===")
    print(f"Records analysed: {len(data)}")
    print(f"Overall average: {np.mean(data['score']):.2f}")
    print("\nAverage score by subject:")
    print(data.groupby("subject")["score"].mean().round(2))
    print("\nCleaned data:")
    print(data.to_string(index=False))
    print(f"\nCharts saved in: {CHARTS_FOLDER}")


if __name__ == "__main__":
    main()
