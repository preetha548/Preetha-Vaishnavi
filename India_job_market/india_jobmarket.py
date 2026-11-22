
import os
import pandas as pd
import matplotlib.pyplot as plt

print("Starting India Job Market Analysis...")

# ==========================================
# 1. LOAD DATASET
# ==========================================

try:
    df = pd.read_csv("analyzed_job_dataset.csv")
    print("\nDataset loaded successfully!")

except FileNotFoundError:
    print("ERROR: job_dataset.csv not found!")
    raise SystemExit

# ==========================================
# 2. VALIDATE DATASET
# ==========================================

required_columns = [
    "Job ID", "Job Title", "Company Name", "Job Location",
    "Job Type", "Salary Range", "Experience Required",
    "Posted Date", "Application Deadline", "Job Portal",
    "Number of Applicants", "Education Requirement",
    "Skills Required", "Remote/Onsite", "Company Size"
]

missing = [c for c in required_columns if c not in df.columns]

if missing:
    print("Missing columns:", missing)
    raise SystemExit

# ==========================================
# 3. DATA PREPROCESSING
# ==========================================

df["Number of Applicants"] = pd.to_numeric(
    df["Number of Applicants"], errors="coerce"
)

df["Posted Date"] = pd.to_datetime(
    df["Posted Date"], errors="coerce"
)

df["Application Deadline"] = pd.to_datetime(
    df["Application Deadline"], errors="coerce"
)

df["Deadline Days"] = (
    df["Application Deadline"] - df["Posted Date"]
).dt.days

df["Posted Month"] = df["Posted Date"].dt.strftime("%Y-%m")
df["Posted Weekday"] = df["Posted Date"].dt.day_name()
df["Deadline Month"] = df["Application Deadline"].dt.strftime("%Y-%m")

# Create output folder
os.makedirs("job_market_charts", exist_ok=True)

chart_count = 0

# ==========================================
# 4. CHART HELPER FUNCTIONS
# ==========================================

def save_chart(filename):
    global chart_count

    plt.tight_layout()
    plt.savefig(
        os.path.join("job_market_charts", filename),
        dpi=150,
        bbox_inches="tight"
    )
    plt.close()

    chart_count += 1
    print(f"Chart {chart_count}/30 saved: {filename}")


def bar_chart(series, title, xlabel, ylabel, filename,
              horizontal=False):

    if series.empty:
        print("Skipping empty chart:", title)
        return

    plt.figure(figsize=(10, 6))

    if horizontal:
        series.sort_values().plot(kind="barh")
    else:
        series.plot(kind="bar")

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=40)

    save_chart(filename)


def pie_chart(series, title, filename):

    series = series[series > 0]

    if series.empty:
        return

    plt.figure(figsize=(8, 8))
    series.plot(
        kind="pie",
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title(title)
    plt.ylabel("")

    save_chart(filename)


def stacked_chart(data, title, xlabel, ylabel, filename):

    if data.empty:
        return

    plt.figure(figsize=(11, 6))
    data.plot(kind="bar", stacked=True, figsize=(11, 6))

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=40)

    save_chart(filename)


# ==========================================
# 5. DATASET INFORMATION
# ==========================================

print("\n========== DATASET INFORMATION ==========")

print("Total Jobs:", len(df))
print("Total Companies:", df["Company Name"].nunique())
print("Total Job Titles:", df["Job Title"].nunique())
print("Total Locations:", df["Job Location"].nunique())

print("\nDataset Shape:", df.shape)

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

print("\n========== JOB TYPE COUNT ==========")
print(df["Job Type"].value_counts())

print("\n========== WORK MODE ==========")
print(df["Remote/Onsite"].value_counts())

print("\n========== TOP 10 COMPANIES ==========")
print(df["Company Name"].value_counts().head(10))

print("\n========== TOP 10 LOCATIONS ==========")
print(df["Job Location"].value_counts().head(10))

print("\n========== TOP 10 APPLICANT JOBS ==========")
print(
    df.nlargest(10, "Number of Applicants")[
        ["Job Title", "Company Name", "Number of Applicants"]
    ].to_string(index=False)
)

# ==========================================
# 6. CHART 1 - JOB TYPE DISTRIBUTION
# ==========================================

bar_chart(
    df["Job Type"].value_counts(),
    "Job Type Distribution",
    "Job Type", "Number of Jobs",
    "01_job_type.png"
)

# ==========================================
# 7. CHART 2 - WORK MODE DISTRIBUTION
# ==========================================

pie_chart(
    df["Remote/Onsite"].value_counts(),
    "Remote, Hybrid and Onsite Jobs",
    "02_work_mode.png"
)

# ==========================================
# 8. CHART 3 - COMPANY SIZE DISTRIBUTION
# ==========================================

pie_chart(
    df["Company Size"].value_counts(),
    "Company Size Distribution",
    "03_company_size.png"
)

# ==========================================
# 9. CHART 4 - EDUCATION REQUIREMENTS
# ==========================================

bar_chart(
    df["Education Requirement"].value_counts(),
    "Education Requirements",
    "Education", "Number of Jobs",
    "04_education.png"
)

# ==========================================
# 10. CHART 5 - JOB PORTAL DISTRIBUTION
# ==========================================

bar_chart(
    df["Job Portal"].value_counts(),
    "Job Portal Distribution",
    "Job Portal", "Number of Jobs",
    "05_job_portals.png"
)

# ==========================================
# 11. CHART 6 - TOP 15 COMPANIES
# ==========================================

bar_chart(
    df["Company Name"].value_counts().head(15),
    "Top 15 Companies by Job Listings",
    "Company", "Number of Jobs",
    "06_top_companies.png",
    horizontal=True
)

# ==========================================
# 12. CHART 7 - TOP 15 JOB LOCATIONS
# ==========================================

bar_chart(
    df["Job Location"].value_counts().head(15),
    "Top 15 Job Locations",
    "Location", "Number of Jobs",
    "07_top_locations.png",
    horizontal=True
)

# ==========================================
# 13. CHART 8 - TOP JOB TITLES
# ==========================================

bar_chart(
    df["Job Title"].value_counts().head(15),
    "Top 15 Job Titles",
    "Job Title", "Number of Jobs",
    "08_top_job_titles.png",
    horizontal=True
)

# ==========================================
# 14. CHART 9 - SALARY RANGE DISTRIBUTION
# ==========================================

bar_chart(
    df["Salary Range"].value_counts(),
    "Salary Range Distribution",
    "Salary Range", "Number of Jobs",
    "09_salary_range.png"
)

# ==========================================
# 15. CHART 10 - EXPERIENCE REQUIREMENTS
# ==========================================

bar_chart(
    df["Experience Required"].value_counts(),
    "Experience Requirements",
    "Experience", "Number of Jobs",
    "10_experience.png"
)

# ==========================================
# 16. CHART 11 - APPLICANT HISTOGRAM
# ==========================================

plt.figure(figsize=(10, 6))

df["Number of Applicants"].dropna().plot(
    kind="hist", bins=20
)

plt.title("Distribution of Job Applicants")
plt.xlabel("Number of Applicants")
plt.ylabel("Frequency")

save_chart("11_applicant_histogram.png")

# ==========================================
# 17. CHART 12 - APPLICANT BOXPLOT
# ==========================================

plt.figure(figsize=(8, 6))

df["Number of Applicants"].dropna().plot(
    kind="box"
)

plt.title("Job Applicant Count Boxplot")
plt.ylabel("Number of Applicants")

save_chart("12_applicant_boxplot.png")

# ==========================================
# 18. CHART 13 - MONTHLY JOB POSTINGS
# ==========================================

monthly_jobs = df["Posted Month"].value_counts().sort_index()

bar_chart(
    monthly_jobs,
    "Monthly Job Postings",
    "Month", "Number of Jobs",
    "13_monthly_jobs.png"
)

# ==========================================
# 19. CHART 14 - MONTHLY DEADLINES
# ==========================================

deadline_months = (
    df["Deadline Month"].value_counts().sort_index()
)

bar_chart(
    deadline_months,
    "Monthly Application Deadlines",
    "Deadline Month", "Number of Jobs",
    "14_monthly_deadlines.png"
)

# ==========================================
# 20. CHART 15 - APPLICANTS BY JOB TYPE
# ==========================================

plt.figure(figsize=(10, 6))

df.boxplot(
    column="Number of Applicants",
    by="Job Type",
    rot=35
)

plt.title("Applicants by Job Type")
plt.suptitle("")
plt.xlabel("Job Type")
plt.ylabel("Number of Applicants")

save_chart("15_applicants_by_job_type.png")

# ==========================================
# 21. CHART 16 - APPLICANTS BY WORK MODE
# ==========================================

plt.figure(figsize=(9, 6))

df.boxplot(
    column="Number of Applicants",
    by="Remote/Onsite",
    rot=25
)

plt.title("Applicants by Work Mode")
plt.suptitle("")
plt.xlabel("Work Mode")
plt.ylabel("Number of Applicants")

save_chart("16_applicants_by_work_mode.png")

# ==========================================
# 22. CHART 17 - AVERAGE APPLICANTS BY COMPANY SIZE
# ==========================================

avg_applicants = df.groupby(
    "Company Size"
)["Number of Applicants"].mean()

bar_chart(
    avg_applicants,
    "Average Applicants by Company Size",
    "Company Size", "Average Applicants",
    "17_avg_applicants_company_size.png"
)

# ==========================================
# 23. CHART 18 - JOB TYPE VS WORK MODE
# ==========================================

cross1 = pd.crosstab(
    df["Job Type"], df["Remote/Onsite"]
)

stacked_chart(
    cross1,
    "Job Type vs Work Mode",
    "Job Type", "Number of Jobs",
    "18_jobtype_workmode.png"
)

# ==========================================
# 24. CHART 19 - JOB TYPE VS EDUCATION
# ==========================================

cross2 = pd.crosstab(
    df["Job Type"], df["Education Requirement"]
)

plt.figure(figsize=(10, 7))

plt.imshow(cross2, aspect="auto")
plt.colorbar(label="Number of Jobs")

plt.xticks(
    range(len(cross2.columns)),
    cross2.columns,
    rotation=45
)

plt.yticks(
    range(len(cross2.index)),
    cross2.index
)

plt.title("Job Type vs Education Heatmap")
plt.xlabel("Education")
plt.ylabel("Job Type")

save_chart("19_jobtype_education_heatmap.png")

# ==========================================
# 25. CHART 20 - COMPANY VS JOB TYPE
# ==========================================

top_company_names = df["Company Name"].value_counts().head(10).index

company_data = df[
    df["Company Name"].isin(top_company_names)
]

cross3 = pd.crosstab(
    company_data["Company Name"],
    company_data["Job Type"]
)

stacked_chart(
    cross3,
    "Top Companies vs Job Types",
    "Company", "Number of Jobs",
    "20_company_jobtype.png"
)

# ==========================================
# 26. CHART 21 - LOCATION VS WORK MODE
# ==========================================

top_locations = df["Job Location"].value_counts().head(10).index

location_data = df[
    df["Job Location"].isin(top_locations)
]

cross4 = pd.crosstab(
    location_data["Job Location"],
    location_data["Remote/Onsite"]
)

stacked_chart(
    cross4,
    "Top Locations vs Work Mode",
    "Location", "Number of Jobs",
    "21_location_workmode.png"
)

# ==========================================
# 27. CHART 22 - JOB PORTAL VS JOB TYPE
# ==========================================

cross5 = pd.crosstab(
    df["Job Portal"], df["Job Type"]
)

stacked_chart(
    cross5,
    "Job Portals vs Job Types",
    "Job Portal", "Number of Jobs",
    "22_portal_jobtype.png"
)

# ==========================================
# 28. CHART 23 - EDUCATION VS WORK MODE
# ==========================================

cross6 = pd.crosstab(
    df["Education Requirement"],
    df["Remote/Onsite"]
)

stacked_chart(
    cross6,
    "Education vs Work Mode",
    "Education", "Number of Jobs",
    "23_education_workmode.png"
)

# ==========================================
# 29. CHART 24 - COMPANY SIZE VS JOB TYPE
# ==========================================

cross7 = pd.crosstab(
    df["Company Size"], df["Job Type"]
)

stacked_chart(
    cross7,
    "Company Size vs Job Type",
    "Company Size", "Number of Jobs",
    "24_company_size_jobtype.png"
)

# ==========================================
# 30. CHART 25 - TOP REQUIRED SKILLS
# ==========================================

skills = (
    df["Skills Required"]
    .dropna()
    .str.split(",")
    .explode()
    .str.strip()
)

bar_chart(
    skills.value_counts().head(15),
    "Top 15 Required Skills",
    "Skills", "Number of Job Listings",
    "25_top_skills.png",
    horizontal=True
)

# ==========================================
# 31. CHART 26 - SKILLS VS JOB TYPE
# ==========================================

skill_data = df[["Skills Required", "Job Type"]].dropna().copy()

skill_data["Skills Required"] = (
    skill_data["Skills Required"].str.split(",")
)

skill_data = skill_data.explode("Skills Required")
skill_data["Skills Required"] = (
    skill_data["Skills Required"].str.strip()
)

top_skills = skills.value_counts().head(10).index

skill_data = skill_data[
    skill_data["Skills Required"].isin(top_skills)
]

cross8 = pd.crosstab(
    skill_data["Skills Required"],
    skill_data["Job Type"]
)

stacked_chart(
    cross8,
    "Top Skills vs Job Types",
    "Skills", "Number of Jobs",
    "26_skills_jobtype.png"
)

# ==========================================
# 32. CHART 27 - AVERAGE APPLICANTS BY JOB TITLE
# ==========================================

avg_job_applicants = (
    df.groupby("Job Title")["Number of Applicants"]
    .mean()
    .sort_values(ascending=False)
    .head(15)
)

bar_chart(
    avg_job_applicants,
    "Average Applicants by Job Title",
    "Job Title", "Average Applicants",
    "27_jobtitle_applicants.png",
    horizontal=True
)

# ==========================================
# 33. CHART 28 - APPLICANTS BY SALARY RANGE
# ==========================================

plt.figure(figsize=(11, 6))

df.boxplot(
    column="Number of Applicants",
    by="Salary Range",
    rot=35
)

plt.title("Applicants by Salary Range")
plt.suptitle("")
plt.xlabel("Salary Range")
plt.ylabel("Number of Applicants")

save_chart("28_applicants_salary.png")

# ==========================================
# 34. CHART 29 - JOB POSTINGS BY WEEKDAY
# ==========================================

weekday_order = [
    "Monday", "Tuesday", "Wednesday",
    "Thursday", "Friday", "Saturday", "Sunday"
]

weekday_counts = (
    df["Posted Weekday"]
    .value_counts()
    .reindex(weekday_order)
    .dropna()
)

bar_chart(
    weekday_counts,
    "Job Postings by Weekday",
    "Weekday", "Number of Jobs",
    "29_postings_weekday.png"
)

# ==========================================
# 35. CHART 30 - APPLICATION DEADLINE DAYS
# ==========================================

plt.figure(figsize=(10, 6))

df["Deadline Days"].dropna().plot(
    kind="hist", bins=15
)

plt.title("Distribution of Application Deadline Periods")
plt.xlabel("Days Between Posting and Deadline")
plt.ylabel("Number of Jobs")

save_chart("30_deadline_days.png")

# ==========================================
# 36. EXPORT RESULTS
# ==========================================

df.to_csv("analyzed_job_dataset.csv", index=False)

print("\n======================================")
print("INDIA JOB MARKET ANALYSIS COMPLETED!")
print("Total Records:", len(df))
print("Charts Generated:", chart_count)
print("Dataset Saved: analyzed_job_dataset.csv")
print("Charts Folder: job_market_charts")
print("======================================")
