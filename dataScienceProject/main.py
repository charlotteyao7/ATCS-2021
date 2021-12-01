# Author: Charlotte Yao
# Date: December 1, 2021
# Description: Data Science Final Project

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("environmental_impact_data.csv")
# Indices 0-24 (inclusive) are Republican states
# Indices 25-49 (inclusive) are Democratic states

# Convert columns to per capita
df["Carbon dioxide emitted per capita (metric tons) in 2018"] = df["Carbon dioxide emitted (million metric tons) in 2018"] / (df["Total population in 2020"]) * 1000000
df["Deforestation per capita (meters squared) in 2020"] = df["Deforestation (ha) in 2020"] / (df["Total population in 2020"]) * 10000
df["Daily water withdrew per capita (gallons) in 2015"] = df["Daily water withdrew (million gallons) in 2015"] / (df["Total population in 2020"]) * 1000000
df["Energy consumption per capita (million Btu) in 2019"] = df["Energy consumption (trillion Btu) in 2019"] / (df["Total population in 2020"]) * 1000000

# --- CARBON EMISSIONS BOXPLOT ---
repCarbon = df[0:25]["Carbon dioxide emitted per capita (metric tons) in 2018"]
demCarbon = df[25:50]["Carbon dioxide emitted per capita (metric tons) in 2018"]
plt.boxplot([repCarbon, demCarbon])
plt.xlabel("Political Party Affiliation")
plt.ylabel("Carbon dioxide emitted per capita (metric tons)")
plt.title("Carbon Emissions in 2018")
plt.xticks(ticks=[1, 2], labels=["Republican", "Democrat"])
plt.show()

# --- WATER USE PIE CHART ---
repWaterCount = 0
demWaterCount = 0
for row in df[0:25]["Daily water withdrew per capita (gallons) in 2015"]:
    repWaterCount += int(row)
for row in df[25:50]["Daily water withdrew per capita (gallons) in 2015"]:
    demWaterCount += int(row)
plt.pie([repWaterCount, demWaterCount], labels=["Republican", "Democrat"], autopct="%1.2f%%", colors=["red", "blue"])
plt.title("Sum of Daily Water Withdrew per Capita (gallons) in 2015")
plt.show()

# --- LANDFILL PRODUCTION BAR GRAPH ---
repStates = df[0:25]["State"]
repTrash = df[0:25]["Landfill dumped per capita (tons) in 2019"]
plt.figure(figsize=(12, 8))
plt.bar(repStates, repTrash, color="red")
demStates = df[25:50]["State"]
demTrash = df[25:50]["Landfill dumped per capita (tons) in 2019"]
plt.bar(demStates, demTrash, color="blue")
plt.xticks(rotation=90)
plt.title("Landfill Production in 2019")
plt.xlabel("State")
plt.ylabel("Landfill dumped per capita (tons)")
plt.show()

# --- FOOD WASTE PIE CHART ---
repWasteCount = 0
demWasteCount = 0
for row in df[0:25]["Groceries wasted per capita (dollars) in 2010"]:
    repWasteCount += float(row)
for row in df[25:50]["Groceries wasted per capita (dollars) in 2010"]:
    demWasteCount += float(row)
plt.pie([repWasteCount, demWasteCount], labels=["Republican", "Democrat"], autopct="%1.2f%%", colors=["red", "blue"])
plt.title("Sum of Groceries Wasted per Capita (dollars) in 2010")
plt.show()

# --- DEFORESTATION PIE CHART ---
repTreeCount = 0
demTreeCount = 0
for row in df[0:25]["Deforestation per capita (meters squared) in 2020"]:
    repTreeCount += float(row)
for row in df[25:50]["Deforestation per capita (meters squared) in 2020"]:
    demTreeCount += float(row)
plt.pie([repTreeCount, demTreeCount], labels=["Republican", "Democrat"], autopct="%1.2f%%", colors=["red", "blue"])
plt.title("Sum of Deforestation per Capita (meters squared) in 2020")
plt.show()

# --- ENERGY USE BOX PLOT ---
repEnergy = df[0:25]["Energy consumption per capita (million Btu) in 2019"]
demEnergy = df[25:50]["Energy consumption per capita (million Btu) in 2019"]
plt.boxplot([repEnergy, demEnergy])
plt.xlabel("Political Party Affiliation")
plt.ylabel("Energy consumed per capita (million Btu)")
plt.title("Energy Consumption in 2019")
plt.xticks(ticks=[1, 2], labels=["Republican", "Democrat"])
plt.show()