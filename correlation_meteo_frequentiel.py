import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Lecture du fichier CSV
df = pd.read_csv("strasbourg_entzheim.csv", sep=';')
df['time'] = pd.to_datetime(df['time'], dayfirst=True)

# Filtrage par date
start_date = pd.to_datetime("01/01/1980", dayfirst=True)
end_date = pd.to_datetime("31/12/2024", dayfirst=True)

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

# Paramètres FFT
sampling_frequency = 1
end_freq = 0.006

for title, serie in variables.items():

    signal = serie.dropna()
    N = len(signal)
    # FFT bilatérale
    Y = np.fft.fft(signal)
    spectrum = np.abs(np.abs(Y) / N)

    # Fréquences associées
    freqs = np.abs(np.fft.fftfreq(N, d=1/sampling_frequency)) # pour bilatéral enlever le np.abs

    # Sélection bande [-end_freq ; +end_freq]
    mask = np.abs(freqs) <= end_freq
    freqs_plot = freqs[mask]
    spectrum_plot = spectrum[mask]

    plt.figure(figsize=(10,5))
    plt.plot(freqs_plot, spectrum_plot)
    plt.title(title)
    plt.xlabel("Fréquence")
    plt.ylabel("Amplitude")
    plt.grid()
    plt.tight_layout()


    plt.show()