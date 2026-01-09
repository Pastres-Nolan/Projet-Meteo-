import pandas as pd
import matplotlib.pyplot as plt


# Lecture du fichier CSV
df = pd.read_csv("strasbourg_entzheim.csv", sep=';')
df['time'] = pd.to_datetime(df['time'], dayfirst=True)

# Filtrage par date
start_date = pd.to_datetime("01/01/2007", dayfirst=True)
end_date = pd.to_datetime("31/12/2012", dayfirst=True)

mask = (df['time'] >= start_date) & (df['time'] <= end_date)
df_filtered = df.loc[mask]

# Variables étudiées
variables = {
    "Température moyenne (tavg)": df_filtered['tavg'],
    "Température minimale (tmin)": df_filtered['tmin'],
    "Température maximale (tmax)": df_filtered['tmax'],
    "Précipitations (prcp)": df_filtered['prcp'],
    "Neige (snow)": df_filtered['snow'],
    "Vitesse du vent (wspd)": df_filtered['wspd'],
    "Rafales (wpgt)": df_filtered['wpgt'],
    "Pression (pres)": df_filtered['pres'],
    "Ensoleillement (tsun)": df_filtered['tsun']
}

time = df_filtered['time'] 

#Affichage
for title, data in variables.items():
    plt.figure(figsize=(14,7))
    plt.plot(time, data)
    plt.title(title)
    plt.xlabel("Temps")
    plt.ylabel(title)
    plt.grid()
    plt.tight_layout()
    plt.show()
