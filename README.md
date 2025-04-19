# Projet de Surveillance de Température

Ce projet est une application web développée avec Flask et Dash pour surveiller et enregistrer les températures en temps réel. Il utilise également Streamz pour le traitement des flux de données et Plotly pour la visualisation.

## Table des Matières

1. [Fonctionnalités](#fonctionnalités)
2. [Installation](#installation)
3. [Utilisation](#utilisation)
4. [Exemple de Requête](#exemple-de-requête)
5. [Contributions](#contributions)
6. [Licence](#licence)

## Fonctionnalités

- **API RESTful** : Permet l'enregistrement des températures via une requête POST.
- **Tableau de bord interactif** : Visualisation des données de température en temps réel.
- **Gestion des CORS** : Permet les requêtes cross-origin pour l'API.
- **Notifications** : Envoi de notifications lorsque la température dépasse un seuil défini.
- **Historique des Températures** : Stockage et affichage des températures enregistrées sur une période donnée.

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

4. Visualisez les données de température en temps réel et consultez l'historique.

## Exemple de Requête

Voici un exemple de requête POST pour enregistrer une température :

```bash
curl -X POST http://localhost:5000/api/temperature -H "Content-Type: application/json" -d '{"temperature": 25.5}'
```

## Contributions

Les contributions sont les bienvenues ! Si vous souhaitez contribuer à ce projet, veuillez suivre ces étapes :

1. Forkez le projet.
2. Créez une nouvelle branche (`git checkout -b feature/YourFeature`).
3. Effectuez vos modifications et validez-les (`git commit -m 'Ajout d'une nouvelle fonctionnalité'`).
4. Poussez vos modifications (`git push origin feature/YourFeature`).
5. Ouvrez une Pull Request.

## Licence

Ce projet est sous licence MIT. Consultez le fichier [LICENSE](LICENSE) pour plus de détails.
