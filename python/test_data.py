import pandas as pd
drivers = pd.read_csv("data/drivers.csv")
constructors = pd.read_csv("data/constructors.csv")
races = pd.read_csv("data/races.csv")
results = pd.read_csv("data/results.csv")
circuits = pd.read_csv("data/circuits.csv")

print("Drivers:", drivers.shape)
print("Constructors:", constructors.shape)
print("Races:", races.shape)
print("Results:", results.shape)
print("Circuits:", circuits.shape)

print("\nDrivers:")
print(drivers.head())

print("\nResults:")
print(results.head())