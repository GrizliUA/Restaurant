import pytest
import requests
from rest_framework import status

# Fixture to create a user
@pytest.fixture(autouse=True, scope='session')
def test_create_user():
    user = {
        'username': 'user',
        'password': 'user',
        'email': 'user@user.com'
    }

    response = requests.post(   f'http://127.0.0.1:8000/api/auth/token/?'
                                f'username={user["username"]}&'
                                f'password={user["password"]}&'
                                f'email={user["email"]}')

    assert response.status_code == status.HTTP_200_OK or response.status_code == status.HTTP_400_BAD_REQUEST
    return user



# Fixture to get an access token
@pytest.fixture(autouse=True, scope='session')
def test_get_token(test_create_user):
    response = requests.post(f'http://127.0.0.1:8000/api/token/',data=test_create_user)

    assert response.status_code == status.HTTP_200_OK
    return response.json()