import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os

# ---------------------------------------------------------
# SETUP
# ---------------------------------------------------------

os.makedirs("output", exist_ok=True)

connection = sqlite3.connect("output/f1_analytics.db")


# =========================================================
# 1. TOP 10 DRIVERS BY TOTAL POINTS
# =========================================================

query = """
SELECT
    driver_name,
    SUM(points) AS total_points
FROM f1_results
GROUP BY driver_name
ORDER BY total_points DESC
LIMIT 10;
"""

drivers = pd.read_sql_query(query, connection)

plt.figure(figsize=(10, 6))

plt.barh(
    drivers["driver_name"][::-1],
    drivers["total_points"][::-1]
)

plt.xlabel("Total Points")
plt.ylabel("Driver")
plt.title("Top 10 F1 Drivers by Total Points")

plt.tight_layout()

plt.savefig(
    "output/top_10_drivers_points.png",
    dpi=300
)

plt.close()


# =========================================================
# 2. TOP 10 CONSTRUCTORS BY TOTAL POINTS
# =========================================================

query = """
SELECT
    constructor_name,
    SUM(points) AS total_points
FROM f1_results
GROUP BY constructor_name
ORDER BY total_points DESC
LIMIT 10;
"""

constructors = pd.read_sql_query(query, connection)

plt.figure(figsize=(10, 6))

plt.barh(
    constructors["constructor_name"][::-1],
    constructors["total_points"][::-1]
)

plt.xlabel("Total Points")
plt.ylabel("Constructor")
plt.title("Top 10 F1 Constructors by Total Points")

plt.tight_layout()

plt.savefig(
    "output/top_10_constructors_points.png",
    dpi=300
)

plt.close()


# =========================================================
# 3. POINTS BY SEASON
# =========================================================

query = """
SELECT
    year,
    SUM(points) AS total_points
FROM f1_results
GROUP BY year
ORDER BY year;
"""

season_points = pd.read_sql_query(query, connection)

plt.figure(figsize=(12, 6))

plt.plot(
    season_points["year"],
    season_points["total_points"]
)

plt.xlabel("Season")
plt.ylabel("Total Points")
plt.title("F1 Points Awarded by Season")

plt.tight_layout()

plt.savefig(
    "output/points_by_season.png",
    dpi=300
)

plt.close()


# =========================================================
# 4. GRID POSITION VS FINISHING POSITION
# =========================================================

query = """
SELECT
    grid,
    ROUND(AVG(position), 2) AS average_finish,
    COUNT(*) AS race_entries
FROM f1_results
WHERE grid > 0
  AND position IS NOT NULL
GROUP BY grid
ORDER BY grid;
"""

grid_analysis = pd.read_sql_query(query, connection)

plt.figure(figsize=(10, 6))

plt.scatter(
    grid_analysis["grid"],
    grid_analysis["average_finish"],
    s=grid_analysis["race_entries"] / 5
)

plt.xlabel("Starting Grid Position")
plt.ylabel("Average Finishing Position")
plt.title("Starting Grid Position vs Average Finishing Position")

plt.gca().invert_yaxis()

plt.tight_layout()

plt.savefig(
    "output/grid_vs_finish.png",
    dpi=300
)

plt.close()


# ---------------------------------------------------------
# CLOSE DATABASE
# ---------------------------------------------------------

connection.close()

print("All visualizations created successfully.")

print("\nFiles created:")

print("output/top_10_drivers_points.png")
print("output/top_10_constructors_points.png")
print("output/points_by_season.png")
print("output/grid_vs_finish.png")