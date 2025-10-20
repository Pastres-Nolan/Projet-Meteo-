import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('strasbourg_entzheim.csv', sep = ';')


df['time'] = pd.to_datetime(df['time'], dayfirst=True)
time = df['time'] #date des relevé
tavg = df['tavg'] #température moyenne
tmin = df['tmin'] #température min
tmax = df['tmax'] #température max
prcp = df['prcp'] #précipitation (en mm) 
snow = df['snow'] #epaisseur des neiges (en mm)
wdir = df['wdir'] #direction du vent
wspd = df['wspd'] #vitesse du vent (en km/h)
wpdt = df['wpgt'] #pic de rafal (en km/h)
pres = df['pres'] #pression atmosphérique (en hpa)
tsun = df['tsun'] #durée d’ensoleillement (en minutes) 

np_time = np.array(time)
np_tavg = np.array(tavg)
np_tmin = np.array(tmin)
np_tmax = np.array(tmax)
np_prcp = np.array(prcp)
np_snow = np.array(snow)
np_wdir = np.array(wdir)
np_wspd = np.array(wspd)
np_wpdt = np.array(wpdt)
np_pres = np.array(pres)
np_tsun = np.array(tsun)

# --- Données temporelles (1 an) ---
t_avg = np_tmin[:365]
t_time = np_time[:365]

# --- Conversion des dates en jours ---
t_days = (t_time - t_time[0]).astype('timedelta64[D]').astype(float)

# --- Tracé temporel ---
plt.figure(figsize=(10, 4))
plt.plot(t_days, t_avg)
plt.title("Signal temporel (température sur 1 an)")
plt.xlabel("Temps (jours depuis le début)")
plt.ylabel("Température minimale (°C)")
plt.grid()
plt.show()

# --- FFT ---
N = len(t_avg)
T = t_days[1] - t_days[0]
f = np.fft.fftfreq(N, T)
fft_values = np.fft.fft(t_avg)

mask = f > 0

plt.figure(figsize=(10, 4))
plt.plot(f[mask], np.abs(fft_values[mask]))
plt.title("Spectre en fréquence (FFT)")
plt.xlabel("Fréquence (cycles par jour)")
plt.ylabel("Amplitude")
plt.grid()
plt.show()