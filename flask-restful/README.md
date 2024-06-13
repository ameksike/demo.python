
### Steps
- pip install Flask-RESTful
- python run.py
- python -m unittest discover -s tests

### Example
- ```curl http://127.0.0.1:5000/api/animals/1```
- ```curl -X DELETE http://127.0.0.1:5000/api/animals/1```
- ```curl -X PUT -H "Content-Type: application/json" -d '{"name": "Leopard", "species": "Panthera pardus"}' http://127.0.0.1:5000/api/animals/1 ```


