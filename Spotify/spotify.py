
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# SPOTIFY MUSIC DATA ANALYSIS
# ==========================================

print("=" * 55)
print("       SPOTIFY MUSIC DATA ANALYSIS")
print("=" * 55)

# File paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "dataset.csv")
OUTPUT_DIR = os.path.join(BASE_DIR, "Spotify_Charts")

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Visualization style
sns.set_theme(style="whitegrid")

# ==========================================
# 1. LOAD DATASET
# ==========================================

df = pd.read_csv(DATA_FILE)

print("\nDataset Loaded Successfully!")

print("\nDataset Shape:", df.shape)

print("\nFirst 5 Records:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

# Remove unnecessary index column
if "Unnamed: 0" in df.columns:
    df.drop(columns=["Unnamed: 0"], inplace=True)

# Remove duplicate records
df.drop_duplicates(inplace=True)

# Remove records with missing essential values
df.dropna(
    subset=["track_name", "artists", "track_genre"],
    inplace=True
)

# ==========================================
# 2. POPULARITY DISTRIBUTION
# ==========================================

plt.figure(figsize=(10, 6))

sns.histplot(
    data=df,
    x="popularity",
    bins=30,
    kde=True
)

plt.title("Spotify Track Popularity Distribution")
plt.xlabel("Popularity Score")
plt.ylabel("Number of Tracks")

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "popularity_distribution.png"))
plt.show()

# ==========================================
# 3. TOP 15 MUSIC GENRES
# ==========================================

plt.figure(figsize=(12, 7))

top_genres = df["track_genre"].value_counts().head(15)

sns.barplot(
    x=top_genres.values,
    y=top_genres.index
)

plt.title("Top 15 Music Genres")
plt.xlabel("Number of Tracks")
plt.ylabel("Music Genre")

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "top_genres.png"))
plt.show()

# ==========================================
# 4. ENERGY DISTRIBUTION
# ==========================================

plt.figure(figsize=(10, 6))

sns.histplot(
    data=df,
    x="energy",
    bins=30,
    kde=True
)

plt.title("Spotify Music Energy Distribution")
plt.xlabel("Energy")
plt.ylabel("Frequency")

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "energy_distribution.png"))
plt.show()

# ==========================================
# 5. DANCEABILITY DISTRIBUTION
# ==========================================

plt.figure(figsize=(10, 6))

sns.histplot(
    data=df,
    x="danceability",
    bins=30,
    kde=True
)

plt.title("Music Danceability Distribution")
plt.xlabel("Danceability")
plt.ylabel("Frequency")

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "danceability_distribution.png"))
plt.show()

# ==========================================
# 6. EXPLICIT CONTENT DISTRIBUTION
# ==========================================

plt.figure(figsize=(8, 6))

explicit_counts = df["explicit"].value_counts()

plt.pie(
    explicit_counts,
    labels=["Non-Explicit" if x == False else "Explicit"
            for x in explicit_counts.index],
    autopct="%1.1f%%",
    startangle=90,
    shadow=True
)

plt.title("Explicit vs Non-Explicit Songs")

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "explicit_distribution.png"))
plt.show()

# ==========================================
# 7. SONG DURATION DISTRIBUTION
# ==========================================

df["duration_minutes"] = df["duration_ms"] / 60000

plt.figure(figsize=(10, 6))

sns.histplot(
    data=df,
    x="duration_minutes",
    bins=30,
    kde=True
)

plt.title("Spotify Song Duration Distribution")
plt.xlabel("Duration (Minutes)")
plt.ylabel("Number of Songs")

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "duration_distribution.png"))
plt.show()

# ==========================================
# 8. ENERGY VS DANCEABILITY
# ==========================================

sample_df = df.sample(
    n=min(5000, len(df)),
    random_state=42
)

plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=sample_df,
    x="energy",
    y="danceability",
    hue="explicit",
    alpha=0.6
)

plt.title("Energy vs Danceability")
plt.xlabel("Energy")
plt.ylabel("Danceability")

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "energy_vs_danceability.png"))
plt.show()

# ==========================================
# 9. AVERAGE POPULARITY BY GENRE
# ==========================================

genre_popularity = (
    df.groupby("track_genre")["popularity"]
    .mean()
    .sort_values(ascending=False)
    .head(15)
)

plt.figure(figsize=(12, 7))

sns.barplot(
    x=genre_popularity.values,
    y=genre_popularity.index
)

plt.title("Top 15 Genres by Average Popularity")
plt.xlabel("Average Popularity")
plt.ylabel("Music Genre")

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "popularity_by_genre.png"))
plt.show()

# ==========================================
# 10. VALENCE VS ENERGY
# ==========================================

plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=sample_df,
    x="valence",
    y="energy",
    alpha=0.5
)

plt.title("Music Positivity vs Energy")
plt.xlabel("Valence")
plt.ylabel("Energy")

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "valence_vs_energy.png"))
plt.show()

# ==========================================
# 11. CORRELATION HEATMAP
# ==========================================

numeric_df = df.select_dtypes(include=np.number)

plt.figure(figsize=(13, 9))

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    linewidths=0.5
)

plt.title("Spotify Music Correlation Heatmap")

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "correlation_heatmap.png"))
plt.show()

# ==========================================
# 12. COMBINED DASHBOARD
# ==========================================

fig, axes = plt.subplots(2, 2, figsize=(16, 11))

# Popularity
sns.histplot(
    data=df,
    x="popularity",
    bins=25,
    ax=axes[0, 0]
)

axes[0, 0].set_title("Popularity Distribution")

# Energy
sns.histplot(
    data=df,
    x="energy",
    bins=25,
    ax=axes[0, 1]
)

axes[0, 1].set_title("Energy Distribution")

# Top genres
sns.barplot(
    x=top_genres.values,
    y=top_genres.index,
    ax=axes[1, 0]
)

axes[1, 0].set_title("Top 15 Genres")

# Danceability vs Energy
sns.scatterplot(
    data=sample_df,
    x="danceability",
    y="energy",
    ax=axes[1, 1]
)

axes[1, 1].set_title("Danceability vs Energy")

plt.suptitle(
    "SPOTIFY MUSIC ANALYSIS DASHBOARD",
    fontsize=18,
    fontweight="bold"
)

plt.tight_layout()

plt.savefig(
    os.path.join(OUTPUT_DIR, "spotify_dashboard.png"),
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# ==========================================
# 13. FINAL ANALYSIS REPORT
# ==========================================

print("\n" + "=" * 55)
print("           SPOTIFY ANALYSIS REPORT")
print("=" * 55)

print("\nTotal Songs:", len(df))

print("Total Music Genres:", df["track_genre"].nunique())

print("Total Artists:", df["artists"].nunique())

print("Average Popularity:",
      round(df["popularity"].mean(), 2))

print("Average Energy:",
      round(df["energy"].mean(), 2))

print("Average Danceability:",
      round(df["danceability"].mean(), 2))

print("Average Valence:",
      round(df["valence"].mean(), 2))

print("Average Song Duration:",
      round(df["duration_minutes"].mean(), 2), "minutes")

print("\nMost Popular Song:")

popular_song = df.loc[df["popularity"].idxmax()]

print("Song:", popular_song["track_name"])
print("Artist:", popular_song["artists"])
print("Popularity:", popular_song["popularity"])

print("\nTop 10 Music Genres:")
print(df["track_genre"].value_counts().head(10))

print("\nAverage Popularity by Explicit Status:")
print(df.groupby("explicit")["popularity"].mean().round(2))

print("\nAverage Energy by Genre:")
print(
    df.groupby("track_genre")["energy"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
    .round(2)
)

print("\n" + "=" * 55)
print("ALL VISUALIZATIONS GENERATED SUCCESSFULLY!")
print("Output Folder:", OUTPUT_DIR)
print("=" * 55)
