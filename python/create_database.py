import pandas as pd
import sqlite3

# Load the cleaned analytical dataset
df = pd.read_csv("output/cleaned_f1_results.csv")

# Create SQLite database
connection = sqlite3.connect("output/f1_analytics.db")

# Store the cleaned data as a SQL table
df.to_sql(
    "f1_results",
    connection,
    if_exists="replace",
    index=False
)

connection.close()

print("SQLite database created successfully.")
print("Database: output/f1_analytics.db")
print("Table: f1_results")
print(f"Rows inserted: {len(df)}")