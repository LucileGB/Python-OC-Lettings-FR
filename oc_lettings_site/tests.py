import pytest

from django.core.management import call_command

@pytest.fixture(scope='session')
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command('loaddata', 'data_test.json')

def test_index_get(client):
    response = client.get('/')
    assert response.status_code == 200

@pytest.mark.django_db
def test_index_letting_get(client):
    response = client.get('/lettings/')
#    print(response.content)
    assert response.status_code == 200

@pytest.mark.django_db
def test_letting_get(client):
    response = client.get('/lettings/1/')
    assert b"Joshua Tree Green Haus /w Hot Tub" in response.content
    assert response.status_code == 200

@pytest.mark.django_db
def test_index_profiles_get(client):
    response = client.get('/profiles/')
    assert response.status_code == 200

@pytest.mark.django_db
def test_profiles_get(client):
    response = client.get('/profiles/HeadlinesGazer/')
    assert b"HeadlinesGazer" in response.content
    assert response.status_code == 200
