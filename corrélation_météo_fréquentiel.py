import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

# Chargement des données
df = pd.read_csv("strasbourg_entzheim.csv", sep=';')
df['time'] = pd.to_datetime(df['time'], dayfirst=True)

start_date = pd.to_datetime("01/01/1950", dayfirst=True)
end_date = pd.to_datetime("31/12/2024", dayfirst=True)

mask = (df['time'] >= start_date) & (df['time'] <= end_date)
df_filtered = df.loc[mask]

# Variables étudiées
variables = {
    "Température moyenne (tavg)": df_filtered['tavg'],
    "Température minimale (tmin)": df_filtered['tmin'],
    "Température maximale (tmax)": df_filtered['tmax'],
    "Précipitations (prcp)": df_filtered['prcp'].fillna(0),
    "Neige (snow)": df_filtered['snow'].fillna(0),
    "Vitesse du vent (wspd)": df_filtered['wspd'],
    "Rafales (wpgt)": df_filtered['wpgt'],
    "Pression (pres)": df_filtered['pres'].fillna(0),
    "Ensoleillement (tsun)": df_filtered['tsun']
}

# Paramètres FFT
sampling_frequency = 1
end_freq = 0.006

for title, serie in variables.items():

    signal = serie.dropna().values
    N = len(signal)

    # FFT bilatérale
    Y = fft(signal)
    spectrum = np.abs(Y) / N

    # Fréquences associées
    freqs = fftfreq(N, d=1/sampling_frequency)

    # Sélection bande [-end_freq ; +end_freq]
    mask = np.abs(freqs) <= end_freq
    freqs_plot = freqs[mask]
    spectrum_plot = spectrum[mask]
    
    plt.figure(figsize=(14,7))
    plt.plot(freqs_plot, spectrum_plot)
    plt.title("Spectre bilatéral - " + title)
    plt.xlabel("Fréquence (cycles/jour)")
    plt.ylabel("Amplitude")
    plt.grid()
    plt.tight_layout()
    plt.show()
