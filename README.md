# Projet Mathématiques et Signal - Analyse des cycles météorologiques

## Auteurs
MALEGUE Gabriel, PASTRES Nolan, SCHOSSIG Guillaume (1A IR)

## Description
Ce projet vise à analyser les séries temporelles météorologiques de la station de Strasbourg-Entzheim (1950-2024) pour identifier les cycles annuels, synoptiques et pluri-annuels.
Les variables étudiées incluent :
- Températures (moyenne, minimale, maximale)
- Précipitations
- Chutes de neige
- Vitesse du vent et pics de rafales
- Pression atmosphérique
- Durée d’ensoleillement

L’analyse est réalisée à l’aide de **séries temporelles** et **d’analyses fréquentielles** (transformée de Fourier).

## Contenu du projet
- `strasbourg_entzheim.csv` : données météorologiques brutes
- `boxplot.py` : génération d'histogrammes et de diagrammes à moustaches pour la description statistiques des données
- `corrélation_météo_temporel.py` : création des graphiques temporelles
- `corrélation_météo_fréquentiel.py` : création des spectres fréquentiels
- `environment.yml` : fichier pour créer l’environnement Conda
- `requirements.txt` : fichier pour créer un environnement virtuel (venv)