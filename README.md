# Backend-Stage-Two

## FLASK CRUD API

    A simple CRUD API with a datbase.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your system.


### INSTALLATION
1. Clone this Repository:
    (https://github.com/Nweremizu/Backend-Stage-Two.git)
2. Open your terminal and run
    ```virtualenv venv```
3. Activate the virtual environment
    * On windows, Run:
        ```venv\Scripts\activate```
    * On macOS and Linux, Run:
        ```source venv/bin/activates```
4. Install the required dependencies
    ```pip install -r requirements.txt```

5. If you want to work with a local db Just uncomment this code in the app.py
    ```python
        # os.environ['DATABASE_URI'] = 'sqlite:///users.db'
    ```

## Usage
### Running the Api

To run the API, execute the following command from the project directory:
    ```python app.py```

By default, the API will be accessible at `http://localhost:5000` for a Local DB


## API Endpoints
- `POST /api`: Create a new person.
- `GET /api/<user_id>`: Retrieve details of a person by their ID.
- `PUT /api/<user_id>`: Update details of an existing person.
- `DELETE /api/<user_id>`: Remove a person.

### Example Requests
* Create a new person:
    ##### Endpoint : '/api'
```python
BASE_URL = 'http://localhost:8000/api'
 data ={
        'name': 'Mark Essien',
        'email':'markessien123@gmail.com',
        'age': 32
    }
    response = requests.post(url=BASE_URL, data=data)
    print(response.json())
```

* Get details of a person
    ##### Endpoint : '/api/<int:user_id>'
```python
    user_id = 1
    BASE_URL = 'http://localhost:8000/api'
    response = requests.get(url=f'{BASE_URL}/{user_id}')
    print(response.json())
```
* Update Details of a person
    #### Endpoint : '/api/<int:user_id>'
```python
    user_id = 1
    BASE_URL = 'http://localhost:8000/api'
    data ={
        'age': 35 
    }
    response = requests.patch(url=f'{BASE_URL}/{user_id}', data=data)
    print(response.json())
```

* Delete a person from the database
    #### Endpoint : '/api/<int:user_id>'
```python
    user_id = 1
    BASE_URL = 'http://localhost:8000/api'
    response = requests.delete(url=f'{BASE_URL}/{user_id}')
    print(response.json())
```

## Documentation

For more information about the API, check out the [Documentation](DOCUMENTATION.md)

## Built With

- [Flask](https://flask.palletsprojects.com/en/1.1.x/) - The web framework used
- [SQLAlchemy](https://www.sqlalchemy.org/) - Database ORM
- [PostgreSQL](https://www.postgresql.org/) - Database
