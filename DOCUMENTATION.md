This HNGx CRUD Person REST API. This API allows you to manage
and interact with a "Person" resource, performing CRUD (Create, Read, Update, Delete)
operations on individuals' data.
## Table of Contents
- [Setup](#setup-instructions)
- [API Endpoints](#api-endpoints)
- [Create Person](#create-person)
- [Get Person Details](#get-person-details)
- [Update a Person](#update-a-person)
- [Delete a Person](#delete-a-person)
- [Request/Response Formats](#requestresponse-formats)
- [Sample Usage](#sample-usage)
- [Limitations](#limitations)
## Setup instructions
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
6. Run the app
    ```python app.py```
## API Endpoints
### Create Person
- **Request type:** POST
- **Endpoint:** `/api`
- **Description:** Create a new person.
- **Request Format**
    - Body:
    ```json
    {
    "name": "John Doe",
    "email": "john@example.com",
    "age": 32
    }
    ```
- **Response Format:**
    - Status Code: 201 (Created)
    - Body:
    ```json
    {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com"
    }
    ```
### Get Person Details
- **Request type:** GET
- **Endpoint:** `/api/<user_id>`
- **Description:** Retrieve details of a person by their ID.
- **Request Format:** None required.
- **Response Format:**
    - Status Code: 200 (OK)
    - Body:
    ```json
    {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com"
    }
    ```
### Update a Person
- **Request type:** PATCH
- **Endpoint:** `PUT /api/<user_id>`
- **Description:** Update details of an existing person.
- **Request Format:**
    - Body:
    ```json
    {
    "name": "Updated John Doe",
    "email": "updated_john@example.com"
    }
    ```
- **Response Format:**
    - Status Code: 200 (OK)
    - Body:
    ```json
    {
    "id": 1,
    "name": "Updated John Doe",
    "email": "updated_john@example.com"
    }
    ```
### Delete a Person
- **Request type:** DELETE
- **Endpoint:** `DELETE /api/<user_id>`
- **Description:** Remove a person.
- **Request Format:** None required.
- **Response Format:** No content (204 No Content)
## Request and Response Formats
- **Request Format:**
    - JSON format is used for all data exchanges with the API endpoints.
- **Response Format:**
    - Successful responses provide data in JSON format.
    - Errors are conveyed through suitable HTTP status codes and accompanied by error messages in JSON format.
## Sample Usage
Here are some example API requests:
- Create a new person:
```python
import requests

url = "https://hngx-stage-two-6m3a.onrender.com/api"
data = {
    "name": "John Doe",
    "email": "john@example.com"
}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=data, headers=headers)
print(response.status_code)
print(response.json())
```
- Retrieve details of a person:
```python
import requests

url = "https://hngx-stage-two-6m3a.onrender.com/api/2"

response = requests.get(url)
print(response.status_code)
print(response.json())
```
- Update details of a person:
```python
import requests

url = "https://hngx-stage-two-6m3a.onrender.com/api/2"
data = {
    "name": "Updated John Doe",
    "email": "updated_john@example.com"
}

response = requests.put(url, json=data, headers=headers)
print(response.status_code)
print(response.json())
```
- Remove a person:
```python
import requests

url = "https://hngx-stage-two-6m3a.onrender.com/api/2"

response = requests.delete(url)
print(response.status_code)
print(response.json())

```
For more a more detailed documentation of the API, check out the [Postman Documentation](https://documenter.getpostman.com/view/29556247/2s9YC5xXVo)

## Limitations
- The API assumes that email addresses are unique, and it checks for email uniqueness when creating a new user.
- Error handling for invalid inputs is limited to basic checks
-The API does not currently support authentication or authorization for user operations.

## Setup Instructions
For detailed instructions on how to set up, run, and use this API, please refer to the
[README](README.md) file.