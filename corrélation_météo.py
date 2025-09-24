import pandas as pd
import numpy as np
df = pd.read_csv('strasbourg_entzheim.csv', sep = ';')

time = df['time'] #date des relevé
tavg = df['tavg'] #température moyenne
tmin = df['tmin'] #température min
tmax = df['tmax'] #température max
prcp = df['prpc'] #précipitation (en mm) 
snow = df['snow'] #epaisseur des neiges (en mm)
wdir = df['wdir'] #direction du vent
wspd = df['wspd'] #vitesse du vent (en km/h)
wpdt = df['wpgt'] #pic de rafal (en km/h)
pres = df['pres'] #pression atmosphérique (en hpa)
tsun = df['tsun'] #durée d’ensoleillement (en minutes) 

np_time = np.array(time)
np_tmin = np.array(tmin)
np_tmax = np.array(tmax)
np_prcp = np.array(prcp)
np_snow = np.array(snow)
np_wdir = np.array(wdir)
np_wspd = np.array(wspd)
np_wpdt = np.array(wpdt)
np_pres = np.array(pres)
np_tsun = np.array(tsun)