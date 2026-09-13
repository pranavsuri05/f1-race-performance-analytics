-- =====================================================
-- F1 RACE & PERFORMANCE ANALYTICS
-- SQL ANALYSIS QUERIES
-- =====================================================


-- 1. Top 10 Drivers by Total Points
-- Shows which drivers have accumulated the most points.

SELECT
    driver_name,
    SUM(points) AS total_points
FROM f1_results
GROUP BY driver_name
ORDER BY total_points DESC
LIMIT 10;


-- 2. Top 10 Constructors by Total Points
-- Shows constructor performance based on total points.

SELECT
    constructor_name,
    SUM(points) AS total_points
FROM f1_results
GROUP BY constructor_name
ORDER BY total_points DESC
LIMIT 10;


-- 3. Drivers with the Most Race Wins
-- Position 1 represents a race win.

SELECT
    driver_name,
    COUNT(*) AS wins
FROM f1_results
WHERE position = 1
GROUP BY driver_name
ORDER BY wins DESC
LIMIT 10;


-- 4. Total Points by Season
-- Shows how total points awarded changed over the years.

SELECT
    year,
    SUM(points) AS total_points
FROM f1_results
GROUP BY year
ORDER BY year;


-- 5. Average Finishing Position
-- Only includes drivers with at least 20 race entries
-- to avoid rankings based on very small samples.

SELECT
    driver_name,
    ROUND(AVG(position), 2) AS average_finish
FROM f1_results
WHERE position IS NOT NULL
GROUP BY driver_name
HAVING COUNT(*) >= 20
ORDER BY average_finish ASC
LIMIT 10;


-- 6. Grid Position vs Average Finishing Position
-- Helps analyze whether starting position influences
-- final race position.

SELECT
    grid,
    ROUND(AVG(position), 2) AS average_finish,
    COUNT(*) AS race_entries
FROM f1_results
WHERE grid > 0
  AND position IS NOT NULL
GROUP BY grid
ORDER BY grid;


-- 7. Most Successful Circuits
-- Counts the number of race wins at each circuit.

SELECT
    circuit_name,
    COUNT(*) AS wins
FROM f1_results
WHERE position = 1
GROUP BY circuit_name
ORDER BY wins DESC
LIMIT 10;


-- 8. Driver Performance by Season
-- Allows comparison of drivers across different seasons.

SELECT
    year,
    driver_name,
    SUM(points) AS total_points
FROM f1_results
GROUP BY year, driver_name
ORDER BY year, total_points DESC;