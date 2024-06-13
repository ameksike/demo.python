
### Run 
- docker-compose up
- mongodb://root:pass@localhost:27017/admin
- http://localhost:5000/animals

### Service MongoDB
- docker-compose up -d mongodb
- docker-compose stop mongodb

### Service Redis
- docker-compose up -d redis
- docker-compose stop redis

### Service API
- docker-compose up -d app
- docker-compose stop app
- docker logs flask-mongodb-app-1 -f