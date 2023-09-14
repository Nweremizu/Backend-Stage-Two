import requests

BASE_URL = 'https://hngx-stage-two-6m3a.onrender.com/api'


def api_create_person(name:str, email:str, age:int):
    data ={
        'name': name,
        'email':email,
        'age': age
    }
    response = requests.post(url=BASE_URL, data=data)
    print(response.json())


def api_read_person(id:int):
    response = requests.get(url=f'{BASE_URL}/{id}')
    print(response.json())


def api_udate_person(id:int,name:str, email:str, age:int):
    data ={
        'name': name,
        'email':email,
        'age': age
    }
    response = requests.patch(url=f'{BASE_URL}/{id}', data=data)
    print(response.json())

def api_delete_person(id:int):
    response = requests.delete(url=f'{BASE_URL}/{id}')
    print(response.json())




api_create_person(name='Mark', email='br12@gmail.com', age=20)
api_read_person(id=2)

