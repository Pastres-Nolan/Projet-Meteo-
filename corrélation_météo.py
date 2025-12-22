import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('strasbourg_entzheim.csv', sep=';')
df['time'] = pd.to_datetime(df['time'], dayfirst=True)

variables = {
    "Température moyenne (tavg)": df['tavg'],
    "Température minimale (tmin)": df['tmin'],
    "Température maximale (tmax)": df['tmax'],
    "Précipitations (prcp)": df['prcp'].fillna(0),
    "Neige (snow)": df['snow'].fillna(0),
    "Direction du vent (wdir)": df['wdir'],
    "Vitesse du vent (wspd)": df['wspd'],
    "Rafales (wpgt)": df['wpgt'],
    "Pression (pres)": df['pres'].fillna(0),
    "Ensoleillement (tsun)": df['tsun']
}

time = df['time']

for title, data in variables.items():
    plt.figure(figsize=(12, 5))
    plt.plot(time, data)
    plt.title(title)
    plt.xlabel("Temps")
    plt.ylabel(title)
    plt.grid()
    plt.show()


