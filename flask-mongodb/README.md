
### Run 
- docker-compose up
- mongodb://root:pass@localhost:27017/admin
- http://localhost:5000/animals
- pytest

### Service MongoDB
- docker-compose up -d mongodb
- docker-compose stop mongodb

### Service Redis
- docker-compose up -d redis
- docker-compose stop redis

### Service API
- docker-compose up --force-recreate --build app
- docker-compose up -d app
- docker-compose stop app
- docker logs flask-mongodb-app-1 -f


### Pipenv
- pip install pipenv
- pipenv install -r requirements.txt
- pipenv shell
- pipenv graph
- exit

### Virtualenv
- pip install virtualenv
- Install
    - virtualenv env
    - python -m venv ./env
    - .\env\Scripts\activate
    - pip install -r requirements.txt
    - pip list
- Develop
    - virtualenv env
    - pip install virtualenv
    - virtualenv env
    - .\env\Scripts\activate
    - pip install Flask
    - pip install pandas
    - python -m pip freeze > requirements.txt