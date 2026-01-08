import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(
    "strasbourg_entzheim.csv",
    sep=";",
    parse_dates=["time"],
    dayfirst=True
)

pd.set_option("display.max_columns", None)  # montre toutes les colonnes
print(df.describe())

variables = ["tavg", "prcp", "pres", "wspd", "tsun"]

# Histogrammes
for var in variables:
    plt.figure(figsize=(12,6))
    df[var].dropna().hist(bins=50)
    plt.title(f"Histogramme de {var}")
    plt.xlabel(var)
    plt.ylabel("Nombre de jours")
    plt.show()

# Boxplots ( moustaches)
for var in variables:
    plt.figure(figsize=(12,6))
    plt.boxplot(df[var].dropna(), vert=False)
    plt.title(f"Boxplot de {var}")
    plt.xlabel(var)
    plt.show()

