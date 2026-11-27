
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import squarify

# Load Dataset
df = pd.read_csv(
    r"C:\Users\USER PC\Desktop\Airlines Flight\airlines_flights_data.csv"
)

sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (12, 7)

# Sample for faster visualization
sample = df.sample(10000, random_state=42)

# Create output folder
import os
os.makedirs("airline_charts", exist_ok=True)

def save_chart(name):
    plt.tight_layout()
    plt.savefig(f"airline_charts/{name}.png", dpi=300)
    plt.show()
    plt.close()

# =========================================
# 1. VIOLIN PLOT
# =========================================
plt.figure()
sns.violinplot(
    data=sample,
    x="airline",
    y="price",
    hue="airline",
    palette="Set2",
    legend=False
)
plt.title("Ticket Price Distribution by Airline")
plt.xticks(rotation=30)
save_chart("01_violin_plot")

# =========================================
# 2. TREEMAP
# =========================================
airline_counts = df["airline"].value_counts()

plt.figure(figsize=(12, 7))
squarify.plot(
    sizes=airline_counts.values,
    label=airline_counts.index,
    alpha=0.8,
    color=sns.color_palette("Set3", len(airline_counts))
)
plt.title("Airline Flight Distribution Treemap")
plt.axis("off")
save_chart("02_treemap")

# =========================================
# 3. SUNBURST CHART
# =========================================
fig = px.sunburst(
    df.sample(20000, random_state=42),
    path=["source_city", "destination_city", "airline"],
    values=None,
    title="Flight Routes Sunburst Chart"
)
fig.write_html("airline_charts/03_sunburst.html")
fig.show()

# =========================================
# 4. SANKEY DIAGRAM
# =========================================
routes = df.groupby(
    ["source_city", "destination_city"]
).size().reset_index(name="count")

top = routes.nlargest(25, "count")

cities = list(set(top["source_city"]) | set(top["destination_city"]))
city_id = {city: i for i, city in enumerate(cities)}

fig = px.bar(
    top,
    x="source_city",
    y="count",
    color="destination_city",
    title="Top Flight Route Connections"
)
fig.write_html("airline_charts/04_route_connections.html")
fig.show()

# =========================================
# 5. POLAR CHART
# =========================================
departure = df["departure_time"].value_counts()

angles = np.linspace(0, 2*np.pi, len(departure), endpoint=False)

fig = plt.figure()
ax = fig.add_subplot(111, projection="polar")

ax.bar(
    angles,
    departure.values,
    width=0.6,
    color=sns.color_palette("husl", len(departure))
)

ax.set_xticks(angles)
ax.set_xticklabels(departure.index)
ax.set_title("Departure Time Polar Chart")

save_chart("05_polar_chart")

# =========================================
# 6. BUBBLE CHART
# =========================================
bubble = sample.groupby("airline").agg(
    duration=("duration", "mean"),
    price=("price", "mean"),
    flights=("price", "size")
).reset_index()

plt.figure()
plt.scatter(
    bubble["duration"],
    bubble["price"],
    s=bubble["flights"] * 2,
    c=np.arange(len(bubble)),
    cmap="viridis",
    alpha=0.7
)

for _, row in bubble.iterrows():
    plt.annotate(
        row["airline"],
        (row["duration"], row["price"])
    )

plt.xlabel("Average Duration")
plt.ylabel("Average Price")
plt.title("Airline Duration vs Price Bubble Chart")
save_chart("06_bubble_chart")

# =========================================
# 7. DAYS LEFT HEATMAP
# =========================================
heat = df.pivot_table(
    values="price",
    index="days_left",
    columns="class",
    aggfunc="mean"
)

plt.figure(figsize=(10, 9))
sns.heatmap(heat, cmap="YlOrRd")
plt.title("Average Ticket Price by Days Left and Class")
save_chart("07_days_heatmap")

# =========================================
# 8. RIDGELINE-STYLE KDE PLOT
# =========================================
plt.figure(figsize=(12, 7))

for airline in df["airline"].unique():
    values = sample.loc[
        sample["airline"] == airline, "price"
    ]
    sns.kdeplot(
        values,
        label=airline,
        fill=False,
        linewidth=2
    )

plt.title("Flight Price Density by Airline")
plt.xlabel("Price")
plt.legend()
save_chart("08_density_plot")

# =========================================
# 9. JOINT PLOT
# =========================================
g = sns.jointplot(
    data=sample,
    x="duration",
    y="price",
    kind="hex",
    cmap="magma"
)
g.fig.suptitle("Flight Duration vs Price Joint Plot")
g.fig.savefig("airline_charts/09_joint_plot.png", dpi=300)
plt.show()
plt.close()

# =========================================
# 10. ECDF PLOT
# =========================================
plt.figure()

sns.ecdfplot(
    data=sample,
    x="price",
    hue="class"
)

plt.title("Cumulative Ticket Price Distribution")
save_chart("10_ecdf_plot")

# =========================================
# 11. STRIP PLOT
# =========================================
plt.figure()

sns.stripplot(
    data=sample.sample(2000, random_state=42),
    x="stops",
    y="price",
    hue="class",
    alpha=0.5,
    jitter=True
)

plt.title("Ticket Price Distribution by Stops")
save_chart("11_strip_plot")

# =========================================
# 12. SWARM PLOT
# =========================================
plt.figure()

sns.swarmplot(
    data=sample.sample(500, random_state=42),
    x="class",
    y="price",
    hue="class",
    palette="Set2",
    legend=False
)

plt.title("Ticket Price Swarm Plot")
save_chart("12_swarm_plot")

# =========================================
# 13. HEXBIN PLOT
# =========================================
plt.figure()

plt.hexbin(
    sample["duration"],
    sample["price"],
    gridsize=35,
    cmap="inferno",
    mincnt=1
)

plt.colorbar(label="Flight Count")
plt.xlabel("Duration")
plt.ylabel("Price")
plt.title("Flight Duration and Price Density")

save_chart("13_hexbin_plot")

# =========================================
# 14. PARALLEL COORDINATES
# =========================================
parallel = sample[
    ["duration", "days_left", "price"]
].copy()

parallel["class"] = sample["class"]

fig = px.parallel_coordinates(
    parallel,
    color="price",
    dimensions=["duration", "days_left", "price"],
    color_continuous_scale="Viridis",
    title="Parallel Coordinates Flight Analysis"
)

fig.write_html("airline_charts/14_parallel.html")
fig.show()

# =========================================
# 15. 3D SCATTER PLOT
# =========================================
fig = px.scatter_3d(
    sample.sample(3000, random_state=42),
    x="duration",
    y="days_left",
    z="price",
    color="class",
    title="3D Flight Price Analysis"
)

fig.write_html("airline_charts/15_3d_scatter.html")
fig.show()

# =========================================
# 16. BOXEN PLOT
# =========================================
plt.figure()

sns.boxenplot(
    data=sample,
    x="airline",
    y="price",
    hue="airline",
    palette="Set2",
    legend=False
)

plt.title("Advanced Price Distribution by Airline")
plt.xticks(rotation=30)
save_chart("16_boxen_plot")

# =========================================
# 17. LOLLIPOP CHART
# =========================================
avg = df.groupby("airline")["price"].mean().sort_values()

plt.figure()

plt.hlines(
    y=avg.index,
    xmin=0,
    xmax=avg.values,
    color="skyblue",
    linewidth=3
)

plt.scatter(avg.values, avg.index, color="red", s=100)

plt.title("Average Airline Price Lollipop Chart")
plt.xlabel("Average Price")

save_chart("17_lollipop_chart")

# =========================================
# 18. DUMBBELL CHART
# =========================================
price_class = df.groupby(
    ["airline", "class"]
)["price"].mean().unstack()

if "Economy" in price_class.columns and "Business" in price_class.columns:

    plt.figure(figsize=(12, 7))

    for airline, row in price_class.iterrows():
        plt.plot(
            [row["Economy"], row["Business"]],
            [airline, airline],
            marker="o",
            linewidth=3
        )

    plt.title("Economy vs Business Price Dumbbell Chart")
    plt.xlabel("Average Price")

    save_chart("18_dumbbell_chart")

# =========================================
# 19. CALENDAR-STYLE PRICE HEATMAP
# =========================================
calendar = df.pivot_table(
    values="price",
    index="days_left",
    columns="airline",
    aggfunc="mean"
)

plt.figure(figsize=(12, 12))

sns.heatmap(
    calendar,
    cmap="coolwarm",
    center=calendar.stack().median()
)

plt.title("Airline Price Variation by Days Left")
save_chart("19_price_calendar_heatmap")

# =========================================
# 20. AIRLINE MARKET SHARE DONUT
# =========================================
counts = df["airline"].value_counts()

plt.figure(figsize=(9, 9))

plt.pie(
    counts.values,
    labels=counts.index,
    autopct="%1.1f%%",
    startangle=90,
    wedgeprops={"width": 0.4},
    colors=sns.color_palette("Set2")
)

plt.title("Airline Market Share Distribution")
save_chart("20_donut_chart")

print("\n20 UNIQUE CHARTS GENERATED SUCCESSFULLY!")
print("Check the airline_charts folder.")

