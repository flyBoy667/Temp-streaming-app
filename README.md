# Projet de Surveillance de Température

Ce projet est une application web développée avec Flask et Dash pour surveiller et enregistrer les températures en temps réel. Il utilise également Streamz pour le traitement des flux de données et Plotly pour la visualisation.

## Fonctionnalités

- **API RESTful** : Permet l'enregistrement des températures via une requête POST.
- **Tableau de bord interactif** : Visualisation des données de température en temps réel.
- **Gestion des CORS** : Permet les requêtes cross-origin pour l'API.

## Installation

1. Clonez le dépôt :
   ```bash
   git clone <URL_DU_DEPOT>
   cd <NOM_DU_REPERTOIRE>
   ```

2. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

## Utilisation

1. Lancez le serveur Flask :
   ```bash
   python app.py
   ```

2. Accédez à l'API pour enregistrer une température :
   - URL : `http://localhost:5000/api/temperature`
   - Méthode : POST
   - Paramètre : `temperature` (float) - Température en degrés Celsius

3. Accédez au tableau de bord :
   - URL : `http://localhost:5000/dashboard/`

## Exemple de Requête

Voici un exemple de requête POST pour enregistrer une température :
