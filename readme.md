![badge](https://img.shields.io/static/v1?label=Project&nbsp;OC&message=13&color=blueviolet&style=for-the-badge)
![badge](https://img.shields.io/static/v1?label=Status&message=done&color=green&style=for-the-badge)

# ocrp13-Lettings

Scale a Django Application Using Modular Architecture.

![Logo orange_county_lettings](./logos/orangecountylettings.png "Logo")

****
### Description
The project's purpose is to discover the DevOps practices with CircleCI, DockerHub, Heroku and 
Sentry.  
This repository contains a basic django application which is automatically built, tested, saved and deployed on 
each push on main.

### Prerequisite
- GitHub account with read access to this repository
- Git CLI
- SQLite CL
- Python 3.6 or higher

### macOS / Linux
#### Clone repository
- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Create virtual environment
- `cd /path/to/ocrp13-Lettings`
- `python -m venv venv`
- `apt-get install python3-venv` (If the previous step has errors).
- Activate the environment `source venv/bin/activate`.
- Confirm that `python` command executes Python in the virtual environment as well `which python`.
- Confirm the python version is 3.6 or higher `python --version`.
- Confirm that `pip` command executes pip in the virtual environment as well `which pip`.
- To deactivate the virtual environment `deactivate`.

#### Run site
- `cd /path/to/ocrp13-Lettings`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Use your browser with this url `http://localhost:8000/`.
- Confirm that the site is running (the database already contains entries).

#### Linting
- `cd /path/to/ocrp13-Lettings`
- `source venv/bin/activate`
- `flake8`

#### Unit tests
- `cd /path/to/ocrp13-Lettings`
- `source venv/bin/activate`
- `pytest -vs`

#### Database
- `cd /path/to/ocrp13-Lettings`
- Open a shell session `sqlite3`
- Connect to the database : `.open oc-lettings-site.sqlite3`
- Display tables `.tables`
- Display columns in the profile table `pragma table_info(oc_lettings_site_profile);`
- Launch a request on the profile table, `select user_id, favorite_city from 
oc_lettings_site_profile where favorite_city like 'B%';`
- `.quit` to exit.

#### Administation panel
- Navigate to `http://localhost:8000/admin`
- Connect with the user : `admin`, `Abc1234!`

### Windows
Use PowerShell as above except :
- Activate the virtual environment, `.\venv\Scripts\Activate.ps1`
- Replace `which <my-command>` by `(Get-Command <my-command>).Path`

## Deployment
The Deployment needs these platforms which you have to subscribe to :

[CircleCI](https://circleci.com/) : Allows you to manage continuous integration and deployment.  
[DockerHub](https://hub.docker.com) :
Docker allows you to create containers/images to execute our application in an isolated environment.  
DockerHub is a cloud to save these images.  
[Heroku](https://www.heroku.com) : Allows the running of the application (Install Heroku CLI).  
[Sentry](https://sentry.io/welcome/) : Allows you to catch bugs in production.  


#### Configuration :
**1 - Sentry :**  
Create a new project (type django) and copy the given *DSN* key.

**2 - Heroku :**  
Create a new application and copy its name. Heroku will help to link your local folder 
with the heroku repository.
Once folders have been linked, enter these two variables in the Heroku environment with these commands :  
`heroku config:set SECRET_KEY=<votre clef django>`  
`heroku config:set SENTRY_DSN=<votre clef dsn donnée par sentry>`  

You can see the current variables with `heroku config`.

**3 - DockerHub :**  
Create a repository with the same Heroku application name.  

**4 - CircleCI :**  
In the tab *projects*, search your GitHub repository and click on the button *Set Up Project*. Then select the 
*Fastest* method. Due to this method, CircleCI will use the configuration file *.circleci/config.yml*.  

From the main menu, navigate into *Organization Settings/Contexts* to create a context.  
The latter allows you to save variables used in the configuration file.  
Create a context name : `oc-lettings-context` and add these variables to it :  

`DOCKER_LOGIN` : Votre login DockerHub  
`DOCKER_PASSWORD` : Password DockerHub  
`HEROKU_APP_NAME` : Your application name (the same used in DockerHub)  
`HEROKU_API_KEY` : Your API key given by Heroku  

#### Production application launching
Each push on the main branch sets off :  

1. **build-and-test** : Create a Docker image to launch the application. Then validate test with Pytest and lint 
with Flake8.
2. **publish-dockerhub** : If the build-and-test has been validated, save the image on DockerHub.
3. **heroku-deployment** : If the publish-dockerhub has been validated, update the application on Heroku.

You can see these steps on the CircleCI dashboard.  
You can open the application with the command `heroku open`.  

#### Local application launch

##### Django
See the section [Run site](#run-site)

##### DockerHub
Get an image name generated by a commit on your DockerHub and use the command :  
`docker run -it -p 8000:8000 <nom de l'image>`

The server will run on the url `http://localhost:8000/`.

##### Heroku
Open a terminal, navigate into the application folder. Activate the virtual environment and 
enter the command `heroku local`.

The server will run on the url `http://0.0.0.0:5000/`.
