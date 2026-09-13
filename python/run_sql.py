import sqlite3

# Connect to SQLite database
connection = sqlite3.connect("output/f1_analytics.db")


# =====================================================
# QUERY 1 — TOP DRIVERS
# =====================================================

query = """
SELECT
    driver_name,
    SUM(points) AS total_points
FROM f1_results
GROUP BY driver_name
ORDER BY total_points DESC
LIMIT 10;
"""

print("\n" + "=" * 60)
print("TOP 10 DRIVERS BY TOTAL POINTS")
print("=" * 60)

results = connection.execute(query)

for row in results:
    print(row)


# =====================================================
# QUERY 2 — TOP CONSTRUCTORS
# =====================================================

query = """
SELECT
    constructor_name,
    SUM(points) AS total_points
FROM f1_results
GROUP BY constructor_name
ORDER BY total_points DESC
LIMIT 10;
"""

print("\n" + "=" * 60)
print("TOP 10 CONSTRUCTORS BY TOTAL POINTS")
print("=" * 60)

results = connection.execute(query)

for row in results:
    print(row)


# =====================================================
# QUERY 3 — MOST WINS
# =====================================================

query = """
SELECT
    driver_name,
    COUNT(*) AS wins
FROM f1_results
WHERE position = 1
GROUP BY driver_name
ORDER BY wins DESC
LIMIT 10;
"""

print("\n" + "=" * 60)
print("TOP 10 DRIVERS BY RACE WINS")
print("=" * 60)

results = connection.execute(query)

for row in results:
    print(row)


# =====================================================
# QUERY 4 — POINTS BY SEASON
# =====================================================

query = """
SELECT
    year,
    SUM(points) AS total_points
FROM f1_results
GROUP BY year
ORDER BY year;
"""

print("\n" + "=" * 60)
print("POINTS BY SEASON")
print("=" * 60)

results = connection.execute(query)

for row in results:
    print(row)


# Close database connection
connection.close()

print("\nSQL analysis completed successfully.")