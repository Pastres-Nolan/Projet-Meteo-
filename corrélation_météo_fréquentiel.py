import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# =========================
# Chargement des données
# =========================
df = pd.read_csv("strasbourg_entzheim.csv", sep=';')
df['time'] = pd.to_datetime(df['time'], dayfirst=True)

start_date = pd.to_datetime("01/01/2000", dayfirst=True)
end_date = pd.to_datetime("31/12/2024", dayfirst=True)

mask = (df['time'] >= start_date) & (df['time'] <= end_date)
df_filtered = df.loc[mask]

# =========================
# Variables étudiées
# =========================
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

# =========================
# Paramètres FFT et filtre
# =========================
sampling_frequency = 1       # 1 jour
end_freq = 0.006             # bande fréquentielle affichée
freq_threshold = 0.003       # fréquence à partir de laquelle on commence à atténuer
transition_width = 0.001     # largeur de la transition pour atténuation douce

# =========================
# Boucle sur les variables
# =========================
for title, serie in variables.items():

    signal = serie.dropna().values
    signal = signal - np.mean(signal)  # suppression DC
    N = len(signal)

    # FFT
    Y = np.fft.fft(signal)
    spectrum = np.abs(Y) / N
    freqs = np.abs(np.fft.fftfreq(N, d=1/sampling_frequency))

    # =========================
    # Atténuation fréquentielle douce
    # =========================
    attenuation = np.ones_like(freqs)

    mask = freqs > freq_threshold
    attenuation[mask] = 1 - (freqs[mask] - freq_threshold) / transition_width
    attenuation[mask] = np.clip(attenuation[mask], 0, 1)

    spectrum_att = spectrum * attenuation

    # Bande fréquentielle affichée
    mask_band = freqs <= end_freq
    f = freqs[mask_band]
    spec_raw = spectrum[mask_band]
    spec_att = spectrum_att[mask_band]

    # =========================
    # PLOT SUR LE MÊME GRAPHE
    # =========================
    plt.figure(figsize=(10,5))
    plt.plot(f, spec_raw, alpha=0.4, label="Spectre brut")
    plt.plot(f, spec_att, linewidth=2, label="Spectre bruit atténué")
    plt.axvline(1/365, color='r', linestyle='--', linewidth=1.5, label="Cycle annuel")
    plt.xlabel("Fréquence (cycles / jour)")
    plt.ylabel("Amplitude")
    plt.title(title)
    plt.grid()
    plt.legend()
    plt.tight_layout()
    plt.show()
