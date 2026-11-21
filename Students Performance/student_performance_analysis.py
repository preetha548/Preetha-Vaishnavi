
import os
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------------------
# STUDENT PERFORMANCE ANALYSIS
# -----------------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "StudentsPerformance.csv")
CHART_DIR = os.path.join(BASE_DIR, "Student_Charts")

os.makedirs(CHART_DIR, exist_ok=True)


def save_chart(filename):
    """Save the current chart in the output folder."""
    plt.tight_layout()
    plt.savefig(os.path.join(CHART_DIR, filename), dpi=300)
    plt.close()


def main():
    print("\n======================================")
    print("     STUDENT PERFORMANCE ANALYSIS")
    print("======================================")

    # Check whether the CSV file exists
    if not os.path.exists(DATA_FILE):
        print("\nERROR: StudentsPerformance.csv was not found.")
        print("Save the CSV file in the same folder as this Python file.")
        return

    # Load dataset
    df = pd.read_csv(DATA_FILE)

    # Clean column names
    df.columns = df.columns.str.strip()

    required_columns = [
        "gender",
        "race/ethnicity",
        "parental level of education",
        "lunch",
        "test preparation course",
        "math score",
        "reading score",
        "writing score"
    ]

    missing = [col for col in required_columns if col not in df.columns]

    if missing:
        print("Missing columns:", missing)
        return

    # Convert subject scores into numeric values
    score_columns = ["math score", "reading score", "writing score"]

    for col in score_columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Remove incomplete records and invalid scores
    df = df.dropna(subset=required_columns)
    df = df[
        df[score_columns].ge(0).all(axis=1)
        & df[score_columns].le(100).all(axis=1)
    ].copy()

    if df.empty:
        print("No valid student records found.")
        return

    # -----------------------------------------
    # DATA PROCESSING
    # -----------------------------------------

    df["total score"] = df[score_columns].sum(axis=1)
    df["average score"] = df[score_columns].mean(axis=1).round(2)

    def performance_level(score):
        if score >= 80:
            return "Excellent"
        elif score >= 60:
            return "Good"
        elif score >= 40:
            return "Average"
        else:
            return "Needs Improvement"

    df["performance level"] = df["average score"].apply(
        performance_level
    )

    # Save processed results
    result_file = os.path.join(
        BASE_DIR, "student_performance_results.csv"
    )
    df.to_csv(result_file, index=False)

    # -----------------------------------------
    # BASIC DATASET INFORMATION
    # -----------------------------------------

    print("\n1. DATASET INFORMATION")
    print("--------------------------------------")
    print("Total students:", len(df))
    print("Total columns:", len(df.columns))
    print("Missing values:", df.isnull().sum().sum())

    print("\n2. SUBJECT SCORE SUMMARY")
    print("--------------------------------------")
    print(df[score_columns].describe().round(2))

    print("\n3. SUBJECT AVERAGES")
    print("--------------------------------------")
    print(df[score_columns].mean().round(2))

    print("\n4. PERFORMANCE LEVEL")
    print("--------------------------------------")
    print(df["performance level"].value_counts())

    print("\n5. GENDER DISTRIBUTION")
    print("--------------------------------------")
    print(df["gender"].value_counts())

    print("\n6. TEST PREPARATION ANALYSIS")
    print("--------------------------------------")
    print(
        df.groupby("test preparation course")[
            score_columns
        ].mean().round(2)
    )

    print("\n7. PARENTAL EDUCATION ANALYSIS")
    print("--------------------------------------")
    print(
        df.groupby("parental level of education")[
            score_columns
        ].mean().round(2)
    )

    # -----------------------------------------
    # CHART 1: GENDER DISTRIBUTION
    # -----------------------------------------

    df["gender"].value_counts().plot(
        kind="bar",
        title="Student Gender Distribution",
        xlabel="Gender",
        ylabel="Number of Students"
    )
    plt.xticks(rotation=0)
    save_chart("gender_distribution.png")

    # -----------------------------------------
    # CHART 2: SUBJECT AVERAGES
    # -----------------------------------------

    averages = df[score_columns].mean()

    averages.plot(
        kind="bar",
        title="Average Marks by Subject",
        xlabel="Subject",
        ylabel="Average Score"
    )
    plt.xticks(
        [0, 1, 2],
        ["Mathematics", "Reading", "Writing"],
        rotation=0
    )
    save_chart("subject_average.png")

    # -----------------------------------------
    # CHART 3: MATHEMATICS DISTRIBUTION
    # -----------------------------------------

    plt.hist(df["math score"], bins=15, edgecolor="black")
    plt.title("Mathematics Score Distribution")
    plt.xlabel("Mathematics Score")
    plt.ylabel("Number of Students")
    save_chart("math_score_distribution.png")

    # -----------------------------------------
    # CHART 4: READING DISTRIBUTION
    # -----------------------------------------

    plt.hist(df["reading score"], bins=15, edgecolor="black")
    plt.title("Reading Score Distribution")
    plt.xlabel("Reading Score")
    plt.ylabel("Number of Students")
    save_chart("reading_score_distribution.png")

    # -----------------------------------------
    # CHART 5: WRITING DISTRIBUTION
    # -----------------------------------------

    plt.hist(df["writing score"], bins=15, edgecolor="black")
    plt.title("Writing Score Distribution")
    plt.xlabel("Writing Score")
    plt.ylabel("Number of Students")
    save_chart("writing_score_distribution.png")

    # -----------------------------------------
    # CHART 6: PERFORMANCE LEVEL
    # -----------------------------------------

    df["performance level"].value_counts().reindex(
        ["Excellent", "Good", "Average", "Needs Improvement"],
        fill_value=0
    ).plot(
        kind="bar",
        title="Overall Student Performance",
        xlabel="Performance Level",
        ylabel="Number of Students"
    )

    plt.xticks(rotation=20)
    save_chart("performance_level.png")

    # -----------------------------------------
    # CHART 7: TEST PREPARATION
    # -----------------------------------------

    df.groupby("test preparation course")[
        score_columns
    ].mean().plot(
        kind="bar",
        title="Test Preparation vs Subject Scores",
        xlabel="Test Preparation",
        ylabel="Average Score"
    )

    plt.xticks(rotation=0)
    plt.legend(
        ["Mathematics", "Reading", "Writing"]
    )
    save_chart("test_preparation.png")

    # -----------------------------------------
    # CHART 8: LUNCH PERFORMANCE
    # -----------------------------------------

    df.groupby("lunch")["average score"].mean().plot(
        kind="bar",
        title="Average Performance by Lunch Type",
        xlabel="Lunch Type",
        ylabel="Average Score"
    )

    plt.xticks(rotation=0)
    save_chart("lunch_performance.png")

    # -----------------------------------------
    # CHART 9: PARENTAL EDUCATION
    # -----------------------------------------

    df.groupby("parental level of education")[
        "average score"
    ].mean().sort_values().plot(
        kind="bar",
        title="Parental Education vs Student Performance",
        xlabel="Parental Education",
        ylabel="Average Score"
    )

    plt.xticks(rotation=35, ha="right")
    save_chart("parental_education.png")

    # -----------------------------------------
    # CHART 10: GENDER PERFORMANCE
    # -----------------------------------------

    df.groupby("gender")[score_columns].mean().plot(
        kind="bar",
        title="Subject Performance by Gender",
        xlabel="Gender",
        ylabel="Average Score"
    )

    plt.xticks(rotation=0)
    plt.legend(["Math", "Reading", "Writing"])
    save_chart("gender_performance.png")

    # -----------------------------------------
    # CHART 11: SCORE CORRELATION
    # -----------------------------------------

    correlation = df[score_columns].corr()

    plt.imshow(correlation, cmap="coolwarm", vmin=-1, vmax=1)
    plt.colorbar(label="Correlation")

    plt.xticks(
        range(3),
        ["Math", "Reading", "Writing"]
    )
    plt.yticks(
        range(3),
        ["Math", "Reading", "Writing"]
    )

    for i in range(3):
        for j in range(3):
            plt.text(
                j, i,
                f"{correlation.iloc[i, j]:.2f}",
                ha="center",
                va="center"
            )

    plt.title("Subject Score Correlation")
    save_chart("score_correlation.png")

    # -----------------------------------------
    # CHART 12: AVERAGE SCORE DISTRIBUTION
    # -----------------------------------------

    plt.hist(
        df["average score"],
        bins=15,
        edgecolor="black"
    )

    plt.title("Overall Average Score Distribution")
    plt.xlabel("Average Score")
    plt.ylabel("Number of Students")
    save_chart("average_score_distribution.png")

    # -----------------------------------------
    # FINAL RESULTS
    # -----------------------------------------

    top_student = df.loc[df["average score"].idxmax()]
    lowest_student = df.loc[df["average score"].idxmin()]

    print("\n8. TOP PERFORMANCE")
    print("--------------------------------------")
    print("Highest average score:", top_student["average score"])

    print("\n9. LOWEST PERFORMANCE")
    print("--------------------------------------")
    print("Lowest average score:", lowest_student["average score"])

    print("\n10. OVERALL ANALYSIS")
    print("--------------------------------------")
    print("Overall average:", round(df["average score"].mean(), 2))
    print("Highest subject average:", averages.idxmax())
    print("Lowest subject average:", averages.idxmin())

    print("\n======================================")
    print("       ANALYSIS COMPLETED!")
    print("======================================")
    print("Processed dataset:", result_file)
    print("Charts saved in:", CHART_DIR)
    print("Total charts generated: 12")


if __name__ == "__main__":
    main()
