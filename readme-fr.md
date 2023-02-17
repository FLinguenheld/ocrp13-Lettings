![badge](https://img.shields.io/static/v1?label=Project&nbsp;OC&message=13&color=blueviolet&style=for-the-badge)
![badge](https://img.shields.io/static/v1?label=Status&message=in_progess&color=blue&style=for-the-badge)

# ocrp13-Lettings

Scale a Django Application Using Modular Architecture.

![Logo orange_county_lettings](./logos/orangecountylettings.png "Logo")

****
## Résumé

Site web d'Orange County Lettings.

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre 
OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/ocrp13-Lettings`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activez l'environnement `source venv/bin/activate`
- Confirmez que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmez que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmez que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/ocrp13-Lettings`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Allez sur `http://localhost:8000/` dans un navigateur.
- Confirmez que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/ocrp13-Lettings`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/ocrp13-Lettings`
- `source venv/bin/activate`
- `pytest -vs`

#### Base de données

- `cd /path/to/ocrp13-Lettings`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(oc_lettings_site_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from 
oc_lettings_site_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Allez sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1`
- Remplacez `which <my-command>` par `(Get-Command <my-command>).Path`

## Déploiement

Le déploiement utilise ces différentes plateformes, vous avez besoin d'un compte pour chacune d'elles :  

[CircleCI](https://circleci.com) : Permet de gérer l'intégration continue et le déploiement.  
[DockerHub](https://hub.docker.com) :
Docker permet de créer des containers/images pour executer notre application dans un environnement isolé.
DockerHub est un cloud permettant de sauvegarder ses images.  
[Heroku](https://www.heroku.com) : Hebergeur de l'application. (installez heroku CLI)  
[Sentry](https://sentry.io/welcome/) : Permet de capturer les bugs en production.  


#### Configuration :
**1 - Sentry :**
Créez un nouveau projet de type django et copiez la clef *DSN* qui vous sera donnée.

**2 - Heroku :**
Créez une nouvelle application et copiez son nom. Heroku vous donnera les informations vous permettant de lier 
votre dossier contenant le projet avec votre dépôt Heroku.  
Une fois votre dossier lié, entrez ces deux variables dans l'environnement Heroku avec les commandes :  
`heroku config:set SECRET_KEY=<votre clef django>`  
`heroku config:set SENTRY_DSN=<votre clef dsn donnée par sentry>`  

Vous pouvez voir les variables actuellement enregistrées avec la commande `heroku config`

**3 - DockerHub :**
Créez un *repository* du même nom que votre application Heroku.

**4 - CircleCI :**
- Dans l'onglet *projects*, cliquez sur le bouton *Set Up Project* du dépôt *lettings*. Puis selectionnez 
la methode *Fastest*.
  Cette methode va utiliser le fichier de configuration se trouvant dans le dossier *.circleci/config.yml*.

- A partir du menu principal, rendez-vous dans *Organization Settings/Contexts* pour créer un contexte.
Ce dernier permet d'enregistrer des variables utilisées par le fichier config.yml.  
Créez le contexte : `oc-lettings-context` puis ajoutez les variables suivantes :  
`DOCKER_LOGIN` : Votre login DockerHub  
`DOCKER_PASSWORD` : Password DockerHub  
`HEROKU_APP_NAME`  : Le nom de votre application (le même que DockerHub)  
`HEROKU_API_KEY`  : Votre clef API donnée par Heroku  

#### Lancement du site en production

Chaque push sur la branche main déclenchera ces actions :
1. **build-and-test** : création d'une image avec Docker pour lancer l'application, validation des tests avec 
Pytest et du linter avec Flake8.
2. **publish-dockerhub** : Si build and test a fonctionné, enregistrement de l'image de l'application dans DockerHub.
3. **heroku-deployment** : Si publish-dockerhub a fonctionné, mise à jour de l'application dans le dépôt Heroku.

Vous pouvez voir ces étapes avec votre dashboard CircleCI.  
Vous pourrez ouvrir le site avec la commande `heroku open`.  

#### Lancement du site en local

##### Django
Voir la section [Exécuter le site](#exécuter-le-site)

##### DockerHub
Récupérez le nom de l'image générée par un commit puis entrez la commande :  
`docker run -it -p 8000:8000 <nom de l'image>`

Le serveur sera accessible avec votre navigateur à l'adresse `http://localhost:8000/`.

##### Heroku
Ouvrez un terminal, rendez-vous dans le dossier de l'application, activez l'environnement virtuel puis entrez 
la commande `heroku local`.

Le serveur sera accessible avec votre navigateur à l'adresse `http://0.0.0.0:5000/`.