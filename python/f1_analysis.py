import pandas as pd
import os

# ---------------------------------------------------------
# 1. LOAD DATA
# ---------------------------------------------------------

drivers = pd.read_csv("data/drivers.csv", na_values="\\N")
constructors = pd.read_csv("data/constructors.csv", na_values="\\N")
races = pd.read_csv("data/races.csv", na_values="\\N")
results = pd.read_csv("data/results.csv", na_values="\\N")
circuits = pd.read_csv("data/circuits.csv", na_values="\\N")

print("Data loaded successfully.")

print(f"Drivers: {drivers.shape}")
print(f"Constructors: {constructors.shape}")
print(f"Races: {races.shape}")
print(f"Results: {results.shape}")
print(f"Circuits: {circuits.shape}")


# ---------------------------------------------------------
# 2. CLEAN DATA TYPES
# ---------------------------------------------------------

races["date"] = pd.to_datetime(races["date"], errors="coerce")

results["position"] = pd.to_numeric(results["position"], errors="coerce")
results["grid"] = pd.to_numeric(results["grid"], errors="coerce")
results["points"] = pd.to_numeric(results["points"], errors="coerce")
results["laps"] = pd.to_numeric(results["laps"], errors="coerce")
results["fastestLapSpeed"] = pd.to_numeric(
    results["fastestLapSpeed"], errors="coerce"
)

print("\nData types cleaned.")


# ---------------------------------------------------------
# 3. CHECK MISSING VALUES
# ---------------------------------------------------------

print("\nMissing values in results:")
print(results.isnull().sum())


# ---------------------------------------------------------
# 4. MERGE TABLES
# ---------------------------------------------------------

analysis_df = results.merge(
    drivers[["driverId", "forename", "surname"]],
    on="driverId",
    how="left"
)

analysis_df = analysis_df.merge(
    constructors[["constructorId", "name"]],
    on="constructorId",
    how="left",
    suffixes=("", "_constructor")
)

analysis_df = analysis_df.merge(
    races[["raceId", "year", "round", "circuitId", "name", "date"]],
    on="raceId",
    how="left",
    suffixes=("", "_race")
)

analysis_df = analysis_df.merge(
    circuits[["circuitId", "name", "location", "country"]],
    on="circuitId",
    how="left",
    suffixes=("", "_circuit")
)


# ---------------------------------------------------------
# 5. CREATE READABLE COLUMN NAMES
# ---------------------------------------------------------

analysis_df["driver_name"] = (
    analysis_df["forename"] + " " + analysis_df["surname"]
)

analysis_df["constructor_name"] = analysis_df["name"]

analysis_df["race_name"] = analysis_df["name_race"]

analysis_df["circuit_name"] = analysis_df["name_circuit"]


# ---------------------------------------------------------
# 6. SELECT FINAL COLUMNS
# ---------------------------------------------------------

final_df = analysis_df[
    [
        "raceId",
        "year",
        "round",
        "race_name",
        "date",
        "circuitId",
        "circuit_name",
        "location",
        "country",
        "driverId",
        "driver_name",
        "constructorId",
        "constructor_name",
        "grid",
        "position",
        "points",
        "laps",
        "fastestLap",
        "rank",
        "fastestLapTime",
        "fastestLapSpeed",
        "statusId",
    ]
].copy()


# ---------------------------------------------------------
# 7. SORT DATA
# ---------------------------------------------------------

final_df = final_df.sort_values(
    ["year", "round", "position"],
    ascending=[True, True, True]
)


# ---------------------------------------------------------
# 8. SAVE CLEANED DATA
# ---------------------------------------------------------

os.makedirs("output", exist_ok=True)

final_df.to_csv(
    "output/cleaned_f1_results.csv",
    index=False
)

print("\nCleaned dataset created.")
print(f"Final dataset shape: {final_df.shape}")

print("\nFirst 5 rows:")
print(final_df.head())