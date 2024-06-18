---

# Monitoring System

Ce projet consiste en un système de monitoring avec une API pour récupérer des anomalies et un frontend pour afficher les données.

## Structure du projet

- **main.py**: Fichier principal contenant l'API FastAPI.
- **front/app.py**: Fichier principal du frontend Flask.
- **front/templates/**: Dossier contenant les fichiers HTML des templates.
- **anomalies.db**: Base de données SQLite utilisée par l'API pour stocker les anomalies.

## Configuration

1. **Installation des dépendances**

   Assurez-vous d'avoir Python installé. Installez ensuite les dépendances en exécutant :

   ```
   pip install requirement.txt
   ```

2. **Démarrage de l'API**

   Pour démarrer l'API avec FastAPI, exécutez :

   ```
   uvicorn main:app --host 127.0.0.1 --port 8000
   ```

   L'API sera disponible à l'adresse : `http://127.0.0.1:8000/`

3. **Démarrage du Frontend**

   Pour démarrer le frontend avec Flask, depuis le dossier `front/`, exécutez :

   ```
   cd front
    ```

   ```
   python app.py
   ```

   Le frontend sera disponible à l'adresse : `http://127.0.0.1:5000/`

## Fonctionnalités

- **Accueil (`/`)**: Affiche un message d'accueil de l'API.
- **Démarrage des prédictions (`/start`)**: Démarre les prédictions via l'API.
- **Anomalies (`/anomalie`)**: Affiche les données des anomalies dans un tableau.

## Utilisation

- Ouvrez votre navigateur et accédez à l'URL du frontend pour naviguer dans les différentes fonctionnalités.
- Les données sont récupérées depuis l'API FastAPI et affichées dynamiquement dans les templates HTML du frontend Flask.

## Avertissement

- Ce serveur de développement ne doit pas être utilisé en production. Utilisez un serveur WSGI tel que Gunicorn pour le déploiement en production.

---