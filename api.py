import json
import requests
import settings


class Pets:
    """ API library to website http://34.141.58.52:8080/#/"""

    def __init__(self):
        self.base_url = 'http://34.141.58.52:8000/'

    def get_token(self) -> json:
        """Request to Swagger to get user's token (valid email ana password)"""
        data = {
            "email": settings.VALID_EMAIL,
            "password": settings.VALID_PASSWORD
        }
        # data = {
        #     "email": email,
        #     "password": settings.VALID_PASSWORD
        # }

        res = requests.post(self.base_url + 'login', data=json.dumps(data))
        my_token = res.json()['token']
        my_id = res.json()['id']
        status = res.status_code
        return my_token, status, my_id

    def get_list_users(self) -> json:
        my_token = Pets().get_token()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.get(self.base_url + 'users', headers=headers)
        status = res.status_code
        my_id = res.json()
        return status, my_id

    def create_pet(self) -> json:
        """Request to Swagger to create a pet"""
        my_token = Pets().get_token()[0]
        my_id = Pets().get_token()[2]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {
            "name": 'Vasya',
            "type": 'cat',
            "age": 5,
            "owner_id": my_id
        }
        res = requests.post(self.base_url + 'pet', data=json.dumps(data), headers=headers)
        pet_id = res.json()['id']
        status = res.status_code
        return pet_id, status

    def upload_pet_photo(self) -> json:
        """Request to Swagger to upload an image to a pet"""
        my_token = Pets().get_token()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        pet_id = Pets().create_pet()[0]
        files = {'pic': ('dog-puppy.jpg', open(r"C:\Users\dombr\PycharmProjects\Pet_API\tests\photo\dog-puppy.jpg",
                                               'rb'), 'image/jpg')}
        res = requests.post(self.base_url + f'pet/{pet_id}/image', headers=headers, files=files)
        status = res.status_code
        link = res.json()['link']
        return status, link

    def add_like_pet(self) -> json:
        """Request to Swagger to add a like to a pet"""
        my_token = Pets().get_token()[0]
        pet_id = Pets().create_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.put(self.base_url + f'pet/{pet_id}/like', headers=headers)
        status = res.status_code
        return status

    def add_comment_pet(self) -> json:
        """Request to Swagger to add a comment to a pet"""
        my_token = Pets().get_token()[0]
        pet_id = Pets().create_pet()[0]
        my_id = Pets().get_token()[2]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {
            "pet_id": pet_id,
            "message": "123456789",
            "user_id": my_id,
            "user_name": "df@mail.ru"
        }
        res = requests.put(self.base_url + f"pet/{pet_id}/comment", data=json.dumps(data), headers=headers)
        status = res.status_code
        comment_id = res.json()['id']
        return status, comment_id

    def get_pets_list(self) -> json:
        """Request to Swagger to get a list of pets by user's id (id+type+name)"""
        my_token = Pets().get_token()[0]
        my_id = Pets().get_token()[2]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {
            "user_id": my_id
        }
        res = requests.post(self.base_url + 'pets', data=json.dumps(data), headers=headers)
        status = res.status_code
        list_of_pets = res.json()
        return list_of_pets, status

    def get_pet_by_id(self) -> json:
        """Request to Swagger to get a pet by pet's id"""
        my_token = Pets().get_token()[0]
        pet_id = Pets().create_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.get(self.base_url + f'pet/{pet_id}', headers=headers)
        status = res.status_code
        pet_id_return = res.json()["pet"]["id"]
        return status, pet_id_return

    def update_pet(self) -> json:
        """Request to Swagger to update a pet"""
        my_token = Pets().get_token()[0]
        pet_id = Pets().create_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {
            "id": pet_id,
            "name": "Vasya",
            "type": "dog",
            "age": 1
        }
        res = requests.patch(self.base_url + 'pet', data=json.dumps(data), headers=headers)
        pet_id_return = res.json()['id']
        status = res.status_code
        return status, pet_id_return

    def delete_pet_by_id(self) -> json:
        """Request to Swagger to delete a pet by id"""
        my_token = Pets().get_token()[0]
        pet_id = Pets().create_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.delete(self.base_url + f'pet/{pet_id}', headers=headers)
        status = res.status_code
        return status


Pets().get_token()
Pets().get_list_users()
Pets().create_pet()
Pets().upload_pet_photo()
Pets().add_like_pet()
Pets().add_comment_pet()
Pets().get_pets_list()
Pets().get_pet_by_id()
Pets().delete_pet_by_id()
Pets().update_pet()
