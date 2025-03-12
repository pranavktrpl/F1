# Load required libraries
import pandas as pd

# Load datasets (note: the original datasets span up to 2020, but we restrict our analysis to 2010–2024)
circuits = pd.read_csv("formula-1-world-championship-1950-2020/circuits.csv")
races = pd.read_csv("formula-1-world-championship-1950-2020/races.csv")
lap_times = pd.read_csv("formula-1-world-championship-1950-2020/lap_times.csv")
qualifying = pd.read_csv("formula-1-world-championship-1950-2020/qualifying.csv")
results = pd.read_csv("formula-1-world-championship-1950-2020/results.csv")

with open("kaggle-dataset-description.txt", "w") as f:

    # Inspect the structure, summary statistics, and missing values
    if circuits.info()!=None: 
        f.write("Circuits info:")
        f.write(circuits.info())
    f.write("Circuits description:\n")
    f.write(circuits.describe().to_string(header=True, index=True))
    f.write(f"\nMissing values in circuits:{circuits.isna().sum().sum()}\n")

    if races.info()!=None: 
        f.write("\nRaces info:")
        f.write(races.info())
    f.write("Races description:\n")
    f.write(races.describe().to_string(header=True, index=True))
    f.write(f"\nMissing values in races:{races.isna().sum().sum()}\n")

    if lap_times.info()!=None: 
        f.write("\nLap times info:")
        f.write(lap_times.info())
    f.write("Lap times description:\n")
    f.write(lap_times.describe().to_string(header=True, index=True))
    f.write(f"\nMissing values in lap_times:{lap_times.isna().sum().sum()}\n")

    if qualifying.info()!=None: 
        f.write("Qualifying info:")
        f.write(qualifying.info())
    f.write("Qualifying description:\n")
    f.write(qualifying.describe().to_string(header=True, index=True))
    f.write(f"\nMissing values in qualifying:{qualifying.isna().sum().sum()}\n")

    if results.info()!=None: 
        f.write("\nResults info:")
        f.write(results.info())
    f.write("Results description:\n")
    f.write(results.describe().to_string(header=True, index=True))
    f.write(f"\nMissing values in results:{results.isna().sum().sum()}\n")


