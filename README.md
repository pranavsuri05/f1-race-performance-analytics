# F1 Race & Performance Analytics

An end-to-end Formula 1 analytics project using SQL, Python, and Power BI to analyze race results, driver performance, constructor performance, season trends, and grid-to-finish performance.

## Project Overview

This project analyzes historical Formula 1 race data across drivers, constructors, races, and circuits.

The workflow covers:

- Data validation and cleaning using Python
- Joining multiple F1 datasets into a unified analytical dataset
- SQL-based performance analysis using SQLite
- Python-based data visualization
- Interactive Power BI dashboard for exploration and filtering

## Project Architecture

```text
Raw F1 CSV Data
       |
       v
Python / Pandas
Data Cleaning & Transformation
       |
       v
Cleaned Analytical Dataset
       |
       +--------------------+
       |                    |
       v                    v
   SQLite / SQL          Python
   Analysis              Visualizations
       |                    |
       +---------+----------+
                 |
                 v
          Power BI Dashboard


